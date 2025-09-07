import tensorflow_datasets as tfds


def load_data():
    # Load the dataset
    dataset, info = tfds.load('cats_vs_dogs', with_info = True, as_supervised = True)

    return dataset, info

if __name__ == '__main__':
    load_data()