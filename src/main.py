import numpy as np
import cv2
from hist_equal import *
from clahe import *


if __name__ == "__main__":

    for iter in range(25):

        img = cv2.imread("./data/00000000%02d.png" % iter)

        hist1 = hist_equal(img)
        hist2 = adapt_hist_equal(img)

        hist1 = cv2.cvtColor(hist1, cv2.COLOR_GRAY2RGB)
        hist2 = cv2.cvtColor(hist2, cv2.COLOR_GRAY2RGB)

        empty1 = np.zeros((40, 1224, 3), np.uint8)

        vis = np.concatenate((empty1, hist1, empty1, hist2), axis=0)

        text1 = 'Histogram Equalization'
        text2 = 'Contrast Limited Adaptive Histogram Equalization'

        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(vis, text1, (30,25), font, 0.65, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(vis, text2, (30,435), font, 0.65, (0, 255, 255), 2, cv2.LINE_AA)

        cv2.imshow('Output', img)
        cv2.waitKey(1)