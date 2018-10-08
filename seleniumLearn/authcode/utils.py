import os
from PIL import Image
import numpy as np
from config import *
import pickle
import time
import tensorflow as tf


def text2vec(text):
	"""
	text to one-hot vector
	:param text:source text
	:return: np array
	"""
	if len(text) > CAPTCHA_LENGTH:
		return False
	vector = np.zeros(CAPTCHA_LENGTH * VOCAB_LENGTH)
	for i,c in enumerate(text):
		index = i * VOCAB_LENGTH + VOCAB.index(c)
		vector[index] = 1
	return vector

def vec2text(vector):
	"""
	vector to captcha text
	:param vector:np array
	:return:text
	"""
	if not isinstance(vector, np.ndarray):
		vector = np.asarray(vector)

	vector = np.reshape(vector, [CAPTCHA_LENGTH, -1])
	text = ''
	for item in vector:
		text += VOCAB[np.argmax(item)]
	return text

def generate_data(image_path, data_path, file_name):
	"""
	generate training and testing data 
	:param image_path: image path
	:param data_path: data path
	:param file_name: data file name
	:return:
	"""
	if not os.path.exists(image_path):
		raise ValueError('failed to find image path...')
	image_files = os.listdir(image_path)
	out_data = []
	# generate train data
	time1 = time.time()
	for i in range(len(image_files)):
		img_file = os.path.join(image_path, image_files[i])
		if not os.path.isdir(img_file):
			img = Image.open(img_file)
			img = np.array(img)
			r = img[:,:,0].flatten() #flatten---convert to 1-D vector
			g = img[:,:,1].flatten()
			b = img[:,:,2].flatten()
			text = image_files[i].split('.')[0]
			label = text2vec(text)
			out_data += (list(label) + list(r) + list(g) + list(b))

	time2 = time.time()
	out_data = np.array(out_data, np.uint8)
	if not os.path.exists(data_path):
		os.makedirs(data_path)
	out_data.tofile(os.path.join(data_path, file_name))
	time3 = time.time()
	print('read image time:' + str(time2 - time1))
	print('write data file time:' + str(time3 - time2))


def get_next_batch(eval_data, data_dir, batch_size=128): # 未完成
	"""Construct input for kaptcha evaluation using the Reader ops.

	Args:
	eval_data: bool, indicating if one should use the train or eval data set.
	data_dir: Path to the kaptcha data directory.
	batch_size: Number of images per batch.

	Returns:
	images: Images. 4D tensor of [batch_size, IMAGE_HEIGHT, IMAGE_WIDTH, 3] size.
	labels: Labels. 2D tensor of [batch_size, CAPTCHA_LENGTH * VOCAB_LENGTH] size.
	"""
	if not eval_data:
		filenames = [os.path.join(data_dir, 'data_batch_%d.bin' % i) for i in range(1, 6)]
	batch_x = np.zeros([batch_size, IMAGE_HEIGHT * IMAGE_WIDTH])
	batch_y = np.zeros([batch_size, CAPTCHA_LENGTH * VOCAB_LENGTH])


def read_kaptcha(filename_queue):
	"""read and parses examples from kaptcha data files.
	"""
	class KaptchaRecord(object):
		pass
	result = KaptchaRecord()

	# input format
	label_bytes = CAPTCHA_LENGTH * VOCAB_LENGTH
	result.height = IMAGE_HEIGHT
	result.width = IMAGE_WIDTH
	result.depth = 3
	image_bytes = result.height * result.width * result.depth
	# record consists of a label followed by the image
	record_bytes = label_bytes + image_bytes

	reader = tf.FixedLengthRecordReader(record_bytes = record_bytes)
	result.key, value = reader.read(filename_queue)

	# convert from a string to a vector of uint8 that is record_bytes long
	record_byets = tf.decode_raw(value, tf.uint8)

	result.label = tf.cast(
		tf.strided_slice(record_byets, [0], [label_bytes]), tf.int32)

	# The remaining bytes after the label represent the image, which we reshape
	# from [depth * height * width] to [depth, height, width].
	depth_major = tf.reshape(
		tf.strided_slice(record_bytes, [label_bytes], [label_bytes + image_bytes]),
		[result.depth, result.height, result.width])
	# Convert from [depth, height, width] to [height, width, depth].
	result.uint8image = tf.transpose(depth_major, [1, 2, 0])
	return result
			

if __name__ == '__main__':
	generate_data('./image/train', './data/train', 'train_data.bin')