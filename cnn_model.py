import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from tensorflow import keras

(X_train, y_train), (X_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()

class_labels = ["T-shirt", "Trouser", "Pullover", "Dress", "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle Boot"]

X_train.shape, y_train.shape

X_test.shape, y_test.shape

# Display the first image and its label
X_train[0]

y_train[0]


# First, we expand the dimensions of the training data 'X_train' and testing data 'X_test' by adding an extra dimension at the end.
X_train = np.expand_dims(X_train, -1)
X_test = np.expand_dims(X_test, -1)

# Next, we are performing data normalization. We divide all pixel values by 255 to scale them between 0 and 1.
X_train = X_train / 255
X_test = X_test / 255


#Build the cnn model 

