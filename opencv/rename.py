import os
path = 'images/timelapse/'
for filename in os.listdir(path):
    num, suffic = filename.split('.')
    num = num.zfill(4)
    new_filename = num + ".jpg"
    # print(filename, new_filename)
    os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
