# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import pylab
import mnist_fashion_reader

print(tf.__version__)

# import Fashion-MNIST samples
train_images, train_labels = mnist_fashion_reader.load_mnist('data/fashion', kind='train')
test_images, test_labels = mnist_fashion_reader.load_mnist('data/fashion', kind='t10k')

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
print(train_images.shape)
print(len(train_labels))
print(test_images.shape)
print(len(test_labels))

# plt.figure()
# plt.imshow(train_images[10].reshape(28, 28))
# plt.colorbar()
# plt.grid(False)
# pylab.show()

# 图片归一化处理
train_images = train_images / 255.0
test_images = test_images / 255.0
# 显示训练集前25张图片
plt.figure(figsize=(10,10))
for i in range(25):
	plt.subplot(5,5,i+1)
	plt.xticks([])
	plt.yticks([])
	plt.grid(False)
	plt.imshow(train_images[i].reshape(28,28), cmap=plt.cm.binary)
	plt.xlabel(class_names[train_labels[i]])
pylab.show() # 加上才能显示图片

# 1) setup layers
model = keras.Sequential([
	keras.layers.Dense(128, activation=tf.nn.relu),
	keras.layers.Dense(10, activation=tf.nn.softmax)
	])

# 2) compile the model
model.compile(optimizer=tf.train.AdamOptimizer(), # optimizer
	loss='sparse_categorical_crossentropy', # loss function
	metrics=['accuracy']) # monitor the training and testing steps

# 3) train the model
model.fit(train_images, train_labels, epochs=5)

# 4) evaluate accuracy
test_loss, test_acc = model.evaluate(test_images, test_labels)
print('test accuracy:', test_loss)

# 5) make predictions
predictions = model.predict(test_images)
print(predictions[0])
print('test_images[0] prediction:', np.argmax(predictions[0]))
print('test_labels[0]:', test_labels[0])


