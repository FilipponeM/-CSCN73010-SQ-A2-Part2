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
    img = cv.imread(img_path)
    img = cv.resize(img, (32, 32))
    img = img / 255.0
    img = img[None, :]  # Add batch dimension
    return img

@app.route('/', methods=['GET', 'POST'])
def index():
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
            image_path = f'/uploads/uploaded_image.png'

            return render_template('index.html', result=result, image_path=img_path)

    return render_template('index.html', result=None, image_path=None)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('uploads', filename)   

if __name__ == '__main__':
    app.run(debug=True)
