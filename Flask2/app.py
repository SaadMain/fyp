import os
import tensorflow
import numpy as np
from flask import Flask, render_template, request, jsonify
import prediction
import werkzeug
result =	{
  0: "Explosion",
  1: "Fighting",
  2:  "Burgulary",
}

app=Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def main():
	return "Hello"

@app.route('/upload', methods=['GET',"POST"])
def upload():
    if request.method == "POST" :
        imagefile = request.files['video']
        filename = werkzeug.utils.secure_filename(imagefile.filename)
        # print("\nReceived image File name : " + imagefile.filename)
        vid_path =filename
        val={}	
        imagefile.save(vid_path)
        imges=prediction.video_capture(filename)
        img=np.asarray(imges)
        ret=prediction.check(img)	
        val['output']=result[ret]
        try:
            os.remove(vid_path)
        except:
            pass
        print(val['output'])        
        return jsonify({
            "message": val['output'],
        })

if __name__ == "__main__":
    app.run(debug=True)
