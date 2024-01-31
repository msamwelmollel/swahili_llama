# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 19:47:21 2024

@author: msamwelmollel
"""

import sentencepiece as spm
import os

# Load the SentencePiece model
sp = spm.SentencePieceProcessor()
sp.load('C:\\Users\\msamwelmollel\\Documents\\GitHub\\swahili_llama\\scripts\\train\\sentencepiece\\merged_tokenizer_sp\\swahili_llama.model')

# Your sentence
sentence = "Baba yangu anakula kuku."


file_names = ["C:\\Users\\msamwelmollel\\Documents\\GitHub\\swahili_llama\\corpora\\swa_community_2019-sentences.txt"]  # List of file names
sentences = []


import os

directory_path = 'C:\\Users\\msamwelmollel\\Documents\\GitHub\\swahili_llama\\corpora'  # Replace with your folder path
all_texts = []
total_token = 0

# Loop through each file in the directory
for filename in os.listdir(directory_path):
    sentences = []
    if filename.endswith('.txt'):  # Check if the file is a .txt file
        sentence = ""
        file_path = os.path.join(directory_path, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                sentence= sentence+line
            sentences.append(sentence)
            
        tokens = sp.encode_as_pieces(sentences[0])
        token_count = len(tokens)
        total_token= total_token + token_count
        print(["*"]*10)
        print('Number of tokens:', token_count)
        print('Number of Total tokens:', total_token)
        print(["*"]*10)
            # content = file.read()
            # all_texts.append(content)

# At this point, all_texts contains the contents of all text files in the folder
# file_names = ["C:\\Users\\msamwelmollel\\Documents\\GitHub\\swahili_llama\\corpora\\swa_community_2019-sentences.txt"]  # List of file names
# sentences = []

# for file_name in file_names:
#     sentence = ""
#     with open(file_name, 'r', encoding='utf-8') as file:
#         for line in file:
#             sentence= sentence+line
#         sentences.append(sentence)
        
        
#         # content = file.read()
#         # sentence.append(content)

# # all_texts now contains the contents of all files as strings



# # Tokenize the sentence
# tokens = sp.encode_as_pieces(sentence)

# # Count the tokens
# token_count = len(tokens)

# print("Tokens:", tokens)
# print('Number of tokens:', token_count)
# # print("Number of tokens:", token_count)