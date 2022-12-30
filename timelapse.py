import os
import cv2
import datetime
import serial
import glob
import serial.tools.list_ports
import pprint


ports = list(serial.tools.list_ports.comports())
for p in ports:
    pprint.pprint(p)
    pprint.pprint(p[0])
    pprint.pprint(p[1])
    pprint.pprint(p[2])
    if "/dev/ttyACM0" not in p[0]:
        continue
    try:
        arduino_trigger = serial.Serial(
            port=p[0],
            baudrate=115200,
            timeout=None,  # None?
            bytesize=8)
        print(p[0])
        print(arduino_trigger)
    except Exception as e:
        pprint.pprint(e)
        print("Cannot connect to modem device")
        exit(0)
try:
    arduino_trigger
except:
    print("USB modem device not found")
    exit(0)

cap = cv2.VideoCapture(0)

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
