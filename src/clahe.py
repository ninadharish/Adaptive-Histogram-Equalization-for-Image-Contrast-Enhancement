import numpy as np
import cv2


def contrast_clipping(img):

    width, length = img.shape
    clip_limit = 40
    clipper = 0

    img_lin = np.reshape(img.copy(), (width*length))

    freq = np.zeros((256))
    for item in img_lin:
        freq[item] += 1

    for i in range(len(freq)):
        if freq[i] > clip_limit:
            clipper = clipper + freq[i] - clip_limit
            freq[i] = clip_limit

    if clipper <= 256:
        for j in range(0, len(freq), round(np.divide(256, clipper))):
            freq[j] += 1
    else:
        for j in range(len(freq)):
            freq[j] += round(np.divide(clipper, 256))
    freq = np.divide(freq, np.sum(freq))

    cdf = np.multiply(255, (np.cumsum(freq)))

    for i in range(len(img_lin)):
        img_lin[i] = cdf[img_lin[i]]
    img_adapt_hist_eq = np.reshape(img_lin, (width, length))

    return img_adapt_hist_eq


def adapt_hist_equal(img):

    width, length, _ = img.shape
    img_copy = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY)

    split_img = []
    for i in range(8):
        for j in range(8):
            split_img.append(img_copy[round(i*(width/8)):round((i+1)*(width/8)), round(j*(length/8)):round((j+1)*(length/8))])
    split_img = np.asarray(split_img, dtype=object)

    adapt_img = []
    for k in range(len(split_img)):
        adapt_img.append(contrast_clipping(split_img[k]))
    adapt_img = np.asarray(adapt_img, dtype=object)
    adapt_img = np.reshape(adapt_img, (8, 8))

    imgfinal = np.hstack((adapt_img[0, 0], adapt_img[0, 1], adapt_img[0, 2], adapt_img[0, 3], adapt_img[0, 4], adapt_img[0, 5], adapt_img[0, 6], adapt_img[0, 7]))
    for i in range(1, 8):
        imgfinal = np.vstack((imgfinal, (np.hstack((adapt_img[i, 0], adapt_img[i, 1], adapt_img[i, 2], adapt_img[i, 3], adapt_img[i, 4], adapt_img[i, 5], adapt_img[i, 6], adapt_img[i, 7])))))

    return imgfinal