# VideoProcessing

In this example we will be reading the video and predicting the shape and the color of the objects in the video


## What is a video?
- Video is the collection of frames (collection of images) which run at a certain rate `(frame per sec)`
- It is important to split video into array of frames


## Necessary libraries 
1. Python 2 or 3 Here I have use python 3
2. Numpy
3. Pandas
4. Open cv - Library for image processing. The version of the library has to be compatible with python version. Make sure you go through the documentation before you install.


## Steps to impliment
- Read the video and split into frames
- Processing the frame
      - Intentfying closed contours (In this case geometric shapes)
      - Identify the shape of contours
      - Identify the color of the geometric figure
      
- Repeat the processing for all the frames
- Save the collection of the frames as a video output


## Input and output video files are also present in this repository. You can try exploring this by cloning this repository to your local machine.


<b>Note:</b> Only three colors `Red`, `Green`, `Blue` have been classified in this exersize.  
