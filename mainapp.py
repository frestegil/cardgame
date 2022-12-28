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
	st.button('New word', on_click=new_word_click, args=(selectedWords, 30,)):


def new_word_click(words, timer):
	word = words.sample(n=1)['mot'].values[0]
	st.write(f'# {word}')
	st.write(f'{timer}')