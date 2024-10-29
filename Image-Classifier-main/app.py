"""
app.py

The user will upload a photo into the webside and will use the learned data from modelcreation 
to assign the photo a "name" or "tag"

"""

from flask import Flask, render_template, request, send_from_directory
import numpy as np
import cv2 as cv
from tensorflow.keras.models import load_model

app = Flask(__name__)

# Load the model from the .keras file
model = load_model('image_classifier.keras')  # Use .keras model

# Class names for CIFAR-10
class_names = ['plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']


def preprocess_image(img_path):
    """
    preprocess_image function

    This function takes in a image throught the image path and 
    preprocess the image to be displayed
    
    Args:
        img_path

    Returns:
        img: resized image

    """
    img = cv.imread(img_path)
    img = cv.resize(img, (32, 32))
    img = img / 255.0
    img = img[None, :]  # Add batch dimension
    return img



@app.route('/', methods=['GET', 'POST'])

def index():
    """
    index 

    This function takes in the GET and POST REST requests fromt eh user
    and sends it through the preprocess image to be be displayed on the web page

    Returns:
        the Template for the image to be displayed in html

    """
    if request.method == 'POST':
        # Handle the uploaded image
        file = request.files['file']
        if file:
            # Save the uploaded image
            img_path = 'uploads/uploaded_image.png'
            file.save(img_path)

            # Preprocess the image
            img = preprocess_image(img_path)

            # Make a prediction
            prediction = model.predict(img)
            index = np.argmax(prediction)
            result = class_names[index]

            # Change image_path to be relative to static files
            image_path = '/uploads/uploaded_image.png'

            return render_template('index.html', result=result, image_path=img_path)

    return render_template('index.html', result=None, image_path=None)



@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """
    uploaded file

    Takes the image and places it into the uploads 
    then renames the image

    Returns:
        The new image into the uploads folder
    
    """
    return send_from_directory('uploads', filename)

if __name__ == '__main__':
    app.run(debug=True)
