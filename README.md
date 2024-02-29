# Swahili-Llama: A Conversation Large Language Model for Swahili Use Cases and Retrieval Augmented Generation 


<img src="info/swahili_llama.jpg" alt="Swahili LLaMA Image" width="300" height="auto">

## Description

To enhance the use of Large language models for Swahili content, We have created this repository, which aims to provide the code for Swahili-LLaMA - an LLM model based on the open-source LLaMA-2. Our approach includes expanding the vocabulary from the original 32K in LLaMA-2 to 49K in this initial version. We use LoRA for continued pretraining of the model, and the results in this current repository are at checkpoint 50% of 500M tokens based on LLaMA-2.  A comprehensive technical report and the final model at the 100% checkpoint—which promises even greater optimization—will be published shortly. This model demonstrates superior performance in Swahili text generation and is suitable for use with Retrieval-Augmented Generation (RAG) frameworks.


## Usage Note
This initial version of the model has yet to go through detoxification or alignment with human evaluative criteria. For now, it is meant only for research purposes. Once supervised training and model alignment is complete, we expect later versions will show improvements in areas like reducing hallucinations and harmful or offensive content generation. The goal is to enhance performance to address ethical concerns before releasing for other applications. However, as an unfinished product, all current model outputs should be considered experimental and interpreted with caution by researchers.

## Table of Contents


- [Available Models](#available-models)
- [Benchmark Scores](#benchmark-scores)
- [Demo](#demo)
- [Getting Started](#getting-started)
- [Datasets](#datasets)
- [Prompting Format](#prompting-format-for-instruction-models)
- [Usage Note](#usage-note)
- [Contributions](#contributions)
- [License](#license)
- [Citation](#citation)
- [Contact](#contact)

## Available Models

| Model                    | Type                        | Data              | Base Model           | # Params | Download Links                                                         |
|--------------------------|-----------------------------|-------------------|----------------------|------|------------------------------------------------------------------------|
| Swahili LLaMA 7B Base      | Base model                  | 2GB              | LLaMA 7B             | 7B   | [HF Hub](https://huggingface.co/Mollel/swahili_LLaMA_7Bv0.1_GGUF), [Kaggle](https://www.kaggle.com/models/mikemollel/new-model-swahili)    |
| Swahili LLaMA 13B Base     | Base model                  | 2GB               | LLaMA 13B            | 13B  | [Soon]    |
 


## Contributions

We welcome contributions to this project. If you have suggestions or improvements, please open an issue or a pull request.

## License

This project is licensed under the GNU GPL v3.0 license - see the [LICENSE.md](LICENSE) file for details.

> **IMPORTANT**: The [GPL 3.0 License](LICENSE) is applicable solely to the source code and datasets provided. As this project is a derivative of Meta's LLaMA 2 model, it is subject to the original licensing of LLaMA 2, which cannot be altered. Therefore, for comprehensive details regarding the licensing of the model, please consult the [LLAMA2-LICENSE](LLAMA2-LICENSE) file.


## Citation

If you use this model in your research, please cite:

```bibtex
@misc{michaelmollelllama,
      title={Swahili-Llama: A Conversation Large Language Model for Swahili Use Cases and RAG}, 
      author={},
      year={2024},
      eprint={},
      archivePrefix={},
      primaryClass={}
}
```


## Contact

If you have any questions about the codebase or research, please don't hesitate to contact me, Michael Mollel, at msamwelmollel@gmail.com. In addition to my research, I also offer AI consulting and development services for companies - so reach out if you are looking for customized AI solutions. Whether you need clarification on my projects or want to discuss a potential collaboration, I welcome the conversation and opportunity to work together. Please email me so we can determine if my expertise matches your needs.
