# A simple Computer Vision starter

This is a starter project using OpenCV and Intel RealSense camera.  
This is largely inspired by 
https://pysource.com/2021/03/11/distance-detection-with-depth-camera-intel-realsense-d435i/


## Pre-requisites

Using pip3 and python3:
```sh
pip3 install --upgrade pip
pip3 install opencv-python
pip3 install pyrealsense2
```

## Some RealSense Tech Specs

### Stereo Vision Depth Technology Overview
The Intel® RealSense™ D400 series depth camera uses stereo vision to calculate depth. The stereo vision implementation consists of a left imager, right imager, and an optional infrared projector. The infrared projector projects a non-visible static IR pattern to improve depth accuracy in scenes with **low texture**. Example of low or poor texture objects are plain blank walls, books pages, or flat objects containing equal symmetric patterns.  

The left and right imagers capture the scene and send imager data to the depth imaging (vision) processor, which calculates depth values for each pixel in the image by correlating points on the left image to the right image and via the shift between a point on the Left image and the Right image. The depth pixel values are processed to generate a depth frame. Subsequent depth frames create a depth video stream

### Accuracy
Range up to 10m.  
<2% error at 2m.  

References:  
[Depth range](https://www.intelrealsense.com/depth-camera-d435/  #:~:text=A%20Powerful%2C%20Full%E2%80%91featured%20Depth%20Camera&text=With%20a%20range%20up%20to,2.0%20and%20cross%2Dplatform%20support).  
[Tuning](https://dev.intelrealsense.com/docs/tuning-depth-cameras-for-best-performance)  
[RealSense Sample Codes](https://github.com/IntelRealSense/librealsense)  