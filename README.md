# Question-Gen-Chroma

Generate questions based on corpora through your own LLM APIs.

## Setup

This project is based on [this repo](https://github.com/ElementQi/chroma_chunking_evaluation).

You are supposed to install the modified version of `chroma_chunking`:

```
git clone https://github.com/ElementQi/chroma_chunking_evaluation.git
cd chroma_chunking_evaluation
pip install -e .
```

You can add any class like what I did, for example,  `QwenSyntheticEvaluation` class in `chunking_evaluation\evaluation_framework\synthetic_evaluation.py`. Just inheritage `SyntheticEvaluation`, the parent class and make some little changes on models you are going to calling.

## Usage

Due to the shortage of the original repo that it only support English corpora well, we need to do more steps for generating content suitable for other languages like Chinese.


There might be some of errors during generation, just wait until the code works.

sample code:

```
python generate.py --key [your-apikey] \
  --corpora-path corpora/pride_and_prejudice.txt \
  --save-path saves/pride_query.csv \
  --query-num 5 \
  --round-num 1
```

If your corpora is non-English:

```
python generate.py --key [your-apikey] \
  --corpora-path corpora/莫言中短篇小说散文选.txt \
  --save-path saves/novel_query.csv \
  --query-num 5 \
  --round-num 1 \
  --non-en True
```

If you are using windows cmd, try:

```
python generate.py --key [your-key] --corpora-path "corpora/莫言中短篇小说散文选.txt" --save-path "saves/novel_query_2.csv" --query-num 2 --round-num 1 --non-en True
```

The files are saved in `/saves`.
