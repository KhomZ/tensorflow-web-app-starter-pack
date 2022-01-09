# ikhomkodes
import numpy as np
from numpy.lib.type_check import imag
from PIL import Image
from io import BytesIO
import tensorflow as tf
from tensorflow.keras.applications import imagenet_utils
from tensorflow.keras.applications.imagenet_utils import decode_predictions

# input_shape = (224, 224)
input_shape = (224, 224, 3)


def load_model():
    model = tf.keras.applications.MobileNetV2(input_shape)
    return model


_model = load_model()


def read_image(image_encoded):
    pil_image = Image.open(BytesIO(image_encoded))
    return pil_image


def preprocess(image: Image.Image):
    image = image.resize(input_shape)
    image = np.asfarray(image)
    image = image / 127.5 - 1.0  # for normalization
    image = np.expand_dims(image, 0)

    return image


def predict(image: np.ndarray):
    predictions = _model.predict(image)
    predictions = imagenet_utils.decode_predictions(predictions)[0][0][1]
    return predictions
