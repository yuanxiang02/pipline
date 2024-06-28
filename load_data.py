from datasets import load_dataset
import requests
import zipfile
import io
from PIL import Image
import json
class DatasetLoader:

    def __init__(self, dataset_name, split):
        self.dataset_name = dataset_name
        self.split = split
        self.dataset = None

    def load_data(self):
        try:
            self.dataset = load_dataset(self.dataset_name, split=self.split)
        except Exception as e:
            print(f"An error occurred while loading datasets")

    def get_example(self, index=0):
        if self.dataset:
            return self.dataset[index]
        else:
            raise ValueError('Dataset not loaded')


if __name__ == "__main__":
    loader = DatasetLoader("squad", split="validation")
    # loader.load_data()
    # example = loader.get_example()
    # print("\nExample from validation set:")
    # print(example)
