""" chapter 4 case study (page129-131)
program: sentenceGenerator.py
3/5/2025

Application tht generates and displays sentences using simple grammar and vocabulary. words are chosen at random, each small tak will be its own function and  user wwill enter the number of sentences to generate.
"""

import random

#Global variables containing the different part of speech that all functions can use.
articles = ("A", "THE", "AN")

nouns = ("BOY", "GIRL", "BAT","BALL","DOG", "CAT", "TURTLE", "ROCK", "PIZZA", "ABRAHAM LINCOLN", "MAZDA", "TABLE", "LAPTOP" )
verbs = ("HIT" , "SAW", "LIKED", "JUMPED", "SNEEZED","RAN", "FELL", "TYPED","SLAPPED")
prepositions=("WITH","BY", "FROM","AT","TO", "UNDER", "AROUND")

#definition of the sentence() function
def sentence():
	"""Builds and returns a sentence."""
	return nounPhrase() + " " + verbPhrase()
# Definition of the nounPhrase() function
def nounPhrase():
	"""BUilds and returns a noun phrase."""
	return random.choice(articles) + " " + random.choice(nouns)
# Definition of the verbPhrase() function
def verbPhrase():
	"""Builds and returns a verb phrase. """
	return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()
#definition of the prepositionalPhrase() function
def prepositionalPhrase():
	""" Builds and returns a prepositional phrase."""
	return random.choice(prepositions) + " " + nounPhrase()
#definition of the main() function
def main():
	"""Allows the user to input the number of the sentences."""
	number = int(input("Please enter a number of sentence: >>"))
	for count in range(number):
		print(sentence())
	input("\nSentences complete, press ENTER to exit..")

# global call to msin() for program to execute
if __name__ == '__main__':
	main()

