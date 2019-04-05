# Vid-to-Json

##Video and image converter - Reads frames pixel position and color then creates json file with this data. 

###Usage-

  vid2json.py -i imagefile -p 10
  The flag -i is the path to an image file. The flag -p 10 says every 10th pixel analyze the rgb data of this pixel.
  
  vid2json.py -v videofile -p10 -f 49 
  The flag -v is the path to a video file. The flag -p is the pixel skip count. The flag -f is the number of video frames
  you want to cut from the video and process.

![bottle](https://user-images.githubusercontent.com/43976537/55659548-32e20c80-57d0-11e9-86e2-255bea0f3abb.png)
