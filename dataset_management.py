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

WANDB_API_KEY= "50a4ae3d3476d2fa831569e4d22bfec32200130f"


# WANDB_API_KEY = None # replace None with your weights and Biases API key (optional)


# lets use our base model to see how it works before we finetune it

base_model_name = "togethercomputer/Llama-2-7B-32K-Instruct"
#base_model_name = "togethercomputer/llama-2-7b-chat"

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

for sample in ourdataset[0:10000]:

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
print(resp)


# upload your dataset file to together and save the file-id, youll need it to start your finetuning run
file_resp = together.Files.upload(file="Alpaca_Swahili_Dataset.jsonl")
file_id = file_resp["id"]
print("-"*50)
print(file_resp)


# Submit your finetune job
ft_resp = together.Finetune.create(
  training_file = file_id ,
  model = base_model_name,
  n_epochs = 1,
  batch_size = 4,
  n_checkpoints = 1,
  learning_rate = 5e-5,
  wandb_api_key = WANDB_API_KEY,
  #estimate_price = True,
  suffix = 'law',
)

fine_tune_id = ft_resp['id']
print(ft_resp)


# run this from time to time to check on the status of your job
print(together.Finetune.retrieve(fine_tune_id=fine_tune_id)) # retrieves information on finetune event
print("-"*50)
print(together.Finetune.get_job_status(fine_tune_id=fine_tune_id)) # pending, running, completed
print(together.Finetune.is_final_model_available(fine_tune_id=fine_tune_id)) # True, False
print(together.Finetune.get_checkpoints(fine_tune_id=fine_tune_id)) # list of checkpoints