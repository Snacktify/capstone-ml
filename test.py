import cv2
import json
import requests
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

img = cv2.imread("test.jpg")
img = cv2.resize(img, (150, 150))
img = img / 255.0
img = (np.expand_dims(img, 0))
json_data = json.dumps(
    {
        "instances": img.tolist()
    }
)
endpoint = "http://localhost:8080/v1/models/snackscan:predict"

response = requests.post(endpoint, data=json_data)
print(response)
prediction = tf.argmax(response.json()["predictions"]).numpy()
print(prediction)