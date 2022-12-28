import streamlit as st
import pandas as pd
import time



def new_word_click(words, timer):
	st.session_state.word=words.sample(n=1)['mot'].values[0]
	st.session_state.timer=timer
	st.session_state.remainingTime=timer


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
	timer = st.slider("Select a timer",5, 60)
	# Play
	st.button('New word', on_click = new_word_click, args = (selectedWords, timer))
	st.info(f'{st.session_state.word}')
	st.write('Remaining time')
	my_bar = st.progress(100)
	for percent_complete in range(st.session_state.timer):
		time.sleep(1)
		rem_time = (st.session_state.timer - percent_complete - 1)/st.session_state.timer
		my_bar.progress(rem_time)
	my_bar.progress(0)
	st.write('Time out')