import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

# Local development serving of media files if they are in the root
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
