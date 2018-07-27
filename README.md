# Language Style Transfer
This repo contains the code and data of the following paper:

<i> "Style Transfer from Non-Parallel Text by Cross-Alignment". Tianxiao Shen, Tao Lei, Regina Barzilay, and Tommi Jaakkola. NIPS 2017. [arXiv](https://arxiv.org/abs/1705.09655)</i>

The method learns to perform style transfer between two non-parallel corpora. For example, given positive and negative reviews as two corpora, the model can learn to reverse the sentiment of a sentence.
<p align="center"><img width=800 src="img/example_sentiment.png"></p>

<br>

## Spotlight Video
[![overview](https://img.youtube.com/vi/OyjXG44j-gs/0.jpg)](https://www.youtube.com/watch?v=OyjXG44j-gs)

<br>

## Data Format
`data/poetry.json` contains Russian 19th century poetry. Also we use Russian Wikipedia as other source.

## Quick Start
- To train a model, first create a <code>tmp/</code> folder (where the model and results will be saved), then go to the <code>code/</code> folder and run the following command:
```bash
python style_transfer.py --train ../data/yelp/sentiment.train --dev ../data/yelp/sentiment.dev --output ../tmp/sentiment.dev --vocab ../tmp/yelp.vocab --model ../tmp/model
```

- To test the model, run the following command:
```bash
python style_transfer.py --test ../data/yelp/sentiment.test --output ../tmp/sentiment.test --vocab ../tmp/yelp.vocab --model ../tmp/model --load_model true --beam 8
```

- Check <code>code/options.py</code> for all running options.

<br>

## Dependencies
Python >= 3.6, TensorFlow 1.8.0
