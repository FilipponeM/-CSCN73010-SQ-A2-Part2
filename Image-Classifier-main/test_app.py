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

    def test_two_CIFAR10Names_fail(self):
        class_names = ['plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

        class_check = ['x','y','x']

        assert class_check != class_names

    def test_three_imageIO_pass(self):
        img_path = 'uploads/uploaded_image.png' 
        img = self.preprocess_image(img_path)
        assert img.shape == (1, 32, 32, 3)  

    def test_four_pass(self):
        