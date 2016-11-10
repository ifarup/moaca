#!/usr/bin/env python3

# Module for performing clustering, classification etc. for the ColourApp
from scipy import misc
from scipy.cluster.vq import vq, kmeans, kmeans2, whiten
import matplotlib.pyplot as plt
import numpy as np

#f = misc.face()  # retrieve a grayscale image
#plt.imshow(f)
#plt.show()

# Reads a image from a directory or use the generic "face"
#face = misc.face()
face = misc.imread("images/asdfghjk.png")
print(face.shape)

#misc.imsave('face.png', face) # First we need to create the PNG file
#face = misc.imread('face.png')

# Not vital in any way
#print(type(face))
#print(face[0])
#print('\n')
#print(face[0][0])
#print('\n')
#print(face[0][0][0])
#print(face.shape)

# Np array of length*width high and RGB wide, all zero
dimensions = face.shape
pictureArr = np.zeros(shape=(dimensions[0]*dimensions[1], dimensions[2]))


# Iterates over the picture and stores the values in the numpy array.
workaround = 0
k=0
for i in range(dimensions[0]):
    for j in range(dimensions[1]):
        pictureArr[workaround] = [face[i][j][k], face[i][j][k+1], face[i][j][k+2]]
        workaround += 1


# Does magic with the picture and returns cluster centers based on the wanted K.
    # Whiten is beneficial, why?
whitened = whiten(pictureArr)
kVal = 3
arr, lab = kmeans2(whitened, kVal)
print(arr)
for i in range(10):
    print(lab[i])








def cluster(im, k=0):

    #face = misc.face()
    #misc.imsave('face.png', face)
    #face = misc.imread('face.png')


    """
    Return clusters (array of centers) and classified image
    """
    k = 2
    dim = im.shape()
    dimArray = np.array[[dim[0]][dim[1]]]
    dimArray = np.ones(dimArray.shape())
    for i in range(dim[0]):
        for j in range(dim[1]/2):
            dimArray[i][j] = 0

    palettArr = np.array[k][3]
    palettArr[0] = {}
    return
