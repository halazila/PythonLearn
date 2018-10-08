# from os.path import join,exists
# from PIL import Image
# import numpy as np
# from config import *

# file = '../image/2a2fx.jpg'
# img = Image.open(file)
# # img.show()
# array = np.array(img)
# L = img.convert('L')
# # L.show()
# print(np.shape(L))
# L_array = np.array(L)
# rel_array = L_array.reshape((-1,np.shape(L_array)[1]*np.shape(L_array)[0]))
# print(np.shape(rel_array))
# print(L_array)
# print(rel_array)

# string = '2a2fx.jpg'
# spstr = string.split('.')[0]
# print(spstr)
# ab = [[1,2,3],[1,2,3],]
# print(np.shape(ab))

# import os
# path = '../image'
# files = os.listdir(path)
# print(files)
# img = Image.open(os.path.join(path,files[0]))
# # img.show()
# # print(files[-2])
# for x in range(-1,-10,-1):
# 	print(x)


# import os
# import numpy as np
# from PIL import Image
# file = '../image/2a2fx.jpg'
# captcha_img = Image.open(file)
# captcha_array = np.array(captcha_img)
# # captcha_img.show()
# # print(captcha_img)
# # print(np.shape(captcha_array))
# # print(captcha_array)
# captcha_bytes = captcha_img.tobytes()
# reconstructed_captcha_img = Image.frombytes(mode='RGB', size=captcha_img.size, data=captcha_bytes)
# reconstructed_captcha_array = np.array(reconstructed_captcha_img)
# print(np.allclose(captcha_array, reconstructed_captcha_array))
# print(captcha_array)



import time
print(time.time())