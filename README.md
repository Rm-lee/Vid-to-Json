# Vid-to-Json

## Video and image converter - Reads frames pixel position and color then creates json file with this data. 

### Usage-

  vid2json.py -i imagefile -p 10  
  The flag -i is the path to an image file. The flag -p 10 says every 10th pixel analyze the rgb data of this pixel.  
  
  vid2json.py -v videofile -p 10 -f 49   
  The flag -v is the path to a video file. The flag -p is the pixel skip count. The flag -f is the number of video  
  frames you want to cut from the video and process.










This command will take this image and create a json file with every 10th pixels information.    
#### vid2json.py -i image.png -p 10  

<p align="center"><img  src="https://user-images.githubusercontent.com/43976537/55663479-62067700-57ec-11e9-9aa2-1152dfabec31.png" width="48%"></p>

 
Example img below is using JS to set a text object at every 10th pixel using the same color of the original pixel.  

<p align="center"><img src="https://user-images.githubusercontent.com/43976537/55659988-147d1080-57d2-11e9-9409-1a8edd5c7813.png" width="70%"></p>


  
