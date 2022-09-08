import numpy as np
import cv2

def hist_equal(img):

    width, length, _ = img.shape

    img_lin = np.reshape((cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY)), (width*length))

    freq = np.zeros((256))

    for i in range(len(freq)):
        freq[i] = np.sum(img_lin == i)

    freq = np.divide(freq, img_lin.shape[0])

    cdf = np.multiply(255, (np.cumsum(freq)))

    for i in range(len(img_lin)):
        img_lin[i] = cdf[img_lin[i]]
    img_hist_eq = np.reshape(img_lin, (width, length))

    return img_hist_eq