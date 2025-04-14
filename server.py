from flask import Flask, request, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/upscale', methods=['POST'])
def upscale():
    file = request.files['file']
    # Simulate upscaling: just return the same file as a placeholder
    return send_file(file, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
