import os
import cv2
import datetime
import serial
import glob
import serial.tools.list_ports
import pprint
from utils import IMAGE_WIDTH, IMAGE_HEIGHT


ports = list(serial.tools.list_ports.comports())
for p in ports:
    pprint.pprint(p[0])
    if "/dev/ttyACM0" not in p[0]:
        continue
    try:
        arduino_trigger = serial.Serial(
            port=p[0],
            baudrate=115200,
            timeout=None,
            bytesize=8)
        print(p[0])
        print(arduino_trigger)
    except Exception as e:
        pprint.pprint(e)
        print("Cannot connect to serial device")
        exit(0)
try:
    arduino_trigger
except:
    print("USB serial device not found")
    exit(0)

# https://stackoverflow.com/questions/40348656/editing-camera-settings-by-using-opencv
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, IMAGE_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, IMAGE_HEIGHT)
cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)      # turn off autofocuas
cap.set(cv2.CAP_PROP_FOCUS , 10)        # set the focus manually
cap.set(cv2.CAP_PROP_BRIGHTNESS, 105)   # set the brightness
cap.set(cv2.CAP_PROP_CONTRAST, 30)      # set the contrast

today = str(datetime.date.today())
hour = str(datetime.datetime.now().hour)
minute = str(datetime.datetime.now().minute)
time_str = today + "_" + hour + "-" + minute

timelapse_img_dir = f'images/timelapse_{time_str}/'

if not os.path.exists(timelapse_img_dir):
    os.mkdir(timelapse_img_dir)

i = 0
try:
    while True:
        data_2 = arduino_trigger.read()
        if len(data_2.strip()):  # we have a character
            ret, frame      = cap.read()
            filename        = f"{timelapse_img_dir}/{str(i).zfill(4)}.jpg"
            i               += 1
            cv2.imwrite(filename, frame)
except Exception as e:
    print(e)
    os.system('say -v Victoria video interrupted')


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

os.system('say -v Victoria time lapse completed!')
