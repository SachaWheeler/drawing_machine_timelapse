import cv2


# https://stackoverflow.com/questions/21892630/how-can-i-test-the-actual-resolution-of-my-camera-when-i-acquire-a-frame-using-o
cam = cv2.VideoCapture(0)
w = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(w, h)
while cam.isOpened():
    err, img = cam.read()
    cv2.imshow("lalala", img)
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break
