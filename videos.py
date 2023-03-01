import json
import os
import glob
from pathlib import Path
from time import sleep
from os import walk
media = "/home/pi/vlc-http-controller-vrquin/videos/"
while(True):
    count_1 = 0
    s_n = 3
    videos =[]
    os.system("sudo chmod 777 /home/pi/vlc-http-controller-vrquin/library.json")
    list_of_files = sorted( filter( os.path.isfile,glob.glob(media + '*') ) )
    for file_name in list_of_files:
        if file_name.endswith(".mp4"):
            file_p = media + file_name
            video_n = Path(file_name).stem
            file_n = video_n + ".mp4"
            img_p = "/thumbnails/" + video_n + ".jpg"
            print(file_p)
            print(file_n)
            print(video_n)
            print(img_p)
            count_1 += 1
            s_n += 1
            folder = {
                "id": count_1,
                "title": video_n,
                "video_n": file_n,
                "p_list" : s_n,
                "img_p":img_p,
                "src": file_name,
            }
            videos.append(folder)
    dictionary = {
        "media": videos
    }
    json_object = json.dumps(dictionary, indent=4)
    with open("/home/pi/vlc-http-controller-vrquin/library.json", "w") as outfile:
        outfile.write(json_object)
    os.system("sudo chmod 644 /home/pi/vlc-http-controller-vrquin/library.json")
    i = 1
    while(i):
        count_2 = 0
        for file_name in os.listdir(media):
            if file_name.endswith(".mp4"):
                count_2 += 1
        if (count_1 == count_2):
            print("deba")
            sleep(1)
        else:
            i = 0
