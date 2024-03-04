# Swahili-Llama: A Conversation Large Language Model for Swahili Use Cases and Retrieval Augmented Generation 


<img src="info/swahili_llama.jpg" alt="Swahili LLaMA Image" width="300" height="auto">

## Description

To enhance the use of Large language models for Swahili content, We have created this repository, which aims to provide the code for Swahili-LLaMA - an LLM model based on the open-source LLaMA-2. Our approach includes expanding the vocabulary from the original 32K in LLaMA-2 to 49K in this initial version. We use LoRA for continued pretraining of the model, and the results in this current repository are at checkpoint 35% of 700M tokens based on LLaMA-2.  A comprehensive technical report and the final model at the 100% checkpoint—which promises even greater optimization—will be published shortly. This model demonstrates superior performance in Swahili text generation and is suitable for use with Retrieval-Augmented Generation (RAG) frameworks.

## A cup of Coffee
This work has been self-funded with limited resources, relying on my finances and some computational (2-A6000 GPU) space provided by the AIDLab at UDOM. Given constraints, further development is dependent on external support. If you find this project on Swahili AI worthwhile, please consider a small donation via Buy Me A Coffee to fuel continued progress [buying me a coffee](https://www.buymeacoffee.com/mollel). Any contributions would be invaluable and greatly appreciated by myself and others who could benefit. My goal has always been to enable underserved communities by providing open access. With your backing, I hope to move this effort forward so its social impact may be fully realized. 

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/mollel)




## Table of Contents

- [Usage Note](#usage-note)
- [Available Models](#available-models)
- [Datasets](#datasets)
- [Prompting Format](#prompting-format-for-instruction-models)
- [Contributions](#contributions)
- [License](#license)
- [Citation](#citation)
- [Contact](#contact)

## Usage Note
This initial version of the model has yet to go through detoxification or alignment with human evaluative criteria. For now, it is meant only for research purposes. we expect later versions will show improvements in areas like reducing hallucinations and harmful or offensive content generation and text generation. Current model outputs should be considered experimental and interpreted with caution by researchers.

## Available Models

| Model                    | Type                        | Data              | Base Model           | # Params | Download Links                                                         |
|--------------------------|-----------------------------|-------------------|----------------------|------|------------------------------------------------------------------------|
| Swahili LLaMA 7B Base      | Base model                  | 2GB              | LLaMA 7B             | 7B   | [HF Hub](https://huggingface.co/Mollel/swahili_LLaMA_7Bv0.1), [Kaggle](https://www.kaggle.com/models/mikemollel/new-model-swahili)    |
| Swahili Instruct LLaMA 7B      | Instruct model                  | 2GB               | LLaMA 7B            | 7B  | [HF Hub](https://huggingface.co/Mollel/swahili-Instruct-llama-2-7b/tree/main)    |
| Swahili LLaMA 13B Base     | Base model                  | 2GB               | LLaMA 13B            | 13B  | [Soon]    |


### Quantized Version of Available Models

| Model                    | Format | Bits                 | Download Links                                                               |
|--------------------------|--------|----------------------|------------------------------------------------------------------------------|
| Swahili LLaMA 7B Base      | GGUF   | Q8_0 | [HF Hub](https://huggingface.co/Mollel/swahili_LLaMA_7Bv0.1_GGUF)      |
| Swahili LLaMA 7B Instruct      | GGUF   | Q4_K_M | [HF Hub](https://huggingface.co/Mollel/swahili-Instruct-llama-2-7b-GGUF/blob/main/swahili-instruct-llama-2-7b.Q4_K_M.gguf)      |
| Swahili LLaMA 7B Instruct      | GGUF   | Q5_K_M | [HF Hub](https://huggingface.co/Mollel/swahili-Instruct-llama-2-7b-GGUF/blob/main/swahili-instruct-llama-2-7b.Q5_K_M.gguf)      |
| Swahili LLaMA 13B Base     | GGUF   | Q8_0 | [Soon]     |

## Datasets

In this repository, I have included a Swahili-translated version of the Alpaca dataset. This dataset has been used for instruction fine-tuning in the current experiments. However, it's important to note that as of now, we have not performed any formal evaluation of the fine-tuned models. Evaluation will be conducted once we complete the experiments with the 13B parameter model. The evaluation results and analysis will be included in future updates to this repository.

**Swahili Alpaca Credit**: [iamshnoo/alpaca-cleaned-swahili](https://huggingface.co/datasets/iamshnoo/alpaca-cleaned-swahili)

## Prompting Format for Instruction Models

**Prompt Template Without Input**

```
<s>[INST] {prompt} [/INST]
```


## Contributions

We welcome contributions to this project. If you have suggestions or improvements, please open an issue or a pull request.

## License

This project is licensed under the GNU GPL v3.0 license - see the [LICENSE.md](LICENSE) file for details.

> **IMPORTANT**: The [GPL 3.0 License](LICENSE) is applicable solely to the source code and datasets provided. As this project is a derivative of Meta's LLaMA 2 model, it is subject to the original licensing of LLaMA 2, which cannot be altered. Therefore, for comprehensive details regarding the licensing of the model, please consult the [LLAMA2-LICENSE](LLAMA2-LICENSE) file.


## Citation

If you use this model in your research, please cite: Soon




## Contact

If you have any questions about the codebase or research, please don't hesitate to contact me, Michael Mollel, at msamwelmollel@gmail.com. In addition to my research, I also offer AI consulting and development services for companies - so reach out if you are looking for customized AI solutions. Whether you need clarification on my projects or want to discuss a potential collaboration, I welcome the conversation and opportunity to work together. Please email me so we can determine if my expertise matches your needs.
