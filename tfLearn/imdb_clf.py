import tensorflow as tf
from tensorflow import keras
import numpy as np

print('tf.__version__:', tf.__version__)

imdb = keras.datasets.imdb


# 1) download imdb dataset
#path：如果你在本机上已有此数据集（位于'~/.keras/datasets/'+path），则载入。否则数据将下载到该目录下
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(path='imdb.npz', num_words=10000) 
# print('Training entries:{}, labels:{}'.format(len(train_data), len(train_labels)))
# print(train_data[0])
# print(len(train_data[0]), len(train_data[1]))
# print('train_labels[0]:', train_labels[0])


# 2) convert integers back to words
# imdb_word_index.json is https request, here download file failed, 
# using code requests.get(verify=False) to download file
word_index = imdb.get_word_index() 

# user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
# headers = {'User-Agent':user_agent}
# url = 'https://storage.googleapis.com/tensorflow/tf-keras-datasets/imdb_word_index.json'
# r = requests.get(url, headers=headers, verify=False)
# print(r.text)
# with open('imdb_word_index.json', 'w') as f:
# 	f.write(r.text)

# The first indices are reserved
word_index = {k:(v+3) for k, v in word_index.items()}
word_index['<PAD>'] = 0
word_index['<START>'] = 1
word_index['<UNK>'] = 2 # unknow
word_index['<UNUSED>'] = 3

reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])

def decode_review(text):
	return ' '.join([reverse_word_index.get(i, '?') for i in text])

# print(decode_review(train_data[0]))

# 3) prepare data
train_data = keras.preprocessing.sequence.pad_sequences(
	train_data, value=word_index['<PAD>'], padding='post', maxlen=256
	)
test_data = keras.preprocessing.sequence.pad_sequences(
	test_data, value=word_index['<PAD>'], padding='post', maxlen=256
	)
# print(train_data[0])


# 4) build the model
vocab_size = 10000
model = keras.Sequential()
model.add(keras.layers.Embedding(vocab_size, 16))
model.add(keras.layers.GlobalAveragePooling1D())
model.add(keras.layers.Dense(16, activation=tf.nn.relu))
model.add(keras.layers.Dense(1, activation=tf.nn.sigmoid))

model.summary()


# 5) loss function and optimizer
model.compile(optimizer=tf.train.AdamOptimizer(),
	loss='binary_crossentropy',
	metrics=['accuracy'])

# 6) create a validation set
x_val = train_data[:10000]
partial_x_train = train_data[10000:]
y_val = train_labels[:10000]
partial_y_train = train_labels[10000:]

# 7) train the model
history = model.fit(partial_x_train,
					partial_y_train,
					epochs=40,
					batch_size=512,
					validation_data=(x_val, y_val),
					verbose=1)

# 8) evaluate the model
results = model.evaluate(test_data, test_labels)
print(results)

# 9) predict test data
predict = model.predict(test_data)
print('test_labels[0]=', test_labels[0], 'test_data[0] prediction=', predict[0])

# 10) predict one data
pre_data = test_data[0]
pre_data = np.expand_dims(pre_data, 0)
print(pre_data.shape)
predict_single = model.predict(pre_data)
print(predict_single)