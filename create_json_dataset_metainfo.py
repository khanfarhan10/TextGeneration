import json
import os
import fnmatch
import numpy as np


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


def search_file(filename, directory):
    files = find(filename, directory)
    if len(files) > 1:
        print("Warning, Multiple Files Found, Selecting First Entry of :", files)
    return files[0]


def get_text(filename='shakespeare.txt', verbose=0):
    # open the txt file first
    ROOT_DIR = os.getcwd()
    data_file = filename if os.path.exists(filename) else search_file(
        filename=filename, directory=os.path.join(ROOT_DIR, "data"))
    path_to_file = data_file

    text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
    # length of text is the number of characters in it
    if verbose == 1:
        print('Length of text: {} characters'.format(len(text)))
    return text


def get_vocabulary(text):
    vocab = sorted(set(text))
    # print(type(vocab))
    # print(vocab)
    return vocab


def save_list_to_json(LIST, filename='dataset_metainfo/shakespeare_metadata.txt'):
    # open output file for writing
    with open(filename, 'w') as filehandle:
        json.dump(LIST, filehandle)


def retrieve_list_from_json(filename='dataset_metainfo/shakespeare_metadata.txt'):
    # open output file for reading
    with open(filename, 'r') as filehandle:
        LIST = json.load(filehandle)
    return LIST


def get_dataset_metainfo(vocab):
    char2idx = {u: i for i, u in enumerate(vocab)}
    idx2char = np.array(vocab)
    return char2idx, idx2char


if __name__ == '__main__':
    text = get_text()
    vocab = get_vocabulary(text)
    save_list_to_json(
        filename='dataset_metainfo/shakespeare_metadata.txt', LIST=vocab)
    char2idx, idx2char= get_dataset_metainfo(vocab)

# python create_json_dataset_metainfo.py
