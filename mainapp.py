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
nbWords = st.number_input('Define number of words', format='%d')
if nbWords > selectedWords.shape[0]:
	st.error(f'The number of words must be under {selectedWords.shape[0]}')
else:
	nbClicks = 1
	words = selectedWords.sample(n=nbWords)
	if st.button('Display a word'):
		st.write(words.loc[nbClicks, 'mot'])
		nbClicks = nbClicks + 1
		if nbClicks == nbWords:
			st.write('No more words')