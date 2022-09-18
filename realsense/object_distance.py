import cv2
import pyrealsense2
from realsense_depth import *

# Initializations
dc = DepthCamera()
point = (400, 300)

# Sets object position based on mouse event
def set_object_position(event, x, y, args, param):
    global point # updates object position
    point = (x, y)

# Associate mouse event to Color window, i.e. the object the mouse is pointing to
# However, need to check if ubuntu detects usb mouse event
cv2.namedWindow("Color frame")
cv2.setMouseCallback("Color frame", set_object_position)

while True:
    ret, depth_frame, color_frame = dc.get_frame()

    # Make the point more visible with red circle, show distance in black color at a specific point slightly up
    cv2.circle(color_frame, point, 4, (0, 0,  255))
    distance = depth_frame[point[1], point[0]] # known quirk of using y,x instead of x,y
    cv2.putText(color_frame, "{}mm".format(distance), (point[0], point[1] - 20), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,0), 2)

    cv2.imshow("Depth frame", depth_frame)
    cv2.imshow("Color frame", color_frame)
    
    # Exit loop if ESC key pressed
    key = cv2.waitKey(1)
    if key == 27:
        break
