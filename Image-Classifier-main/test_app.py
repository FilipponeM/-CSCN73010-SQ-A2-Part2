import cv2 as cv

class TestApp:

    def preprocess_image(self, img_path):
        img = cv.imread(img_path)
        img = cv.resize(img, (32, 32))
        img = img / 255.0
        img = img[None, :]  # Add batch dimension
        return img

    def test_one_CIFAR10Names_pass(self):
        class_names = ['plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

        class_check = ['plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

        assert class_check == class_names

    def test_three_imageIO_pass(self):
        # Assuming you have a valid image file for testing
        img_path = 'uploads/uploaded_image.png'  # Replace with a valid image path
        img = self.preprocess_image(img_path)
        assert img.shape == (1, 32, 32, 3)  # Use assert to check shape


    #def test_five_pass(self):





        