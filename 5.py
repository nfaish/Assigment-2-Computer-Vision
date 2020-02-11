from numpy import *
from numpy import random
from scipy.ndimage import filters
from PIL import *
from pylab import *

def edge(X, th):
    imx = zeros(X.shape)
    filters.gaussian_filter(X, (2,2), (0,1), imx)
    imy = zeros(X.shape)
    filters.gaussian_filter(X, (2,2), (1,0), imy)
    ims = sqrt(imx**2 + imy**2)
    ims[ims<th]=0
    ims[ims>=th]=1
    ims = uint8(ims)
    return ims

im2 = array(Image.open('resize_dorm.jpg').convert('L'))

im2e = edge(im2, 8)

figure(figsize=(12, 12))
gray()
subplot(1, 2, 1)
imshow(im2)
subplot(1, 2, 2)
imshow(im2e)
show()


# Hough transform
im3 = zeros((256, 256))
for y in range(im2e.shape[0]):
    for x in range(im2e.shape[1]):
        if (im2e[y, x]>0):
            for i in range(256):            
                t = math.pi/2*i/256
                r = x*math.cos(t)+y*sin(t)
                r = r*255/sqrt(im2e.shape[0]**2 + im2e.shape[1]**2)
                im3[int(r), i] = im3[int(r), i] + 1
                
figure(figsize=(12, 12))
gray()
imshow(im3)
show()

peaks=[]
im4 = np.array(im3)
for i in range(4):
    ym = argmax(im4)/im4.shape[0]
    xm = argmax(im4)%im4.shape[0]
    peaks.append([ym, xm])
    im4[ym-10:ym+10, xm-10:xm+10] = -1
print (peaks)
figure()
imshow(im4)
show()

imshow(im4)
for [rmax, tmax] in peaks:
    rmax = 1.0*rmax
    tmax = 1.0*tmax
    print (rmax, tmax)
    im4 = im2.copy()
    t = math.pi/2*tmax/256
    r = rmax/256*math.sqrt(im2.shape[0]**2 + im2.shape[1]**2)
    print (t, tmax/256*90, r, math.sqrt(im2.shape[0]**2 + im2.shape[1]**2))
    x0 = 0
    y0 = r/math.sin(t)
    if (y0<0):
        y0 = 0
        x0 = r/math.cos(t)
    elif (y0>=im4.shape[0]):
        y0 = im4.shape[0]
        x0 = (r-y0*math.sin(t))/math.cos(t)
    x1 = im4.shape[1]
    y1 = (r - math.cos(t)*x1)/math.sin(t)
    if (y1<0):
        y1 = 0
        x1 = r/math.cos(t)
    elif (y1>=im4.shape[0]):
        y1 = im4.shape[0]
        x1 = (r-y1*math.sin(t))/math.cos(t)
    plot([x0, x1], [y0, y1])
    print ((x0, y0), (x1, y1))
show()