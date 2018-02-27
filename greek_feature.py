import os
import sys
from cltk.tokenize.sentence import TokenizeSentence
from cltk.tokenize.word import WordTokenizer
from cltk.stem.lemma import LemmaReplacer

class Features:
	def freq_interrogatives(file):
		file = TokenizeSentence("greek").tokenize_sentences(file)
		num_interrogative = 0

		for line in file:
			num_interrogative += line.count(";")

		return num_interrogative / len(file)

	def freq_conditional_characters(file):
		file = WordTokenizer('greek').tokenize(file)
		num_conditional_characters = 0
		num_characters = 0

		for word in file:
			num_conditional_characters += len(word) if word == "εἲ" or word == "ἐάν" or word == "εἰ" else 0 #Accent should be acute?
			num_characters += len(word)

		return num_conditional_characters / num_characters

	def freq_personal_pronouns(file):
		file = LemmaReplacer('greek').lemmatize(file)
		num_pronouns = 0
		num_characters = 0

		for word in file:
			num_pronouns += len(word) if word == "ἐγώ" or word == "ἐμέω" or word == "σύ" or word == "σεύω" else 0
			num_characters += len(word)

		return num_pronouns / num_characters

	def freq_demonstrative(file):
		file = LemmaReplacer('greek').lemmatize(file)
		num_demonstratives = 0
		num_characters = 0

		for word in file:
			num_demonstratives += len(word) if word == 'ἐκεῖνος' or word == 'αὕται' or word == 'οὗτος' or word == 'τόδε' \
			or word == 'τάδε' or word == 'ἐκείνᾱς' or word == 'τάσσω' or word == 'ταύτᾱς' or word == 'ὅδε' else 0
			num_characters += len(word)

		return num_demonstratives / num_characters

	def freq_indefinite_pronoun_in_non_interrogative_sentence(file):
		# Extremely time consuming
		# file = TokenizeSentence("greek").tokenize_sentences(file)
		# num_pronouns = 0
		# num_characters = 0
		# for line in file:
			# line = LemmaReplacer('greek').lemmatize(line)
			# if ';' not in line:
			# 	for word in line:
			# 		num_pronouns += len(word) if word == 'τις' else 0
			# 		num_characters += len(word)

		#TODO Need to check for interrogatives
		file = LemmaReplacer('greek').lemmatize(file)
		num_pronouns = 0
		num_characters = 0

		for word in file:
			num_pronouns += len(word) if word == 'τις' else 0
			num_characters += len(word)

		return num_pronouns / num_characters

	def freq_allos(file):
		file = LemmaReplacer('greek').lemmatize(file)
		num_allos = 0
		num_characters = 0

		for word in file:
			num_allos += len(word) if word == 'ἄλλος' or word == 'ἄλλᾱς' else 0
			num_characters += len(word)

		return num_allos / num_characters

	def freq_autos(file):
		file = LemmaReplacer('greek').lemmatize(file)
		num_autos = 0
		num_characters = 0

		for word in file:
			num_autos += len(word) if word == 'αὐτός' or word == 'αὐτᾱς' else 0
			num_characters += len(word)

		return num_autos / num_characters

	def freq_reflexive(file):
		file = LemmaReplacer('greek').lemmatize(file)
		num_reflexive = 0
		num_characters = 0

		for word in file:
			num_reflexive += len(word) if word == 'ἐμαυτοῦ' or word == 'σαυτοῦ' or word == 'ἑαυτοῦ' else 0
			num_characters += len(word)

		return num_reflexive / num_characters

	def freq_vocative_sentences(file):
		file = TokenizeSentence("greek").tokenize_sentences(file)
		num_vocative = 0

		for line in file:
			num_vocative += 1 if 'ὦ' in line else 0

		return num_vocative / len(file)

	def freq_superlative(file):
		file = WordTokenizer('greek').tokenize(file)
		num_superlative = 0
		num_characters = 0

		for word in file:
			num_superlative += len(word) if word.endswith(('τατος', 'τάτου', 'τάτῳ', 'τατον', 'τατοι', 'τάτων', \
				'τάτοις', 'τάτους', 'τάτη', 'τάτης', 'τάτῃ', 'τάτην', 'ταται', 'τάταις', 'τάτας', 'τατα')) else 0
			num_characters += len(word)

		return num_superlative / num_characters

	def freq_conjunction(file):
		file = WordTokenizer('greek').tokenize(file)
		num_conjunction = 0
		num_characters = 0

		for word in file:
			num_conjunction += len(word) if word in {'τε', 'καί', 'δέ', 'ἀλλά', 'καίτοι', 'οὐδέ', 'μηδέ', 'ἤ'} else 0
			num_characters += len(word)

		return num_conjunction / num_characters

	def mean_sentence_length(file):
		file = TokenizeSentence("greek").tokenize_sentences(file)
		lens = 0

		for line in file:
			lens += len(line)

		return lens / len(file)

	def non_interoggative_sentence_with_relative_clause(file):
		return 0

	def mean_length_relative_clause(file):
		return 0

	def relative_clause_per_sentence(file):
		#Count of relative pronouns in non-interrogative sentences / total non-interrogative sentences
		file = TokenizeSentence("greek").tokenize_sentences(file)
		num_relative_pronoun = 0
		num_non_interrogative_sentence = 0
		pronouns = {'ὅς', 'οὗ', 'ᾧ', 'ὅν', 'οἵ', 'ὧν', 'οἷς', 'οὕς', 'ἥ', 'ᾗς', 'ἥν', 'αἵ', 'αἷς', 'ἅς', 'ὅ', 'ἅ'}

		for line in file:
			if not line.endswith(';'): #TODO what if line ends in quote or bracket?
				for word in line.split():
					num_relative_pronoun += 1 if word in pronouns else 0
				num_non_interrogative_sentence += 1

		return num_relative_pronoun / num_non_interrogative_sentence

tesserae_clone_command = "git clone https://github.com/tesserae/tesserae.git"
greek_text_dir = "tesserae/texts/grc"

def main():
	global greek_text_dir

	#Associates files names to their respective features
	text_to_features = {}

	file_names = None
	if len(sys.argv) > 1:
		if sys.argv[1] == "debug": #if debug, just scan pre-selected corpus
			file_names = ["tesserae/texts/grc/polybius.histories.tess"]
		else: #Allows user to select custom path other than tesserae
			greek_text_dir = sys.argv[1]

	#Download corpus if non-existent
	if not os.path.isdir(greek_text_dir):
		print("Corpus at " + greek_text_dir + " does not exist - attempting to clone repository...")
		os.system(tesserae_clone_command)

	#Obtain all the files to parse by traversing through the directory
	if file_names is None:
		file_names = [current_path + os.sep + current_file_name for current_path, current_dir_names, current_file_names in \
		os.walk(greek_text_dir) for current_file_name in current_file_names if current_file_name.endswith(".tess")]

	#Feature extraction
	for file_name in file_names:
		text_to_features[file_name] = {}

		#Store each line of file in a list
		file_text = []
		with open(file_name, "r") as file:
			for line in file:
				#Ignore lines without tess tags, or parse the tag out and strip whitespace
				if not line.startswith("<"):
					continue
				assert ">" in line
				line = line[line.index(">") + 1:].strip()
				file_text.append(line)

		#Convert list of strings into a single string
		file_text = " ".join(file_text)

		#Invoke those values of the Feature class which are functions
		for feature in Features.__dict__.values():
			if callable(feature):
				score = feature(file_text)
				text_to_features[file_name][feature] = score
				print(file_name + ", " + str(feature) + ", " + str(score))

if __name__ == "__main__":
	main()
