import json
import nltk
import numpy as np
from nltk.stem import PorterStemmer

nltk.download('punkt_tab', quiet=True)

stemmer = PorterStemmer()

def preprocess_data(file_path):
	with open(file_path, 'r') as file:
		data = json.load(file)

		words = []
		labels = []
		training_data = []

		for intent in data['intents']:
			for pattern in intent['patterns']:
				tokens = nltk.word_tokenize(pattern)
				words.extend(tokens)
				training_data.append((tokens, intent['tag']))

			if intent['tag'] not in labels:
				labels.append(intent['tag'])

		words = sorted(set([stemmer.stem(w.lower()) for w in words if w not in ['?', '!', '.', ',']]))
		labels = sorted(labels)

		return words, labels, training_data
