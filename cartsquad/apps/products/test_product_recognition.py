import unittest
import numpy as np
import matplotlib.pyplot as plt
from product_recognition import make_prediction_and_return_label


class TestProductRecognition(unittest.TestCase):
    def test_prediction_and_plot_sample1(self):
        # Create a test image and label
        test_image = X_test[0]
        actual_label = y_test[0]
        
        # Capture the print output
        with self.assertLogs() as cm:
            make_prediction_and_plot(test_image, actual_label)
        
        # Assert the printed output contains the expected labels
        expected_output = f'Actual = {class_labels[actual_label]} / Predicted = {class_labels[actual_label]}'
        self.assertIn(expected_output, cm.output)

    def test_prediction_and_plot_sample2(self):
        # Create a test image and label
        test_image = X_test[1]
        actual_label = y_test[1]

        # Capture the print output
        with self.assertLogs() as cm:
            make_prediction_and_plot(test_image, actual_label)
        
        # Assert the printed output contains the expected labels
        expected_output = f'Actual = {class_labels[actual_label]} / Predicted = {class_labels[actual_label]}'
        self.assertIn(expected_output, cm.output)

if __name__ == '__main__':
    unittest.main()
