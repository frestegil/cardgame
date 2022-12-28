import streamlit as st
import pandas as pd

st.title('Card game')
file = st.file_uploader('Select file to upload')
if file != '':
	df = pd.read_csv(file, sep=";")
	# st.write (df.head())
	levels = df.niveau.unique()
	checkboxes = [st.checkbox(l) for l in levels]
	levels = pd.DataFrame({"niveau":levels})
	selectedCheckboxes = [x for x, z in enumerate(checkboxes) if z == True] 
	selectedLevels = levels.iloc[selectedCheckboxes]
	selectedWords = df.merge(selectedLevels, on='niveau')
	# Play
	st.button('New word',
		on_click=selectplayer,
		args=(selectedWords.sample(n=1)['mot'].values[0],30,)):


def new_word_click(word, timer):
	st.write(f'# {word}')