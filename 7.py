import numpy as np
from PIL import *
from pylab import *
from scipy.ndimage import measurements, morphology

im2 = np.array(Image.open('resize_dorm.jpg').convert('L'))
im2 = 1*(im2<64)
im_open = morphology.binary_opening(im2, ones((6, 3)), iterations=4)


print ("\n")
print ("Hasil Pengolahan Morphology Function")
figure(figsize=(10, 10))
subplot(1, 2, 1)
imshow(im2)
subplot(1, 2, 2)
imshow(im_open)
show()

labels2, nbr_objects2 = measurements.label(im_open)
print ("\n")
print ("Number of Objects in Image :", nbr_objects2)
print ("\n")
center = measurements.center_of_mass(im_open, labels2, range(nbr_objects2))

print ("\n")
figure(figsize=(8, 8))
imshow(im_open)
for i in range(nbr_objects2):
    plot(center[i][1], center[i][0], "*")
print ("Hasil Pengolahan Center of Mass")
show()
