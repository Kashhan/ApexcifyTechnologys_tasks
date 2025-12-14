import tensorflow as tf
import numpy as np
from PIL import Image
import os

# Load model
model = tf.keras.models.load_model("keras_model.h5")

# Load labels
with open("labels.txt", "r") as f:
    labels = [line.strip().split(" ", 1)[1] for line in f.readlines()]

def classify_image(image_path):
    image = Image.open(image_path).convert("RGB")
    image = image.resize((224, 224))

    image_array = np.array(image, dtype=np.float32)
    image_array = image_array / 255.0
    image_array = np.expand_dims(image_array, axis=0)

    predictions = model.predict(image_array)
    predicted_index = np.argmax(predictions)
    confidence = predictions[0][predicted_index]

    return labels[predicted_index], confidence

# Path to test images
base_path = "test_images"

for class_folder in os.listdir(base_path):
    class_path = os.path.join(base_path, class_folder)

    if not os.path.isdir(class_path):
        continue

    print("\nTesting class:", class_folder.upper())

    for image_file in os.listdir(class_path):
        image_path = os.path.join(class_path, image_file)

        label, confidence = classify_image(image_path)

        print(
            f"Image: {image_file} -> Predicted: {label} "
            f"({round(confidence * 100, 2)}%)"
        )
