import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
import tensorflow as tf
from PIL import Image


class AIUtil:

    @staticmethod
    def invert_coordinates(coordinates, image_size):
        inverted_polygon_coordinates = [(x, image_size[1] - y) for x, y in coordinates]
        return inverted_polygon_coordinates

    @staticmethod
    def load_image_tensors(image_paths, image_size):
        image_tensors = [AIUtil.load_image_tensor(image_path, image_size) for image_path in image_paths]
        return image_tensors

    @staticmethod
    def load_image_tensor(path, image_size):
        image = Image.open(path)
        image = image.resize(image_size)
        image_tensor = tf.convert_to_tensor(np.array(image))
        # image_tensor = tf.expand_dims(image_array, 0)
        return image_tensor

    @staticmethod
    def flatten_coordinates(coordinates):
        """ Inverts and flattens coordinates
        """
        coordinates = np.array(sum(coordinates, ()))
        return coordinates

    @staticmethod
    def create_cnn_model(input_shape):
        model = Sequential()
        model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=input_shape))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Flatten())
        model.add(Dense(16, activation='relu'))
        model.add(Dense(8, activation='sigmoid'))
        return model