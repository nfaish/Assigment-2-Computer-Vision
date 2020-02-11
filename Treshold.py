import sys
import numpy as np
import skimage.io
import skimage.filters


# get filename and sigma value from command line
filename = sys.argv[1]
sigma = float(sys.argv[2])

# read the original image, converting to grayscale
img = skimage.io.imread(fname=filename, as_gray=True)

# blur before thresholding
blur = skimage.filters.gaussian(img, sigma=sigma)

# perform adaptive thresholding to produce a binary image
t = skimage.filters.threshold_otsu(blur)
binary = blur > t

# save binary image; first find beginning of file extension
dot = filename.index(".")
binary_file_name = filename[:dot] + "-binary" + filename[dot:]
skimage.io.imsave(fname=binary_file_name, arr=skimage.img_as_ubyte(binary))

# determine root mass ratio
rootPixels = np.nonzero(binary)
w = binary.shape[1]
h = binary.shape[0]
density = rootPixels / (w * h)

# output in format suitable for .csv
print(filename, density, sep=",")
