from numpy import *
from numpy import random
from scipy.ndimage import filters
from PIL import *
from pylab import *


im = zeros((500, 500))
im[100:400, 100:400] = 128
im[200:300, 200:300]=255
figure()
gray()
imshow(im)
show()

def edge(X, th):
    imx = zeros(X.shape)
    filters.sobel(X, 1, imx)
    imy = zeros(X.shape)
    filters.sobel(X, 0, imy)
    ims = sqrt(imx**2 + imy**2)
    ims[ims<th]=0
    ims[ims>=th]=1
    ims = uint8(ims)
    return ims

im2 = edge(im, 0.1)

figure()
gray()
imshow(im2)
show()