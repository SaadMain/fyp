import numpy as np
import tensorflow as tf
import cv2
import os
from tensorflow.keras.models import load_model
def video_capture(vid_path):
    vid_capture = cv2.VideoCapture(vid_path) 
    if (vid_capture.isOpened() == False):
      print("Error opening the video file")
      try:
            os.remove(vid_path)
      except:
            pass
      return None
    else:
      d=0
      counter=0
      cat_images=[]
    while(vid_capture.isOpened()):
      ret, frame = vid_capture.read()
      if ret == True:
          d=d+1
          if d <16:
            continue
          else:
            counter=counter+1
            d=0
            frame_grey=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            frame_grey=cv2.resize(frame_grey, (320,240), interpolation = cv2.INTER_AREA)
            #print('Resized Dimensions : ',frame_grey.shape)
            datu=np.array(frame_grey)
            normu_dat=datu/255
            cat_images.append(normu_dat)
            if counter==60:
              break
      else:
        if counter<60:
          while counter<60:
            cat_images.append(normu_dat)
            counter=counter+1
          #print(len(cat_images))
        break
    vid_capture.release()
    cv2.destroyAllWindows()
    return cat_images


def check(images):
    new_model = tf.keras.models.load_model('3dcnn_weight.h5',compile = True)
   # new_model.summary()
    test_img=np.expand_dims(images, axis=0)
    x=new_model.predict(test_img)
    b=np.argmax(x)
    return b

