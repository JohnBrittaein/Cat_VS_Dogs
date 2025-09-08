from tensorflow.keras.models import load_model
from predict import predict

model = load_model('saved_models/Cat_VS_Dog_Model_ver_1.h5')

image_path = 'images/image2.jpg'

prediction = predict(model, image_path)

print(prediction)