import argparse
import cv2
import os
from PIL import Image
import json
import glob
import sys
import getopt

#arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--imagefile", required=False,
                help="Image file path. Example <-i something.jpg")
ap.add_argument("-p", "--pixels", required=True,
                help="pixels to skip, every nth pixel will be analyzed. Example <-p 5>")

ap.add_argument("-f", "--frames", required=False,
                help="Number of frames to use from video. Example <-f 50>")
ap.add_argument("-v", "--videofile", required=False,
                help="Videofile path>")

args = vars(ap.parse_args())

pixels = int(args["pixels"])

#split videos into frames then rgb into json
def video_pixel_converter():

    frames = int(args["frames"])
    vidcap = cv2.VideoCapture(args["videofile"])
    success, image = vidcap.read()
    count = 0
    try:
        if not os.path.exists('data'):
            os.makedirs('data')
    except OSError:
        print('Error: Creating directory of data')

    while success:
        if count <= frames:
            success, image = vidcap.read()

            # Saves image of the current frame in jpg file
            name = './data/' + str(count) + '.jpg'
            print('Creating...' + name)
            cv2.imwrite(name, image)
            count += 1
        else:
            break

    listoffiles = os.listdir("data")

    listoffiles = len(listoffiles)
    list_of_files = glob.glob('data/*')
    latest_file = max(list_of_files, key=os.path.getctime)
    os.remove(latest_file)

    counter = 0
    dictionary1 = {}
    dictionaryJSON = {}
    arrayJson = []
    while counter < frames:

        diction = {}
        

        image = Image.open("data/" + "%d.jpg" % counter)

        width, height = image.size

        for y in range(0, height, pixels):
            for x in range(0, width, pixels):
                strY = str(y) + ','
                strX = str(x)
                strxy = strY + strX

                rgb = str(image.getpixel((x, y))).replace("(", "")
                rgb = rgb.replace(")", "")
                diction[strxy] = rgb

        dictionary1[counter] = diction

        print("image {} Done".format(counter))
        counter += 1
    arrayJson.append(dictionary1)
    dictionaryJSON["frames"] = arrayJson

    with open('jsonData.json', 'w') as outfile:
        json.dump(dictionaryJSON, outfile, sort_keys=True,
                  indent=4, ensure_ascii=False)

    print("finished")

#take single images rgb data convert to json 
def image_converter():
    diction = {}
    dictionary1 = {}
    dictionaryJSON = {}
    arrayJson = []

    image = Image.open(args["imagefile"])
    width, height = image.size
  

    for y in range(0, height, pixels):
            for x in range(0, width, pixels):
                strY = str(y) + ','
                strX = str(x)
                strxy = strY + strX

                rgb = str(image.getpixel((x, y))).replace("(", "")
                rgb = rgb.replace(")", "")
                diction[strxy] = rgb

    dictionary1[0] = diction

    print("image Done")
    arrayJson.append(dictionary1)
    dictionaryJSON["frames"] = arrayJson

    with open('jsonData.json', 'w') as outfile:
        json.dump(dictionaryJSON, outfile, sort_keys=True,
                  indent=4, ensure_ascii=False)

    print("finished")


if args["videofile"]:
    video_pixel_converter()

if args["imagefile"]:
    image_converter()
