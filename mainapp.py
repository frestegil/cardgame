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
print()
if selectedWords.shape[0] > 0:
	nbWords = 1
	if st.button('Display a word'):
		if nbWords < selectedWords.shape[0]:
			st.write(selectedWords.iloc['mot', nbWords])
			nbWords = nbWords + 1
		else:
			st.write('No more words')
else:
	st.write('No words selected')