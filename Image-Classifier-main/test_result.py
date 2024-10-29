
from tensorflow.keras import datasets

class TestApp:

    def test_one_CIFAR10Names_pass(self):
        class_names = ['plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

        class_check = ['plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

        assert class_check == class_names

    def test_two_CIFAR10Names_fail(self):
        class_names = ['plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

        class_check = ['x','y','x']

        assert class_check != class_names

    def test_cifar10_dataset(self):
        (training_images, training_labels), (testing_images, testing_labels) = datasets.cifar10.load_data()
        assert training_images.shape == (50000, 32, 32, 3)
        assert training_labels.shape == (50000, 1)
        assert testing_images.shape == (10000, 32, 32, 3)
        assert testing_labels.shape == (10000, 1)

