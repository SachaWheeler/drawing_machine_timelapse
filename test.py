import os
import cv2
import datetime
import serial
import glob
import serial.tools.list_ports
import pprint
from utils import IMAGE_WIDTH, IMAGE_HEIGHT


# print(cv2.CAP_PROP_AUTOFOCUS)

today = str(datetime.date.today())
hour = str(datetime.datetime.now().hour)
minute = str(datetime.datetime.now().minute)
time_str = today + "_" + hour + "-" + minute

timelapse_img_dir = f'images/timelapse_test_focus'

if not os.path.exists(timelapse_img_dir):
    os.mkdir(timelapse_img_dir)

i = 0
contrast = 5
while contrast <= 255:
    print(contrast)
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, IMAGE_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, IMAGE_HEIGHT)
    cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)
    cap.set(28, 10)  # focus
    cap.set(10, 105) # brightness
    cap.set(11, 30) # contrast
    ret, frame      = cap.read()
    filename        = f"{timelapse_img_dir}/{str(contrast).zfill(4)}.jpg"
    i               += 1
    cv2.imwrite(filename, frame)
    cap.release()
    contrast += 5


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

os.system('say -v Victoria time lapse completed!')
