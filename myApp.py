import streamlit as st

import pandas as pd

'''
# This is the document title
This is some _markdown_.
'''

df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
df

x = 10
x


import matplotlib.pyplot as plt 
import numpy as np

arr = np.random.normal(1, 1, size=100)

fig, ax = plt.subplots()

ax.hist(arr, bins=20)

fig

# import streamlit as st
# import streamlit.components.v1 as components

# name = st.text_input('Name')

# if not name:
#     st.warning('Please input a name.')
#     st.stop()

# st.success('Thank you for inputting a name.')

with st.form("my_form", clear_on_submit=True):
    st.write("Inside the form")
    first_name = st.text_input('First Name')
    last_name = st.text_input('Last Name')
    
    slider_val = st.slider("Form Slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)
st.write("Outside the form")

# df_1 = pd.DataFrame(np.random.randn(1000, 2) / [50, 50]+[37.76, -122,4], columns =['lat', 'lon'])

# st.map(df_1)

import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO

df = pd.DataFrame(
     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
     columns=['lat', 'lon'])

st.map(df)

uploaded_file = st.file_uploader("Choose a file")
# if uploaded_file is not None:

#     bytes_data = uploaded_file.getvalue()
#     st.write(bytes_data)

#     # stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
#     # st.write(stringio)

#     # string_data = stringio.read()
#     # st.write(string_data)

#     dataframe = pd.read_csv(uploaded_file)
#     st.write(dataframe)


# from PIL import Image
# img_file_buffer = st.camera_input("Take a picture")

# if img_file_buffer is not None:
#     # Reading image file buffer as PIL Image
#     img = Image.open(img_file_buffer)

#     # Converting PIL image to numpy array
#     img_array = np.array(img)

#     st.write(img_array.shape)

# st.download_button(
#     label = "Download the image",
#     data=img_file_buffer,
#     file_name = "download_file.jpeg",
#     mime='jpeg'
# )

camera_on = st.checkbox("Click, to switch on Camera")
while camera_on:
    picture = st.camera_input("Take a picture")

    if picture:
        st.image(picture)

