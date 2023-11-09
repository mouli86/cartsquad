import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
import pickle

# Fashion MNIST dataset
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()

# Define class labels
class_labels = ["T-shirt", "Trouser", "Pullover", "Dress", "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle Boot"]

# Calculate mean and standard deviation from the training data
mean = np.mean(X_train)
std = np.std(X_train)

# Standardize the data
X_train = (X_train - mean) / std
X_test = (X_test - mean) / std

# Split the data into training and validation sets
X_train, X_validation, y_train, y_validation = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

# CNN model
cnn_model = keras.models.Sequential([
    keras.layers.Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)),
    keras.layers.MaxPooling2D(pool_size=(2, 2)),
    keras.layers.Conv2D(64, kernel_size=(3, 3), activation='relu'),
    keras.layers.MaxPooling2D(pool_size=(2, 2)),
    keras.layers.Conv2D(128, kernel_size=(3, 3), activation='relu'),
    keras.layers.MaxPooling2D(pool_size=(2, 2)),
    keras.layers.Conv2D(256, kernel_size=(3, 3), activation='relu'),
    keras.layers.MaxPooling2D(pool_size=(2, 2)),
    keras.layers.Conv2D(512, kernel_size=(3, 3), activation='relu'),
    keras.layers.MaxPooling2D(pool_size=(2, 2)),
    keras.layers.Flatten(),
    keras.layers.Dense(1024, activation='relu'),
    keras.layers.Dropout(0.4),
    keras.layers.Dense(512, activation='relu'),
    keras.layers.Dropout(0.4),
    keras.layers.Dense(256, activation='relu'),
    keras.layers.Dropout(0.4),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dense(16, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

# Compile the model
cnn_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model with more epochs and a larger batch size
cnn_model.fit(X_train, y_train, epochs=25, batch_size=256, validation_data=(X_validation, y_validation))

# Evaluate the model
test_loss, test_accuracy = cnn_model.evaluate(X_test, y_test)
print("Test Accuracy:", test_accuracy)

# Function to return the predicted label
def make_prediction_and_return_label(test_image):
    # Make a prediction
    y_pred = cnn_model.predict(np.expand_dims(test_image, axis=0)).round(2)
    predicted_label = class_labels[np.argmax(y_pred[0)]
    return predicted_label

# Save the model
with open("fashion_mnist_model.pkl", "wb") as model_file:
    pickle.dump(cnn_model, model_file)

# Load the model using pickle
with open("fashion_mnist_model.pkl", "rb") as model_file:
    loaded_model = pickle.load(model_file)
