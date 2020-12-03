
from flask import Flask
from flask import jsonify
from flask import request
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array
#from tensorflow import convert_to_tensor
import os
from tensorflow.keras.models import *
import base64
import io
from PIL import Image
print("Importing libraries...")


app = Flask(__name__)
""" app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/predict": {"origins": "http://localhost:port"}})
app.config['CORS_HEADERS'] = 'Content-Type' """


print("Loading model...")
model = load_model('model_adv.h5')

""" print("Scanning image...")
img = image.load_img("./CovidDataset/Downloaded Images/google_pic_104_n.jpg", target_size=(224,224))
img = image.img_to_array(img)
img = np.expand_dims(img, axis=0)

print("Predicting result...")
p = model.predict_classes(img) """


def process(image, target_size):
    if image.mode != "RGB":
        image = image.convert("RGB")
    image = image.resize(target_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    return image

# @cross_origin(origin='localhost',headers=['Content- Type','Authorization'])


@app.route("/predict", methods=["POST"])
def predict():
    message = request.get_json(force=True)
    encoded = message['image']
    decoded = base64.b64decode(encoded)
    print("Scanning image...")
    imgpil = Image.open(io.BytesIO(decoded))
    img = process(imgpil, target_size=(224, 224))
    p = model.predict_classes(img)
    print("Predicting result...")
    if p[0, 0] == 1:
        result = "Covid -ve"
    else:
        result = "Covid +ve"
    print(result)
    response = jsonify({
        'prediction': {
            'covid': result
        }
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


""" print("||=========================||")
if p[0,0] == 0 :
    print("|| COVID +VE")
else:
    print("|| COVID -VE")
print("||=========================||") """


@app.route('/sample')
def running():
    return 'Flask is running!'

# set FLASK_APP=name
# flask run
