import tensorflow as tf
from tensorflow.keras.preprocessing import image as keras_image

def preprocess_image(image_path):
    # Load the image from file
    img = keras_image.load_img(image_path, target_size=(224, 224))  # Resize to (224, 224)
    
    # Convert image to a numpy array
    img_array = keras_image.img_to_array(img)
    
    # Add a batch dimension (to simulate batch size of 1)
    img_array = tf.expand_dims(img_array, axis=0)

    # Normalize the image
    img_array = img_array / 255.0

    return img_array

def predict(model, image):
    image = preprocess_image(image)

    prediction = model.predict(image)

    if prediction >= 0.5:
        return "Dog"
    else: 
        return "Cat"
