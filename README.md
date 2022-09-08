# Adaptive Histogram Equalization

## Description

[Adaptive Histogram Equalization](https://towardsdatascience.com/histogram-equalization-5d1013626e64) is a contrast enhancing technique in Image Processing. Adaptive Histogram Equalization considers the global contrast of the image, whereas [Contrast Limited Adaptive Histogram Equalization (CLAHE)](https://en.wikipedia.org/wiki/Adaptive_histogram_equalization#:~:text=Ordinary%20AHE%20tends,excess%20is%20negligible.) considers the local contrast which preventes unnecessary contrast enhancement. Both these techniques are implemented in this project without the use of inbuilt functions.


## Data

* Input set of frames

![alt text](/data/data.gif)


## Approach

### Adaptive Histogram Equalization

* Convert frame to Grayscale and create a Frequcny matrix of size 256 where the element at each index is the number of pixels with the value of that index.

* Find the Cumulative Sum of this matrix and divide by the total number of pixels in the frame to get the Cumulative Density Function (CDF) matrix.

* Multiply each element in the CDF by 255 and fill these values in the corresponding pixels to get the Adaptive Histogram Equalized Image.


### Contrast Limited Adaptive Histogram Equalization (CLAHE)

* The entire frame is divided into a grid of 8x8 and the following process is carried out for all the 64 parts of the frame.

* Similar to the previous case, a frequency matrix is created.

* A limit of 40 pixel is set and all the pixels which have a intensity frequency greater than 40 are set to 40. 

* The total number of excess pixels for all intensities is saved and equally divided between all the intensities.

* With this new Frequency matrix, further steps same as the previous section are followed.

* All the 64 parts of the image are combined to form the CLAHE output frame.


## Output

* Histogram of Original Frame

![alt text](/output/output1.png)

* Histogram of Adaptive Histogram Equalized Image

![alt text](/output/output2.png)

* Histogram of Contrast Limited Adaptive Histogram Equalized Image

![alt text](/output/output3.png)

* Final Output

![alt text](/output/final_output.gif)



## Getting Started

### Dependencies

<p align="left"> 
<a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/>&ensp; </a>
<a href="https://numpy.org/" target="_blank" rel="noreferrer"> <img src="https://www.codebykelvin.com/learning/python/data-science/numpy-series/cover-numpy.png" alt="numpy" width="40" height="40"/>&ensp; </a>
<a href="https://opencv.org/" target="_blank" rel="noreferrer"> <img src="https://avatars.githubusercontent.com/u/5009934?v=4&s=400" alt="opencv" width="40" height="40"/>&ensp; </a>

* [Python 3](https://www.python.org/)
* [NumPy](https://numpy.org/)
* [OpenCV](https://opencv.org/)


### Executing program

* Clone the repository into any folder of your choice.
```
git clone https://github.com/ninadharish/Adaptive-Histogram-Equalization-for-Image-Contrast-Enhancement.git
```

* Open the repository and navigate to the `src` folder.
```
cd Adaptive-Histogram-Equalization-for-Image-Contrast-Enhancement/src
```

* Run the program.
```
python main.py
```


## Authors

👤 **Ninad Harishchandrakar**

* [GitHub](https://github.com/ninadharish)
* [Email](mailto:ninad.harish@gmail.com)
* [LinkedIn](https://linkedin.com/in/ninadharish)