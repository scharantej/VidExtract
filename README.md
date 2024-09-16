## Problem Analysis

The app we are designing aims to extract image frames from a submitted video. The user will have the ability to submit a video file, and our app will process it to extract the individual frames and make them available in a suitable format.

## Flask Application Design

### HTML Files

**1. home.html:**

- This file will be the landing page of our application.
- It will contain a form for the user to submit a video file.

**2. success.html:**

- This file will be displayed after the video has been processed successfully.
- It will include a list of links to the extracted image frames.

### Routes

**1. / (GET):**

- This route will render the home.html file.

**2. /upload-video (POST):**

- This route will handle the file upload.
- It will extract the frames from the uploaded video and save them in a specified directory.
- After processing, it will redirect to /success.html with links to the extracted frames.

### Code Structure

```python
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
```

### Explanation

- The code starts by importing necessary dependencies and creating a Flask application instance.
- The `/` route handles the rendering of the home page where users can submit a video.
- The `/upload-video` route handles the video upload and frame extraction.
- The `/success` route displays a list of links to the extracted frames.