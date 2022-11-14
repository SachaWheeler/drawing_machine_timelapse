import os
import numpy as np
import cv2
import time
import datetime
import serial
from utils import CFEVideoConf, image_resize
import glob
import serial.tools.list_ports


ports = list(serial.tools.list_ports.comports())
for p in ports:
    if "/dev/cu.usbmodem" not in p[0]:
        continue
    try:
        arduino = serial.Serial(
            port=p[0],
            baudrate=115200,
            timeout=1,
            bytesize=8)
            print(p[0])
            print(arduino)

cap = cv2.VideoCapture(0)

today = str(datetime.date.today())
hour = str(datetime.datetime.now().hour)
minute = str(datetime.datetime.now().minute)
time_str = today + "_" + hour + "-" + minute

frames_per_seconds = 30
save_path=f'video/timelapse_{time_str}.mp4'
config = CFEVideoConf(cap, filepath=save_path, res='1080p')
out = cv2.VideoWriter(save_path, config.video_type, frames_per_seconds, config.dims)
timelapse_img_dir = f'images/timelapse_{time_str}/'
# seconds_duration = 15400
# 9.06 for 60v
# 3.16  # for arm voltage 200
delay  = 0.9
seconds_between_shots = 3.03 #   - delay

if not os.path.exists(timelapse_img_dir):
    os.mkdir(timelapse_img_dir)

now = datetime.datetime.now()
# finish_time = now + datetime.timedelta(seconds=seconds_duration)
i = 0
while True:
    # start = time.time()
    data_2 = arduino.read()
    if len(data_2.strip()):  # we have a character
        ret, frame      = cap.read()
        filename        = f"{timelapse_img_dir}/{str(i).zfill(4)}.jpg"
        i               += 1
        cv2.imwrite(filename, frame)


# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()

os.system('say -v Victoria time lapse completed!')
