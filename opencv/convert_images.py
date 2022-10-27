import os
import numpy as np
import cv2
import time
import datetime


from utils import CFEVideoConf, image_resize
import glob


cap = cv2.VideoCapture(0)

frames_per_seconds = 30
save_path='saved-media/timelapse_2022-10-27_10-34.mp4'
config = CFEVideoConf(cap, filepath=save_path, res='1080p')
out = cv2.VideoWriter(save_path, config.video_type, frames_per_seconds, config.dims)
timelapse_img_dir = 'images/timelapse_2022-10-27_10-34/'
seconds_duration = 5400
seconds_between_shots = 3.05  # 3.16  # for arm voltage 200

if not os.path.exists(timelapse_img_dir):
    os.mkdir(timelapse_img_dir)

def images_to_video(out, image_dir, clear_images=True):
    image_list = glob.glob(f"{image_dir}/*.jpg")
    # sorted_images = sorted(image_list, key=os.path.getmtime)
    sorted_images = sorted(image_list)
    for file in sorted_images:
        print(file)
        image_frame  = cv2.imread(file)
        out.write(image_frame)
    if clear_images:
        '''
        Remove stored timelapse images
        '''
        for file in image_list:
            pass
            # os.remove(file)

images_to_video(out, timelapse_img_dir)
# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()

os.system('say -v Victoria time lapse completed!')
