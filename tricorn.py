import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
import os
import imageio


def black(x, y, img):
    img[x][y] = [0, 0, 0]


def initWhite(img):
    length = img.shape[0]
    width = img.shape[1]
    for i in range(0, length):
        for j in range(0, width):
            # print((i, j))
            img[i][j] = np.array([255, 255, 255])


# print(im[1])
def drawOut(img):
    imgplot = plt.imshow(img)
    plt.show()


def formal(zi, m, c):
    ziconj = np.conj(zi)
    return np.power(ziconj, m) + c


# im = imageio.imread('sample.bmp')
# im = np.array(im)
#
# # 横向1000 纵向500 rgb3
# print(im.shape)
# # im[1]取的是第二横向
# # im[:,1]取的是第二列项
# width = im.shape[0]  # 500
# length = im.shape[1]  # 1000
# rgb = im.shape[2]


# this is a generate work!

# width = 20  # 20
# length = 20  # 20
# rgb = 3
# img = np.empty([length, width, rgb])
# print(img.shape)
#
r_start, r_end = -5, 5
(i_start, i_end) = (-5, 5)
# initWhite(img)
# drawOut(img)
#

m = 3
iterationMax = 50
res = 0.01
tmpArray = np.empty([int(3. / res) + 1, int(2. / res) + 1, 3])
print(tmpArray)
initWhite(tmpArray)
# a[-2~1] b[-1~1]
for a in np.arange(-2., 1. + res, res):
    for b in np.arange(-1., 1. + res, res):
        zi = 0
        for i in range(0, iterationMax):
            c = complex(a, b)
            zi1 = formal(zi, m, c)
            zi = zi1
        if (r_start < np.real(zi) < r_end
                and i_start < np.imag(zi) < i_end):
            black(int((a + 2.) / res), int((b + 1.) / res), tmpArray)
drawOut(tmpArray)
# zi1 = formal(zi, m, c)
# print(zi1)
# b = False
# for i in range(0, iterationMax):
#     if b:
#         break
#
#     x = int(np.real(zi1))
#     y = int(np.imag(zi1))
#     print(x, y)
#     if 0 < x < length:
#         if 0 < y < width:
#             black(x, y, img)
#             b = True
#     zi = zi1
#
