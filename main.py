from flask import Flask, render_template, request, flash
from werkzeug.utils import secure_filename
import os
import cv2
import numpy as np

UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg', 'gif', 'webp'}

app = Flask(__name__)
app.secret_key ='super secrate key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("photoediting.html")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def processImage(filename, operation):
    print (f" the operation is {operation} and filename is {filename}") 
    img = cv2.imread("./Images/photo1.jpeg")
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (21, 21), 0, 0)
    match operation:
        case "cgray":
            imgProcessed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
            newFile = f"static/{filename}"
            cv2.imwrite(newFile, imgProcessed)
            return filename
        case "cwebp":
            newFile = f"static/{filename.split('.')[0]}.webp"
            cv2.imwrite(newFile, img)
            return newFile
        case "cjpg":
            newFile = f"static/{filename.split('.')[0]}.jpg"
            cv2.imwrite(newFile, img)
            return newFile
        case "cpng":
            newFile = f"static/{filename.split('.')[0]}.png"
            cv2.imwrite(newFile, img)
            return newFile
        case "cblur":
            newFile = f"static/{filename.split('.')[0]}.png"
            img_blurr = cv2.GaussianBlur(img, (21, 21), 0, 0)
            cv2.imwrite(newFile, img_blurr)
            return newFile
        case "csketch":
            newFile = f"static/{filename.split('.')[0]}.png"
            img_blend = cv2.divide(img_gray, img_blur, scale=256)
            cv2.imwrite(newFile, img_blend)
            return newFile
        case "cWboreder":
            newFile = f"static/{filename.split('.')[0]}.png"
            edges_image = cv2.Canny(img, 100, 200)
            cv2.imwrite(newFile, edges_image)
            return newFile
        case "cedge":
            newFile = f"static/{filename.split('.')[0]}.png"
            grey = cv2.medianBlur(img_gray, 5)
            edges= cv2.adaptiveThreshold (grey, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 9, 2)
            cv2.imwrite(newFile, edges)
            return newFile
        case "cCedge":
            newFile = f"static/{filename.split('.')[0]}.png"
            colors = cv2.bilateralFilter(img, 9, 250, 250)
            color_edge = cv2.bitwise_and (colors, colors, mask = edges)
            cv2.imwrite(newFile, color_edge)
            return newFile
        case "csepia":
            newFile = f"static/{filename.split('.')[0]}.png"
            sepia_filter = np.array([[0.393, 0.769, 0.189],
                             [0.349, 0.686, 0.168],
                             [0.272, 0.534, 0.131]])

            sepia_image = cv2.transform(img, sepia_filter)
            cv2.imwrite(newFile, sepia_image)
            return newFile
        case "cembossedImage":
            newFile = f"static/{filename.split('.')[0]}.png"
            emboss_kernel = np.array([[-2, -1, 0],
                            [-1,  1, 1],
                            [ 0,  1, 2]])
            embossed_image = cv2.filter2D(img, -1, emboss_kernel)
            cv2.imwrite(newFile, embossed_image)
            return newFile
        case "cinfraredImage":
            newFile = f"static/{filename.split('.')[0]}.png"
            infrared_image = cv2.applyColorMap(img_gray, cv2.COLORMAP_HOT)
            cv2.imwrite(newFile, infrared_image)
            return newFile
    pass

@app.route("/edit", methods=['POST', "GET"])
def edit():
  if request.method == 'POST':
        operation = request.form.get('operation')
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return "error"
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return "error no file is there"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            newImg = processImage(filename, operation)
            flash(f"Your image has been processed and is available <a href='/{newImg}' target='_blank'>here</a>")
            return render_template("photoediting.html")
    # return render_template("photoediting.html")

app.run(debug=True, port=5001)