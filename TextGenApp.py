# streamlit run TextGenApp.py

import sqlite3
from create_json_dataset_metainfo import retrieve_list_from_json, get_dataset_metainfo
import random
import pandas as pd
import fnmatch
import os
import time
import json
import numpy as np
import streamlit.components.v1 as components
import streamlit as st
import tensorflow as tf
import warnings
import sqlite3

from sha1_algo import get_SHA1
warnings.filterwarnings("ignore")


ROOT_DIR = os.getcwd()


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
    # print(files)
    return files[0]


def find_model(filename='shakespearen_model.h5'):
    model_file = filename if os.path.exists(filename) else search_file(
        filename=filename+"*", directory=os.path.join(ROOT_DIR, "saved_models"))
    return model_file


def find_metadata(filename='shakespeare_metadata.txt'):
    metadata_file = filename if os.path.exists(filename) else search_file(
        filename=filename+"*", directory=os.path.join(ROOT_DIR, "dataset_metainfo"))
    return metadata_file


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

# python TextGenPred.py


@st.cache
def load_weights(model, path_to_weightsfile):
    model.load_weights(path_to_weightsfile)
    return model


def GenerateFromStart(model_name="shakespeare", start_string="ROMEO :", num_generate=1000, temp=1):
    ROOT_DIR = os.getcwd()

    metadata_file = find_metadata(filename=model_name)
    vocab = retrieve_list_from_json(filename=metadata_file)

    char2idx, idx2char = get_dataset_metainfo(vocab)
    unique_chars = len(vocab)
    embedding_dim = 256
    rnn_units = 1024
    BATCH_SIZE = 64

    model = build_model(vocab_size=unique_chars,
                        embedding_dim=embedding_dim, rnn_units=rnn_units, batch_size=1)
    model_file = find_model(filename=model_name)
    # model = load_weights(model, model_file)
    model.load_weights(model_file)
    model.build(tf.TensorShape([1, None]))

    # print(generate_text(model, start_string=u"ROMEO: ",num_generate=2000, temperature=0.8))
    return generate_text(model, start_string, num_generate=num_generate, temperature=temp)


def model_Shakespeare(start_string, num_generate, temp):
    # load using cache
    # get the text with params
    # then send back the results
    return GenerateFromStart(model_name="shakespeare", start_string=start_string, num_generate=num_generate, temp=temp)


def predictor_page():
    # this page will be responsible for dealing with the predictions

    # decorations
    html_temp = """
    <div style="background-color:#000000;padding:10px">
    <h2 style="color:white;text-align:center;"><b>Artificial Intelligence-based Text Generator</b></h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.markdown("""<br>""", unsafe_allow_html=True)

    MODELS = {"Shakespeare": model_Shakespeare, "Harry Potter": model_Shakespeare,
              "Robert Frost": model_Shakespeare}
    # allow choice of models
    # print(MODELS.keys())
    option = st.selectbox(
        'Choose a Text Generation Model:', list(MODELS.keys()))
    current_model = MODELS[option]

    random_text_string = "Hello World"
    # warming up the model

    results = current_model(
        start_string=random_text_string, num_generate=100, temp=0.5)
    # run the model load functions here:

    # create text input
    text_label = "Starting Input Text"
    filled_text = "Enter your text here"
    ip = st.text_input(text_label, filled_text)  # , height=600 not merged yet
    num_generate = st.slider(label='Number of Words :', min_value=100,
                             max_value=10000, value=500, step=100)
    st.markdown("##### The output text is generated within this word limit.")
    temp = st.slider(label='Temperature :', min_value=0.0,
                     max_value=3.0, value=0.8, step=0.1)
    st.markdown("##### Higher temperatures generate more unpredictable text.")
    # 👈 this is a widget
    show_preds = False
    # print(ip)

    show_preds = False if ((ip == filled_text) or (ip == "")) else True
    # print(show_preds)

    rm = """
    # for instant predictions or lazy predictions
    # perform predictions instantly or wait for user to press a button
    inst = st.checkbox("Instantaneous Predictions", True)
    if inst is False:
        preds=st.button("Predict")
    """

    # show results
    if (show_preds == True):
        results = current_model(
            start_string=ip, num_generate=num_generate, temp=temp)
        # st.success('Generated Text : \n{}'.format(results))
        st.success("Generated Text :")
        st.success(results)
        coded_string = ip+str(num_generate)+str(temp)+results
        hashcode = get_SHA1(coded_string)
        # save results to database
        data = dict()
        data["HashCode"] = hashcode
        data["Input_String"] = ip
        data["Number_Generate"] = num_generate
        data["Temperature"] = temp
        data["Results"] = results
        print(data)
        connection = sqlite3.connect("TextGenData.db")
        cursor = connection.cursor()
        print("Writing results to database")
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS TextGenDataset (HashCode, Input_String, Number_Generate,Temperature, Results)""")
        command = """INSERT INTO TextGenDataset (HashCode, Input_String, Number_Generate,Temperature, Results)
              VALUES (?, ?, ?, ?, ?);"""
        tuple_to_insert = (hashcode, ip, num_generate, temp, results)
        cursor.execute(command, tuple_to_insert)
        connection.commit()
        connection.close()
        print("Done Writing results to database")
        trash = """
        latest_iteration = st.empty()
        bar = st.progress(0)
        for i in range(positivity_scale):
            latest_iteration.text(f'Measured Positivity : {i+1}')
            bar.progress(i + 1)
        """
        st.balloons()

    # st.write("Note: High Complexity/Long Text Inputs may be computationally expensive and might lead to delayed processes & performance issues.")
    st.markdown(
        "### Made with ❤️ by Farhan Khan & Team©. All copyrights reserved.")
    st.markdown("##### Note : Higher Values for Number of Words & Temperature required increased computational CPU processing and might cause in delayed results.")


def about_page():
    # the about the app page with aims & contributors
    print("Hello World!")
    # st.text("hello world")
    components.html(
        """
    <div style="background-color:#ff0055;padding:10px">
    <h1 style="color:white;text-align:center;">About the Project</h1>
    </div>
    
    """
    )
    img_top = """<center><img src="https://i.imgur.com/yOS7IGv.png" width="700px"></center>"""
    st.markdown(img_top, unsafe_allow_html=True)
    topic = """
    
    <br>
    
    The main motive of this project is to predict the amount of area that can get 
    burned in a forest fire based on some parameters like `Humidity(RH)`, `Wind(wind)`,`Rain(rain)`, 
    `Temperature(temp)` etc. 
    
    The project is a part of Hacktoberfest contribution and it has been initiated by <a href="https://github.com/dsc-iem">DSC-IEM</a> .
    We used different Model Building techniques for building the model and did an in-depth exploratory analysis 
    of the provided data. And except these things, creating a user-friendly web-app and deploying it in cloud is 
    also an integral part of a Data Science life cycle. So, we also have put together this web-app to show that.
    
    <p style="color:blue;">If you liked this project then it will be really motivating for us if you can star our repository😄.</p>
     
    
    <br>
    
    [![ReadMe Card](https://github-readme-stats.vercel.app/api/pin/?username=khanfarhan10&repo=TextGeneration&theme=dark)](https://github.com/khanfarhan10/TextGeneration)

    """

    st.markdown(topic, unsafe_allow_html=True)


def collaborator_page():
    st.markdown("Hello world! ")


def sidebar_nav():
    # top image for DSC-IEM
    html_img = """<center><img src="https://i.imgur.com/mx9aCum.png" width="300px" ></center>"""
    st.sidebar.markdown(html_img, unsafe_allow_html=True)
    # https://i.ibb.co/VY5wCkN/47480912-png.png
    # height="130px"

    # NAV BAR
    st.sidebar.markdown("""## Navigation Bar: <br> """, unsafe_allow_html=True)
    st.markdown("""<br><br>""", unsafe_allow_html=True)
    current_page = st.sidebar.radio(
        " ", ["Predictions",  "Project Collaborators", "About"])

    # st.markdown("""<br></br> <br>""",unsafe_allow_html=True)
    sidetext = """
    <br><br><br><br><br>Thank you for visiting this website🤗.  
    We contribute towards open source :  
    Feel free to visit [our github repository](https://github.com/khanfarhan10/TextSentimentAnalysis)
    """

    st.sidebar.markdown(sidetext, unsafe_allow_html=True)

    all_pages = {"Predictions": predictor_page,
                 "Project Collaborators": collaborator_page, "About": about_page}
    # predictor_page()

    func = all_pages[current_page]
    func()


ROOT_DIRECTORY = os.getcwd()
sidebar_nav()

# TODO CLEAN OUTPUT TEXT - GRAMMAR AND SPELLING

# TODO CLEAN CODING
