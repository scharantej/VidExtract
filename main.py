
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import cv2

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/upload-video', methods=['POST'])
def upload_video():
    video = request.files['video']
    filename = secure_filename(video.filename)
    
    # Extract frames here and save them to a directory

    return redirect(url_for('success'))

@app.route('/success')
def success():
    frames = os.listdir('./frames')
    return render_template('success.html', frames=frames)

if __name__ == '__main__':
    app.run(debug=True)
