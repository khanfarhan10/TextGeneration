from create_json_dataset_metainfo import retrieve_list_from_json, get_dataset_metainfo
import tensorflow as tf
import numpy as np
import os
import time
import sqlite3
import os
import fnmatch


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


def find_model(filename='shakespearen_model.h5'):
    model_file = filename if os.path.exists(filename) else search_file(
        filename=filename, directory=os.path.join(ROOT_DIR, "saved_models"))
    return model_file


def build_model(vocab_size, embedding_dim, rnn_units, batch_size):
    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(vocab_size, embedding_dim,
                                  batch_input_shape=[batch_size, None]),
        tf.keras.layers.GRU(rnn_units,
                            return_sequences=True,
                            stateful=True,
                            recurrent_initializer='glorot_uniform'),
        tf.keras.layers.Dense(vocab_size)
    ])
    return model


def generate_text(model, start_string, num_generate=1000, temperature=1.0):
    # Evaluation step (generating text using the learned model)
    # Number of characters to generate
    # Converting our start string to numbers (vectorizing)
    input_eval = [char2idx[s] for s in start_string]
    input_eval = tf.expand_dims(input_eval, 0)
    # Empty string to store our results
    text_generated = []
    # Low temperatures results in more predictable text.
    # Higher temperatures results in more surprising text.
    # Experiment to find the best setting.

    # Here batch size == 1
    model.reset_states()
    for i in range(num_generate):
        predictions = model(input_eval)
        # remove the batch dimension
        predictions = tf.squeeze(predictions, 0)
        # using a categorical distribution to predict the character returned by the model
        predictions = predictions / temperature
        predicted_id = tf.random.categorical(
            predictions, num_samples=1)[-1, 0].numpy()
        # We pass the predicted character as the next input to the model
        # along with the previous hidden state
        input_eval = tf.expand_dims([predicted_id], 0)
        text_generated.append(idx2char[predicted_id])
    return (start_string + ''.join(text_generated))


if __name__ == '__main__':
    ROOT_DIR = os.getcwd()
    #######
    # Shakespeare Metadata
    vocab = retrieve_list_from_json(
        filename='dataset_metainfo/shakespeare_metadata.txt')
    char2idx, idx2char = get_dataset_metainfo(vocab)
    unique_chars = len(vocab)
    embedding_dim = 256
    rnn_units = 1024
    BATCH_SIZE = 64

    model = build_model(vocab_size=unique_chars,
                        embedding_dim=embedding_dim, rnn_units=rnn_units, batch_size=1)
    model_file = find_model()
    model.load_weights(model_file)
    model.build(tf.TensorShape([1, None]))

    print(generate_text(model, start_string=u"ROMEO: ",
                        num_generate=2000, temperature=0.8))


# aim is to save every single thingy in the database to be able to regenrate the output
# python text_gen_pred.py
