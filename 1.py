from PIL import Image
#from numpy import *
import numpy as np
from pylab import *
from scipy.ndimage import filters
from scipy import misc


im = np.array(Image.open('resize_dorm.jpg').convert('L'))

figure(figsize=(16,16))
gray()
subplot(2, 3, 1)
title('original')
imshow(im)

for i in range(5):
    subplot(2, 3, i+2)
    title('sigma='+str(i))
    im1 = filters.gaussian_filter(im, i)
    imshow(im1)

show()

figure(figsize=(16,16))
gray()
subplot(2, 3, 1)
title('original')
imshow(im)

for i in range(5):
    subplot(2, 3, i+2)
    title('sigma='+str(i))
    im1 = filters.gaussian_filter(im, i)
    imx = zeros(im1.shape)
    filters.sobel(im1, 1, imx)
    imy = zeros(im1.shape)
    filters.sobel(im1, 0, imy)
    imxy = sqrt(imx**2+imy**2)
    imshow(imxy)

show()