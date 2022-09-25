import cv2
import numpy as np

# You can get each frame from the video mp4 file in a loop.
# Here, we just demonstrate 1 frame from image.jpg
img = cv2.imread("video/image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 75, 150)

# cv2.HoughLines() # HoughLines() uses high cpu by examining every points in images

# get array of lines from HoughLinesP
# uses maxLineGap to close the line gaps
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=5)
#print(lines) # have a look at the array of array of x1, y1, x2, y2 points

for line in lines:
    # first element of array in array
    x1, y1, x2, y2 = line [0]
    # draw line in green color
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2) 

cv2.imshow("Edges", edges)
cv2.imshow("Images", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1) # ubuntu needs this additional waitKey to continue
# See https://stackoverflow.com/questions/20539497/python-opencv-waitkey0-does-not-respond
