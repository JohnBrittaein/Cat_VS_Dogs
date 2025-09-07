import tensorflow_datasets as tfds

def split_data(dataset, info):
    # Extract the 'train' split
    train_dataset = dataset['train']

    # Split the dataset into 80% train, 20% test
    train_size = int(0.8 * info.splits['train'].num_examples)
    test_size = info.splits['train'].num_examples - train_size

    train_split = train_dataset.take(train_size)
    test_split = train_dataset.skip(train_size)

    return train_split, test_split
