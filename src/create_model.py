import tensorflow as tf
from tensorflow.keras import layers, models

# Using a CNN model for image classification and recogniztion
def create_model():
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation = 'relu', input_shape = (224, 224, 3)),
        layers.MaxPooling2D(2, 2),

        # Second Convolutional Layer
        layers.Conv2D(64, (3, 3), activation = 'relu'),
        layers.MaxPooling2D(2, 2),

        # Third Convolutional Layer
        layers.Conv2D(128, (3, 3), activation = 'relu'),
        layers.MaxPooling2D(2, 2),

        # Flatten the output from Convolutional layers
        layers.Flatten(),

        # Fully connected layer
        layers.Dense(128, activation = 'relu'),

        # Output layer (2 classes: cat or dog)
        layers.Dense(1, activation = 'sigmoid')
    ])

    # Compile the model
    model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

    return model