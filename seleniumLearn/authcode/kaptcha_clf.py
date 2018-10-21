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


train_path = './train_grey'
test_path = './test_grey'

train_images = os.listdir(train_path)
test_images = os.listdir(test_path)

train_data = []
train_labels = []
for f in train_images:
	image = Image.open(os.path.join(train_path, f))
	image_arr = np.array(image)
	image_arr = image_arr.reshape([-1])
	# print(image_arr.shape)
	train_data.append(list(image_arr))
	text = f.split('.')[0]
	train_labels.append(list(text2vec(text)))

train_data = np.array(train_data)
train_data = train_data.reshape([train_data.shape[0], IMAGE_HEIGHT, IMAGE_WIDTH])
train_data = np.transpose(train_data, (0, 2, 1))
print(train_data.shape)
train_labels = np.array(train_labels)
print(train_labels.shape)

print(train_data[0,:,:])
train_data = train_data / 255

train_data = np.expand_dims(train_data, 3)
print(train_data.shape)

model = keras.Sequential()

model.add(keras.layers.Conv2D(32, 5, strides=(1,1), padding='same', input_shape=(200,50,1), use_bias=True, activation=tf.nn.relu))
model.add(keras.layers.MaxPool2D(2, padding='same'))
model.add(keras.layers.Conv2D(64, 5, strides=(1,1), padding='same', use_bias=True, activation=tf.nn.relu))
model.add(keras.layers.MaxPool2D(5, padding='same'))
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(100, activation=tf.nn.softmax))
model.summary()

model.compile(optimizer=tf.train.AdamOptimizer(),
	loss='categorical_crossentropy',
	metrics=['accuracy'])
model.fit(train_data, train_labels, batch_size=512, epochs=40, verbose=1)

model.save('kaptcha_model.h5')
