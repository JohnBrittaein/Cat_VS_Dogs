
# 🐱 Cat vs. Dog Classifier 🐶

This project is a **Convolutional Neural Network (CNN)** model that can distinguish between **cats** and **dogs** in images. Inspired by tutorials and articles, such as [Cat & Dog Classification Neural Network in Python](https://www.geeksforgeeks.org/deep-learning/cat-dog-classification-using-convolutional-neural-network-in-python/), this project was designed as an introduction to using AI models with Python.

Ultimately, the goal was to familiarize myself with building, training, and deploying AI models—starting with a simple binary classification task: Cats vs. Dogs.

---

## 🚀 Features

- **Simple CNN Architecture**: A straightforward Convolutional Neural Network that is easy to understand and train for binary image classification tasks.
- **Image Preprocessing**: Resizing, normalization, and batching for preparing image data.
- **Model Evaluation**: Track performance during training, including accuracy and loss metrics.
- **Saving & Loading**: The trained model can be saved and reloaded for future predictions.

---

## 💻 Getting Started

To get started with this project, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/cat-vs-dog-classifier.git
cd cat-vs-dog-classifier
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate # On Window, use `venv/Scripts/activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

# 📸 Using the Model

After setting up the environment and installing dependencies, you can begin using the model. Follow these steps:

## 1. Train The Model

Run `train_model` this will train the model using Tensorflow dataset 

```bash
python train_model.py
```

## 2. Prepare Your Images

Place your cat and dog images the `images` folder
Change the `image_path = 'images/image1.jpg'` to your desired image

## 3. Run the Model

Run the `run_model.py` script and view the results in the terminal

```bash
python run_model.py
```

# 🛠️ Improvements & Future Work

This is just the beginning! While the current model is functional, there are several ways it can be improved:

 - **GUI for Easier Interaction:** In the future, I plan to develop a simple graphical user interface (GUI) where you can drag and drop images and see the prediction.
 - **Expanded Dataset:** Currently, the model is designed only for binary classification (Cats vs. Dogs). Expanding the dataset to include more animal categories would make the model more general. This might involve retraining with a larger, more diverse dataset or creating a new project entirely.
 - **Model Enhancements:** Further optimizations and more advanced techniques, such as transfer learning, could be used to improve accuracy, especially for more complex datasets.

# 📚 Files Structure

```plaintext
.
├── cat_vs_dog_classifier/
│   ├── create_model.py      # Defines the CNN model architecture
│   ├── load_data.py         # Loads and processes the dataset
│   ├── pre_process_data.py  # Handles image resizing and normalization
│   ├── predict.py           # Loads the trained model and makes predictions
│   ├── run_model.py         # Main entry point to run the model after it's been trained
|   ├── train_model.py       # Trains the model using Tensorflows dataset
│   └── requirements.txt     # Project dependencies
└── README.md                # Project documentation
```

# 📝 Conclusion

This project was an excellent starting point for my journey into deep learning with Python. While it is simple, it demonstrates how to build a functional AI model from the ground up—training, evaluating, and deploying a classification model with images. There’s plenty of room for improvement, but this project helped me solidify foundational concepts and tools that I can apply to more advanced machine learning tasks in the future.
