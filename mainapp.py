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

selectedCheckboxes = [x for x, z in enumerate(lst) if z == true] 

st.write(selectedCheckboxes)
st.write(levels.iloc[:,selectedCheckboxes])


selectedLevels = levels.iloc[:,checkboxes]
filtered_words = df.loc[df['niveau'].isin([x for x in checkboxes if x = true]),:]
st.write(filtered_words)