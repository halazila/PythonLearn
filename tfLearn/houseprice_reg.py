from __future__ import absolute_import, division, print_function

import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print('tensorflow version:', tf.__version__)

# 1) get data
boston_housing = keras.datasets.boston_housing

(train_data, train_labels), (test_data, test_labels) = boston_housing.load_data(path='boston_housing.npz')

print('Training set:{}'.format(train_data.shape)) # 404 examples, 13 features
print('Testing set:{}'.format(test_data.shape)) # 102 examples, 13 features

print(train_data[0])

column_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD',
                'TAX', 'PTRATIO', 'B', 'LSTAT']
df = pd.DataFrame(train_data, columns=column_names)
print(df.head())

print(train_labels[0:10])

# 2) feature normalize
mean = train_data.mean(axis=0)
std = train_data.std(axis=0)
train_data = (train_data - mean) / std
test_data = (test_data - mean) / std
print(train_data[0])

# 3) create model
def build_model():
	model = keras.Sequential([
		keras.layers.Dense(64, activation=tf.nn.relu, input_shape=(train_data.shape[1],)),
		keras.layers.Dense(64, activation=tf.nn.relu),
		keras.layers.Dense(1)
		])
	optimizer = tf.train.RMSPropOptimizer(0.001)
	model.compile(loss='mse', optimizer=optimizer, metrics=['mae'])
	return model

model = build_model()
model.summary()

# 4) train the model
class PrintDot(keras.callbacks.Callback):
	"""docstring for PrintDot"""
	def on_epoch_end(self, epoch, logs):
		if epoch % 100 == 0:
			print('')
		print('.', end='')

EPOCHS = 500

history = model.fit(train_data, train_labels, epochs=EPOCHS, validation_split=0.2, verbose=0, callbacks=[PrintDot()])


def plot_history(history):
	plt.figure()
	plt.xlabel('Epoch')
	plt.ylabel('Mean Abs Error [1000$]')
	plt.plot(history.epoch, np.array(history.history['mean_absolute_error']), label='Train Loss')
	plt.plot(history.epoch, np.array(history.history['val_mean_absolute_error']), label='Val Loss')
	plt.legend()
	plt.ylim([0, 5])
	# plt.show()

# plt.subplot(1,3,1)
plot_history(history)

# stop train early when loss descend hardly
model_early = build_model()
early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=20)
history_early = model_early.fit(train_data, train_labels, epochs=EPOCHS, validation_split=0.2, verbose=0, callbacks=[early_stop, PrintDot()])
# plt.subplot(1,3,2)
plot_history(history_early)

# 5) evaluate test data
[loss, mae] = model.evaluate(test_data, test_labels, verbose=0)
print('Testing set Mean Abs Error:${:7.2f}'.format(mae*1000))

# 6) predict
test_prediction = model.predict(test_data).flatten()
# plt.subplot(1,3,3)
plt.figure()
plt.scatter(test_labels, test_prediction)
plt.xlabel('True Values [1000$]')
plt.ylabel('Prediction [1000$]')
plt.axis('equal')
plt.xlim(plt.xlim())
plt.ylim(plt.ylim())
_ = plt.plot([-100, 100], [-100, 100])

error = test_prediction - test_labels
plt.figure()
plt.hist(error, bins=50)
plt.xlabel('Prediction Error [1000$]')
plt.ylabel('Count')

plt.show()
