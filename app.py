from flask import Flask, render_template, request

from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import preprocess_input
from tensorflow.keras.utils import img_to_array
from tensorflow.keras.utils import load_img
from keras.applications.vgg16 import VGG16
from IPython.display import display 
from PIL import Image





app = Flask(__name__)
model = VGG16() 

@app.route('/', methods=['GET'])
def Hello_Rash():
    return render_template('index.html') 

@app.route('/', methods=['POST'])
def predict():
    imagefile = request.files['imagefile']
    image_path = "./images/" + imagefile.filename
    imagefile.save(image_path)

    image = load_img(image_path, target_size=(224,224))
    image = img_to_array(image)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    yhat = model.predict(image)
    label = decode_predictions(yhat)
    label = label[0][0]

    classification = '%s (%.2f%%)' % (label[1], label[2]*100)


    return render_template('index.html', prediction = classification) 


if __name__== '__main__':
    app.run(port=3000, debug=True)