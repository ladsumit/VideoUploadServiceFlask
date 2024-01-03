from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])

def upload():
    # Handle video upload logic here
    video_file = request.files['video']
    # Process and save the video file
    return 'Video uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)