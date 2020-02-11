import numpy as np
from PIL import Image
from pylab import *
from scipy.ndimage import measurements

im = np.array(Image.open('3.jpg').convert('L'))
im = 1*(im<128)

labels, nbr_objects = measurements.label(im)

print ("\n")
print ("Result")
figure(figsize=(6, 12))
imshow(labels)
show()

print ("\n")
print ("Number of Objects in Image :", nbr_objects)
print ("\n")

print ("Histogram")
figure()
hist(labels.flatten())
axis([5, 45, 0, 20000])
show()