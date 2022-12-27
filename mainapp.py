import streamlit as st
import pandas as pd

st.title('Card game')
file = st.upload('Select file to upload')
df = pd.read_csv(file, sep=";")
st.write (df.head())