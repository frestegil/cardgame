import streamlit as st
import pandas as pd

st.title('Card game')
file = st.file_uploader('Select file to upload')
df = pd.DataFrame({"caterogie": [], "niveau": [], "mot":[]})
if file != '':
	df = pd.read_csv(file, sep=";")
	# st.write (df.head())
levels = df.niveau.unique()
checkboxes = [st.checkbox(l) for l in levels]

selectedCheckboxes = [x for x, z in enumerate(checkboxes) if z == True] 
st.write(selectedCheckboxes)
selectedLevels = levels.iloc[selectedCheckboxes]
selectedWords = df.loc[df['niveau'].isin(selectedLevels),:]
st.write(selectedWords)

