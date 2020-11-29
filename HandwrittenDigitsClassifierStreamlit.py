# streamlit run HandwrittenDigitsClassifierStreamlit.py

from streamlit_drawable_canvas import st_canvas
import streamlit as st
import pandas as pd
import numpy as np
import sklearn
import pickle

from sklearn.svm import SVC  # import Support Vector Classifier
# Imports PIL module
from PIL import Image

import warnings
warnings.filterwarnings("ignore")

st.title('Handwritten Digit Classifier')

st.subheader("using t-SNE and Streamlit")


st.title('Drawable Canvas First')

# Basic 28*28 frame to get back an image from
# Specify canvas parameters in application
stroke_width = 10
stroke_color = "#000000"
bg_color = "#ffffff"

dirt2 = """
bg_image = st.sidebar.file_uploader("Background image:", type=["png", "jpg"])
drawing_mode = st.sidebar.selectbox(
    "Drawing tool:", ("freedraw", "line", "rect", "circle", "transform")
)
realtime_update = st.sidebar.checkbox("Update in realtime", True)
"""
bg_image = False
drawing_mode = "freedraw"
realtime_update = True

# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color="" if bg_image else bg_color,
    background_image=Image.open(bg_image) if bg_image else None,
    update_streamlit=realtime_update,
    height=200, width=200,
    drawing_mode=drawing_mode,
    key="canvas",
)

# print(canvas_result.image_data)

data = canvas_result.image_data


def equal_array(a):
    """Returns True if the array is same throughout"""
    b = np.full(a.shape, a.max())
    # print(b)
    return np.array_equal(a, b)


@st.cache()
def load_model():
    filename = 'non_linear_svc.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    return loaded_model


get_preds = False
svc = load_model()

# or (not equal_array(data))
if data is not None:
    numpy_img = data

    # print(data.max())
    img = numpy_img.squeeze().astype(np.uint8)

    PIL_image = Image.fromarray(img).convert('RGB').convert('L')

    img_reshaped = np.array(PIL_image.resize((28, 28)))
    img_reshaped = img_reshaped.flatten()
    img_reshaped = img_reshaped.reshape(1, 784)
    # print(img_reshaped.shape)
    PIL_image.save('Input.png')

    img_reshaped = Image.open("Input.png").convert('L')
    img_reshaped = np.array(img_reshaped.resize(
        (28, 28))).flatten().reshape(1, 784)
    print(img_reshaped.shape)

    if not equal_array(data):
        get_preds = True


# print(sklearn.__version__) # 0.22.1

if get_preds == True:
    svc = load_model()

    confidence = int(100*np.random.rand())

    y_pred = svc.predict(img_reshaped)
    print(y_pred)
    results = y_pred[0]
    st.header("Predicted : " + str(results))

    # st.header("Confidence = "+str(confidence)+" % ")

    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)
    for i in range(confidence):
        latest_iteration.text(f'Confidence : {i+1}')
        bar.progress(i + 1)


z = """
if canvas_result.image_data is not None:
    st.image(canvas_result.image_data)
"""
# print(type(canvas_result.image_data))
# Do something interesting with the image data and paths
# wait till I hit the predict button

y = """
if canvas_result.image_data is not None:
    st.image(canvas_result.image_data)  # numpy array
if canvas_result.json_data is not None:
    st.dataframe(pd.json_normalize(canvas_result.json_data["objects"]))
"""
