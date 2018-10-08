NUMBER = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
ALPHA_UPPER = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
ALPHA_LOWER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
# VOCAB = NUMBER + ALPHA_LOWER + ALPHA_UPPER
VOCAB = ['a', 'b', 'c', 'd', 'e','2', '3', '4', '5', '6', '7', '8','g','f','y','n','m','p','w','x']
CAPTCHA_LENGTH = 5
VOCAB_LENGTH = len(VOCAB)
TRAIN_DATA_LENGTH = 10000
TEST_DATA_LENGTH = 1000
TRAIN_IMAGE_PATH = './image/train'
TEST_IMAGE_PATH = './image/test'
TRAIN_DATA_PATH = './data/train'
TEST_DATA_PATH = './data/test'
IMAGE_HEIGHT = 50
IMAGE_WIDTH = 200