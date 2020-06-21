import os
import requests as re
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from requests_toolbelt.multipart.encoder import MultipartEncoder

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'obj', 'mtl', 'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files.getlist("file")
        print(file)

        # if user does not select file, browser also
        # submit an empty part without filename
        if len(file) == 0 or file[0].filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file[0] and allowed_file(file[0].filename):
            if len(file) < 2:
                return 'You forget either mtl or obj file'
            fs = []
            for f in file:
                path = os.getcwd() + '/' + f.filename
                f.save(os.path.join(os.getcwd() + '/', f.filename))
                fs.append(path)
            mp_encoder = MultipartEncoder(
                fields={
                    'key': 'small-wood-6393', 'target_type': '2', 'hologram_type': '2',
                    'file_model': (file[1].filename, file[1], file[0]),
                }
            )

            url = 'https://console.echoAR.xyz/upload'
            r = re.post(
                url,
                data=mp_encoder,  # The MultipartEncoder is posted as data, don't use files=...!
                # The MultipartEncoder provides the content-type header with the boundary:
                headers={'Content-Type': mp_encoder.content_type}
            )
            #print(r.text)
            print(mp_encoder.content_type)
            return r.text
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file multiple>
      <input type=submit value=Upload>
    </form>
    '''