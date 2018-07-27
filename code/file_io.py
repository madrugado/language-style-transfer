import os

from nltk import word_tokenize, sent_tokenize
import json
import wikipedia
from tqdm import tqdm


def load_doc(path):
    data = []
    with open(path) as f:
        for line in f:
            sents = sent_tokenize(line)
            doc = [word_tokenize(sent) for sent in sents]
            data.append(doc)
    return data


def load_sent(path, max_size=-1):
    data = []
    with open(path) as f:
        for line in f:
            if len(data) == max_size:
                break
            data.append(line.split())
    return data


def load_vec(path):
    x = []
    with open(path) as f:
        for line in f:
            p = line.split()
            p = [float(v) for v in p]
            x.append(p)
    return x


def load_json(path):
    data = []
    with open(path) as f:
        j = json.load(f)
        for doc in tqdm(j, "Loading poetry:\t"):
            if doc['poet_id'] != 'pushkin':
                continue
            sents = sent_tokenize(doc["content"].replace("\\n", " ").replace("\xa0", " "))
            doc = [word_tokenize(sent) for sent in sents]
            data.append(doc)
    return data


def load_wikipedia():
    data = []
    wiki_path = "../data/wiki.parsed"
    if not os.path.exists(wiki_path):
        wikipedia.set_lang("ru")
        pages = wikipedia.page("Википедия:Хорошие_статьи").links
        for p in tqdm(pages, "Loading Wikipedia:\t"):
            try:
                sents = sent_tokenize(wikipedia.page(p).content)
                doc = [word_tokenize(sent) for sent in sents]
                data.append(doc)
            except wikipedia.exceptions.PageError:
                print("Cannot load page: " + p)

        with open(wiki_path, "wt") as f:
            json.dump(data, f)
    else:
        with open(wiki_path, "rt") as f:
            data = json.load(f)
    return data


def write_doc(docs, sents, path):
    with open(path, 'w') as f:
        index = 0
        for doc in docs:
            for i in range(len(doc)):
                f.write(' '.join(sents[index]))
                f.write('\n' if i == len(doc) - 1 else ' ')
                index += 1


def write_sent(sents, path):
    with open(path, 'w') as f:
        for sent in sents:
            f.write(' '.join(sent) + '\n')


def write_vec(vecs, path):
    with open(path, 'w') as f:
        for vec in vecs:
            for i, x in enumerate(vec):
                f.write('%.3f' % x)
                f.write('\n' if i == len(vec) - 1 else ' ')
