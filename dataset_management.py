# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 13:45:22 2024

@author: msamwelmollel
"""
from datasets import load_dataset


import json
import os

# Specify path to your JSON file
json_path = os.path.join(os.getcwd(), 'google_translated.json')

# Open the JSON file and load it into a dict
with open(json_path, 'r') as json_file:
    legal_dataset = json.load(json_file)
    


print(legal_dataset)
print("-"*50)
# print(legal_dataset['train'][0])
# print("-"*50)
# print(legal_dataset['train'][1])