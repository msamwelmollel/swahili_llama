# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 21:53:26 2024

@author: msamwelmollel
"""

from datasets import load_dataset
import json

def save_dataset_as_json(dataset_name, json_file_path):
    # Load the dataset
    dataset = load_dataset(dataset_name)
    
    # Convert the dataset to a list of dictionaries
    # Adjust 'train' to other splits if necessary
    data_as_list = [item for item in dataset['train']]
    
    # Save the list to a JSON file
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data_as_list, json_file, ensure_ascii=False, indent=4)

# Example usage
# dataset_name = "tatsu-lab/alpaca"
dataset_name = "iamshnoo/alpaca-cleaned-swahili"
json_file_path = 'swahili_dataset.json'
save_dataset_as_json(dataset_name, json_file_path)

