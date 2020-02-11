
from PIL import Image
from numpy import *
from scipy.ndimage import filters
from matplotlib import pyplot as plt

im = array(Image.open('dorm.jpg'))
im2 = zeros(im.shape)
for i in range(3):
    im2[:,:,i] = filters.gaussian_filter(im[:,:,i],2)
im2 = uint8(im2)

plt.subplot(121),plt.imshow(im),plt.title('Original Image')
plt.subplot(122),plt.imshow(im2),plt.title('Blurred Image 2')
plt.show()

im1 = zeros(im.shape)
for i in range(3):
    im1[:,:,i] = filters.gaussian_filter(im[:,:,i],5)
im1 = uint8(im1)
for i in range(3):
    im2[:,:,i] = filters.gaussian_filter(im[:,:,i],10)
im2 = uint8(im2)

plt.subplot(121),plt.imshow(im1),plt.title('Blurred Image 5')
plt.subplot(122),plt.imshow(im2),plt.title('Blurred Image 10')
plt.show()
