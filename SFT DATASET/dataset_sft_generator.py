# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 21:03:43 2024

@author: msamwelmollel
"""

import pandas as pd
from datasets import Dataset, DatasetDict
from datasets import load_dataset
import json
import random

# Replace 'path_to_your_json_file.json' with the path to your JSON file
json_file_path = './swahili_alpaca_dataset.json'



# Load your JSON file
with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)['documents']
    



# Transform data to match desired structure
transformed_data = {
    'instruction': [d['instruction'] for d in data],
    'input': [d['input'] for d in data],
    'output': [d['output'] for d in data]
}

# Create a Dataset from the transformed data
dataset = Dataset.from_dict(transformed_data)


# Wrap the Dataset in a DatasetDict under the 'train' split
dataset = DatasetDict({'train': dataset})





print(dataset)
print("-"*50)
print(dataset['train'][random.randint(1,dataset['train'].shape[0])])
print("-"*50)
print(dataset['train'][random.randint(1,dataset['train'].shape[0])])


train_test_split = dataset['train'].train_test_split(test_size=0.2)

print(train_test_split)



