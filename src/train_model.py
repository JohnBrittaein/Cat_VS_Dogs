from create_model import create_model
from load_data import load_data 
from split_data import split_data
from pre_process_data import preprocess_data

# Load the dataset
dataset, info = load_data()

# split the dataset into training and test datasets
train_dataset, test_dataset = split_data(dataset, info)

# preprocess the dataset 
train_dataset, test_dataset = preprocess_data(train_dataset, test_dataset)

for images, labels in train_dataset.take(1):
    print("Batch shape:", images.shape)
    print("Labels shape:", labels.shape)


# create the model
model = create_model()

# train the model
history = model.fit(train_dataset, epochs = 10, validation_data = test_dataset)

# Evaluate the data
test_loss, test_acc = model.evaluate(test_dataset)
print(f"Test accuracy: {test_acc}")

# Save the model
model.save('saved_models/Cat_VS_Dog_Model_ver_1.h5')
