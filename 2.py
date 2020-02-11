
from PIL import Image
from numpy import *
from pylab import *
from scipy.ndimage import filters
from scipy import misc


im = array(Image.open('resize_dorm.jpg').convert('L'))
im1 = zeros(im.shape)
im1 = filters.gaussian_filter(im, 4)
im2 = 1.0*im1-im
im3 = clip(im - 1*im2, 0, 255)

figure(figsize=(16, 16))
gray()
subplot(2, 2, 1)
title('original')
imshow(uint8(im))

subplot(2, 2, 2)
title('LPF image')
imshow(uint8(im1))

subplot(2, 2, 3)
title('Unsharp mask')
imshow(uint8(im2+128))

subplot(2, 2, 4)
title('sharpened image')
imshow(uint8(im3))

show()

im = array(Image.open('resize_dorm.jpg'))
im1 = zeros(im.shape)
for i in range(3):
    im1[:, :, i] = filters.gaussian_filter(im[:, :, i], 4)
im2 = 1.0*im1-im
im3 = uint8(clip(im - 1*im2, 0, 255))

figure(figsize=(16, 16))
subplot(2, 2, 1)
title('original')
imshow(im)

subplot(2, 2, 2)
title('LPF image')
imshow(uint8(im1))

subplot(2, 2, 3)
title('Unsharp mask')
imshow(uint8(im2))

subplot(2, 2, 4)
title('sharpened image')
imshow(im3)

show()

