import os
import numpy as np
import cv2
import time
import datetime


from utils import CFEVideoConf, image_resize
import glob


frames_per_seconds = 30

input_directory = 'images/'
output_directory = 'video/'

def images_to_video(image_dir):
    video_file = os.path.join(output_directory, image_dir + ".mp4")
    print(f"{image_dir} -> {video_file}")
    # cap = cv2.VideoCapture(0)
    # config = CFEVideoConf(cap, filepath=image_dir, res='1080p')
    # print(f"video type: {config.video_type}")
    # print(f"dims      : {config.dims}")
    # video type: 1145656920
    # dims      : (1920, 1080)
    video_type = 1145656920
    dims =  (1920, 1080)
    out = cv2.VideoWriter(video_file, video_type, frames_per_seconds, dims)

    print(f"converting {image_dir}")
    image_list = glob.glob(f"images/{image_dir}/*.jpg")
    sorted_images = sorted(image_list)
    for file in sorted_images:
        # print(file)
        image_frame  = cv2.imread(file)
        out.write(image_frame)

    out.release()


# iterate over files in the directory
for image_dir in os.listdir(input_directory):
    if image_dir == '.DS_Store':
        continue
    if os.path.isfile(os.path.join(output_directory, image_dir + ".mp4")):
        print(f'{image_dir + ".mp4"} exists ')
        continue
    images_to_video(image_dir)

os.system('say -v Victoria video completed!')
