
import pytest

class TestApp:

    def test_one_CIFAR10Names_pass(self):
        class_names = ['plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

        class_check = ['plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

        assert class_check == class_names

    def test_two_CIFAR10Names_fail(self):
        class_names = ['plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

        class_check = ['x','y','x']

        assert class_check != class_names

    def test_imports_pass(self):
        try:
            import matplotlib.pyplot as plt
            from tensorflow.keras import datasets, layers, models
        except ImportError as e:
            pytest.fail(f"Import failed: {e}")

        # Check if the imported modules are accessible
        assert plt is not None
        assert datasets is not None
        assert layers is not None
        assert models is not None
