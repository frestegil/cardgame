import streamlit as st
import pandas as pd
import time



def new_word_click(words, timer):
	st.session_state.word=words.sample(n=1)['mot'].values[0]
	st.session_state.timer=timer
	


st.title('Card game')
file = st.file_uploader('Select file to upload')
if 'word' not in st.session_state:
	st.session_state.word=''
if file != '':
	df = pd.read_csv(file, sep=";")
	# st.write (df.head())
	levels = df.niveau.unique()
	checkboxes = [st.checkbox(l) for l in levels]
	levels = pd.DataFrame({"niveau":levels})
	selectedCheckboxes = [x for x, z in enumerate(checkboxes) if z == True] 
	selectedLevels = levels.iloc[selectedCheckboxes]
	selectedWords = df.merge(selectedLevels, on='niveau')
	timer = st.slider("Select a timer",5, 30)
	# Play
	st.button('New word', on_click = new_word_click, args = (selectedWords, timer))
	st.markdown(f'# {st.session_state.word}')
	for x in range(st.session_state.timer, 0, -1):
		st.write(f'{x}')
		time.sleep(1)
	st.session_state.word = ""