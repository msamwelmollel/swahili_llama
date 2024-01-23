# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 13:45:22 2024

@author: msamwelmollel
"""


# WANDB_API_KEY = None # replace None with your weights and Biases API key (optional)
# TOGETHER_API_KEY = "xxxx" # replace "xxxx" with your together API key (needed but easy)


import json
import os
import random
import together
from datasets import load_dataset

# Specify path to your JSON file
json_path = os.path.join(os.getcwd(), 'google_translated - Copy.json')

# Open the JSON file and load it into a dict
with open(json_path, 'r') as json_file:
    ourdataset = json.load(json_file)
    





def format_to_llama2_chat(system_prompt, user_model_chat_list):

    """ this function follows from
    https://docs.together.ai/docs/fine-tuning-task-specific-sequences

    It converts this ourdataset into the Llama-2 prompting structure

    Args:
      system_prompt (str): instructions from you the developer to the AI
      user_model_chat_list (List[Tuple[str,str]]): a list of tuples,
        where each tuple is a pair or exchange of string utterances, the first by the user,
        the second by the AI. The earlier exchanges are on the left, meaning time
        runs left to right.
    Returns:
      growing_prompt (str): the concatenated sequence starting with system_prompt and
        alternating utterances between the user and AI with the last AI utternance on the right.
    """

    growing_prompt = f"""<s>[INST] <<SYS>> {system_prompt} <</SYS>>"""

    for user_msg, model_answer in user_model_chat_list:
        growing_prompt += f""" {user_msg} [/INST] {model_answer} </s>"""

    return growing_prompt

format_to_llama2_chat(
    "You are a good robot",
    [("hi robot", "hello human"),("are you good?", "yes im good"),("are you bad?", "no, im good")]
)


data_list = []

for sample in ourdataset:

    instruction_input_separator = random.choice([":", ": ", "\n", "\n\n", " "])
    # instruction_input_separator = random.choice([":" ])
    input = sample['input'] if sample['input'] is not None else ""
    instruction = sample['instruction'] if sample['instruction'] is not None else ""

    training_sequence = format_to_llama2_chat(
        "you are a helpful assistant",
        [(instruction+instruction_input_separator+input,sample['output'])]
    )

    data_list.append({
        "text":training_sequence
    })




# save the reformatted dataset locally
together.Files.save_jsonl(data_list, "Alpaca_Swahili_Dataset.jsonl")


# check your data with your base model prompting type before uploading
resp = together.Files.check(file="Alpaca_Swahili_Dataset.jsonl")
print(resp['is_check_passed'])