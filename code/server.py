import tensorflow as tf
from flask import Flask, request, jsonify
from nltk.tokenize import word_tokenize

import beam_search, greedy_decoding
from options import load_arguments
from style_transfer import create_model
from utils import get_batch
from vocab import Vocabulary

app = Flask(__name__)

y = 0  # poetry
args = load_arguments()

vocab = Vocabulary(args.vocab, args.embedding, args.dim_emb)
print('vocabulary size:', vocab.size)
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.Session(config=config)
model = create_model(sess, args, vocab)
if args.beam > 1:
    decoder = beam_search.Decoder(sess, args, vocab, model)
else:
    decoder = greedy_decoding.Decoder(sess, args, vocab, model)


@app.route('/ready')
def ready():
    return 'OK'


@app.route('/generate/<poet_id>', methods=['POST'])
def generate(poet_id):
    if poet_id != "pushkin":
        generated_poem = 'Карл у Клары украл кораллы,\nКлара у Карла украла кларнет'
        return jsonify({'poem': generated_poem})
    else:
        request_data = request.get_json()
        seed = request_data['seed']
        batch = get_batch([word_tokenize(seed)], [y], vocab.word2id)
        ori, tsf = decoder.rewrite(batch)
        return jsonify({'poem': ' '.join(w for w in tsf[0])})


if __name__ == '__main__':
    app.run(port=8000)
