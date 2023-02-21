from flask import Flask, request, send_file
from flask_cors import CORS
import jsonpickle

from ImageTransform import trataImagem

app = Flask(__name__)
CORS(app)

url = None

@app.route('/images', methods=['POST', 'GET'])
async def image():
    if request.method == 'POST':
        global url
        url = request.json['input_value']
        trataImagem(url)
    
    return send_file('images/image.jpg', mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug = True)