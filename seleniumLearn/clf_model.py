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


def get_model():
	"""Summary
	
	Returns:
	    TYPE: Description
	"""
	my_model = keras.models.load_model('kaptcha_model.h5')
	return my_model


def clf_image(model, img):
	"""Summary
	
	Args:
	    model (TYPE): Description
	    img (TYPE): Description
	
	Returns:
	    TYPE: Description
	"""
	img = img.convert('L')
	img_arr = np.array(img)
	img_arr = img_arr / 255
	img_arr = np.transpose(img_arr, (1,0))
	img_arr = np.expand_dims(img_arr, 2)
	img_arr = np.expand_dims(img_arr, 0)
	predict = model.predict(img_arr)
	predict = predict.reshape(CAPTCHA_LENGTH, VOCAB_LENGTH)
	idx = np.argmax(predict, axis=1)
	text = ''
	for x in idx:
		text = (text + VOCAB[x])
	return text


def clf_authcode(img):
	model = get_model()
	return clf_image(model, img)