# GPT2 Article Generator
[![Run on Ainize](https://ainize.ai/images/run_on_ainize_button.svg)](https://ainize.web.app/redirect?git_repo=https://github.com/ha-mulan/gpt2-article-generator)

# GPT2 Article Generator

An application to allow for generating news articles using [OpenAI](https://openai.com)'s [GPT-2 text generator](https://openai.com/blog/better-language-models/). The model used for this was further trained on [All The News](https://www.kaggle.com/snapcrack/all-the-news), a dataset of over 200,000 news articles by [components.one](https://components.one/).

## Setup

The repository can be cloned as normal:

```shell
git clone https://github.com/DanTm99/gpt2-article-generator.git
```

The model this program uses is hosted on Google Drive and can be downloaded from [here](https://drive.google.com/file/d/1zPrdmD9VepOhsCnHaawJfR3yjv5BRL5H). The contents of this archive should be extracted to the `gpt2-article-generator` folder so that the `checkpoint` is in the `gpt2-article-generator` folder.

Navigate into the folder:

```shell
cd gpt2-article-generator
```

To use this with your GPU you must have and NVIDIA GPU with a CUDA Compute Capability 3.5 or higher.

If you have the required hardware you must install the required software on your system as shown [here](https://www.tensorflow.org/install/gpu#software_requirements).

Install the required packages as normal to use this with GPU support:

```shell
pip3 install -r requirements.txt
```

To use this without GPU support use the following command instead:

```shell
pip3 install -r requirements-no-gpu.txt
```

## Usage

To open the GUI use the following command:

```shell
python3 ArticleGenerator.py
```

This application can also be used via the command line. For detailed help use the following command:

```shell
python3 ArticleGenerator.py -h
```
