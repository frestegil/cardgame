import streamlit as st
import pandas as pd

st.title('Card game')
file = st.file_uploader('Select file to upload')
df = pd.DataFrame({"caterogie": [], "niveau": [], "mot":[]})
if file != '':
	df = pd.read_csv(file, sep=";")
	st.write (df.head())
levels = df.niveau.unique()
x = [st.checkbox(levels)]
filtered_words = df.loc[df['niveau'].isin(x),:]
st.write(filtered_words)