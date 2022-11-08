import os
import numpy as np
import cv2
import time
import datetime


from utils import CFEVideoConf, image_resize
import glob


frames_per_seconds = 30

input_directory = 'images/'
output_directory = 'saved-media/'

def images_to_video(image_dir):
    video_file = os.path.join(output_directory, image_dir + ".mp4")
    print(f"{image_dir} -> {video_file}")
    # return
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
    # print(image_list)
    # sorted_images = sorted(image_list, key=os.path.getmtime
    sorted_images = sorted(image_list)
    # print(sorted_images)
    for file in sorted_images:
        # print(file)
        image_frame  = cv2.imread(file)
        out.write(image_frame)
    # When everything done, release the capture
    # cap.release()
    out.release()
    # cv2.destroyAllWindows()


# iterate over files in
# that directory
for image_dir in os.listdir(input_directory):
    if os.path.isfile(os.path.join(output_directory, image_dir + ".mp4")):
        print("video file exists ")
        continue
    images_to_video(image_dir)

os.system('say -v Victoria video completed!')
