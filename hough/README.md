# A simple Hough Transform starter

This is a starter project using OpenCV Hough Transform to detect lines.  

![original image](./doc/image.jpg) 

![canny to edges to hough to lines](./doc/edges_lines.png) 

This is largely inspired by a video from  
https://www.youtube.com/watch?v=KEYzUP7-kkU

## Pre-requisites

Using pip3 and python3:
```sh
pip3 install --upgrade pip
pip3 install opencv-python
```

## OpenCV

You can get each frame from the video mp4 file in a loop.  
This starter just demonstrate 1 frame from image.jpg.  

Typically, you would covert RGB image to gray image.  
Use Canny function to get the edges from the gray image.  
With the edges, use HoughLinesP function to get the lines.  
```python
img = cv2.imread("video/image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 75, 150)

# get array of lines from HoughLinesP
# uses maxLineGap to close the line gaps
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=5)
```

