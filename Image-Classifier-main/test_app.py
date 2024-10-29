

class TestApp:

    def preprocess_image(self, img_path):
        import cv2 as cv
        img = cv.imread(img_path)
        img = cv.resize(img, (32, 32))
        img = img / 255.0
        img = img[None, :]  
        return img

    def test_one_CIFAR10Names_pass(self):
        class_names = ['plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

        class_check = ['plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

        assert class_check == class_names

    def test_two_CIFAR10Names_fail(self):
        class_names = ['plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

        class_check = ['x','y','x']

        assert class_check != class_names

    def test_three_imageIO_pass(self):
        img_path = 'uploads/uploaded_image.png' 
        img = self.preprocess_image(img_path)
        assert img.shape == (1, 32, 32, 3)  

    def test_imports_pass(self):
        try:
            import numpy as np
            import cv2 as cv
            from tensorflow.keras.models import load_model
            from flask import Flask, render_template, request, send_from_directory
        except ImportError as e:
            pytest.fail(f"Import failed: {e}")

        # Check if the imported modules are accessible
        assert np is not None
        assert cv is not None
        assert load_model is not None
        assert Flask is not None
        assert render_template is not None
        assert request is not None
        assert send_from_directory is not None