import streamlit as st
import pandas as pd

st.title("Data Science and AI Batch 05")
name = st.text_input("Enter you name:")
if name:
    st.write(f"Hello {name} !!! Welcome, to our AI class.")

age = st.slider("Select your age:", 0, 100, 23)
st.write(f"{name} Do remember that your age is {age}.")
options=['Python', 'Java', 'JavaScript', 'c++']
choice=st.selectbox("Choose your favourite language", options)
st.write(f"You selected {choice}") 

data={
    "Name":["jack", "john", "jamie", "jill"],
    "age":[12, 54, 65, 32],
    "city":["tokyo", "koyoto", "hamamastu", "hiroshima"],
}

df=pd.DataFrame(data)

df.to_csv("sampledata.csv")

st.write(df)
uploaded_file=st.file_uploader("Choose a csv file", type="csv")
if uploaded_file is not None:
    df= pd.read_csv(uploaded_file)
    st.write(df)




