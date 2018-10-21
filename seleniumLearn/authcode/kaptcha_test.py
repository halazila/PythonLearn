import tensorflow as tf
from tensorflow import keras
import numpy as np
import os
from PIL import Image

IMAGE_HEIGHT = 50
IMAGE_WIDTH = 200
VOCAB = ['a', 'b', 'c', 'd', 'e','2', '3', '4', '5', '6', '7', '8','g','f','y','n','m','p','w','x']
CAPTCHA_LENGTH = 5
VOCAB_LENGTH = len(VOCAB)

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


my_model = keras.models.load_model('kaptcha_model.h5')
# my_model.summary()

# 灰度图，如果是rgb图像先转换为灰度图
test_path = './test_grey'

test_images = os.listdir(test_path)

totalnum = 0
correctnum = 0

for f in test_images:
	image = Image.open(os.path.join(test_path, f))
	image_arr = np.array(image)
	image_arr = image_arr / 255
	image_arr = np.transpose(image_arr, (1,0))
	image_arr = np.expand_dims(image_arr, 2)
	image_arr = np.expand_dims(image_arr, 0)
	# print(image_arr.shape)
	predict = my_model.predict(image_arr)
	predict = predict.reshape(CAPTCHA_LENGTH, VOCAB_LENGTH)
	# print(predict)
	idx = np.argmax(predict, axis=1)
	# print(idx)
	outstr = ''
	for x in idx:
		outstr = (outstr + VOCAB[x])
	print('original value:', f.split('.')[0], 'predict value:', outstr)

	totalnum = totalnum+1
	if outstr == f.split('.')[0]:
		correctnum = correctnum+1

print('total test image:', totalnum, 'predict correct image:', correctnum, 'correct rate:', correctnum/totalnum)

	