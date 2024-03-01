# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 23:55:59 2024

@author: msamwelmollel
"""

# Based on https://github.com/ymcui/Chinese-LLaMA-Alpaca/blob/main/scripts/merge_tokenizer/merge_tokenizers.py
# & and https://github.com/abhinand5/tamil-llama/blob/main/scripts/train/sentencepiece/merge_tokenizer.py
import os

os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"
import argparse

import sentencepiece as spm
from sentencepiece import sentencepiece_model_pb2 as sp_pb2_model
from transformers import LlamaTokenizer

parser = argparse.ArgumentParser()
parser.add_argument("--llama_tokenizer_dir", default=None, type=str, required=True)
parser.add_argument("--swahili_sp_model_file", default="swahili_token/swahili_sp.model", type=str)
args = parser.parse_args()

llama_tokenizer_dir = args.llama_tokenizer_dir
swahili_sp_model_file = args.swahili_sp_model_file

# load
llama_tokenizer = LlamaTokenizer.from_pretrained(llama_tokenizer_dir)
swahili_sp_model = spm.SentencePieceProcessor()
swahili_sp_model.Load(swahili_sp_model_file)

llama_spm = sp_pb2_model.ModelProto()
llama_spm.ParseFromString(llama_tokenizer.sp_model.serialized_model_proto())
swahili_spm = sp_pb2_model.ModelProto()
swahili_spm.ParseFromString(swahili_sp_model.serialized_model_proto())

# print number of tokens
print(len(llama_tokenizer), len(swahili_sp_model))
print(llama_tokenizer.all_special_tokens)
print(llama_tokenizer.all_special_ids)
print(llama_tokenizer.special_tokens_map)

## Add Tamil tokens to LLaMA tokenizer
llama_spm_tokens_set = set(p.piece for p in llama_spm.pieces)
print(len(llama_spm_tokens_set))
print(f"Before:{len(llama_spm_tokens_set)}")
for p in swahili_spm.pieces:
    piece = p.piece
    if piece not in llama_spm_tokens_set:
        new_p = sp_pb2_model.ModelProto().SentencePiece()
        new_p.piece = piece
        new_p.score = 0
        llama_spm.pieces.append(new_p)
print(f"New model pieces: {len(llama_spm.pieces)}")

## Save
output_sp_dir = "merged_tokenizer_sp"
output_hf_dir = "merged_tokenizer_hf"  # the path to save Tamil-LLaMA tokenizer
os.makedirs(output_sp_dir, exist_ok=True)
with open(output_sp_dir + "/swahili_llama.model", "wb") as f:
    f.write(llama_spm.SerializeToString())
tokenizer = LlamaTokenizer(vocab_file=output_sp_dir + "/swahili_llama.model")

tokenizer.save_pretrained(output_hf_dir)
print(f"Swahili-LLaMA tokenizer has been saved to {output_hf_dir}")


# Test
llama_tokenizer = LlamaTokenizer.from_pretrained(llama_tokenizer_dir)
swahili_llama_tokenizer = LlamaTokenizer.from_pretrained(output_hf_dir)
print(tokenizer.all_special_tokens)
print(tokenizer.all_special_ids)
print(tokenizer.special_tokens_map)
text = """Je Tanzania inaweza kuchukua kombe la mataifa ya Africa?
Can Tanzania secure the CAF Cup trophy?"""
print("Test text:\n", text)
llama_tokenized = llama_tokenizer.tokenize(text)
swahili_llama_tokenized = swahili_llama_tokenizer.tokenize(text)
print(f"Tokenized by LLaMA tokenizer:{llama_tokenized}")
print(f"LLaMA tokenizer n_tokens={len(llama_tokenized)}")
print(f"Tokenized by Swahili-LLaMA tokenizer:{swahili_llama_tokenized}")
print(f"Swahili LLaMA tokenizer n_tokens={len(swahili_llama_tokenized)}")
