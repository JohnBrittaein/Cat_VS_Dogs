import tensorflow as tf

def preprocess_image(image):
    # Resize image to 224 x 224
    image = tf.image.resize(image, [224, 224])

    # Normalize image 
    image = image / 255.0
    return image

def preprocess_data(train_dataset, test_dataset):
    train_dataset = train_dataset.map(lambda x, y: (preprocess_image(x), y))
    test_dataset = test_dataset.map(lambda x, y: (preprocess_image(x), y))

    train_dataset = train_dataset.batch(32).prefetch(tf.data.AUTOTUNE)
    test_dataset = test_dataset.batch(32).prefetch(tf.data.AUTOTUNE)

    return train_dataset, test_dataset
