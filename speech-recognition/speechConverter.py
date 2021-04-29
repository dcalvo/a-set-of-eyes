# Python program to translate
# speech to text and text to speech

import speech_recognition as sr
import pyttsx3

from difflib import SequenceMatcher

import webbrowser
import requests
import keyboard

# reference: https://www.geeksforgeeks.org/python-convert-speech-to-text-and-text-to-speech/
def SpeakText(command):
	''' Text-to-speech function '''
	
	# Initialize the engine
	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()
	print(command)

# reference: https://www.geeksforgeeks.org/python-convert-speech-to-text-and-text-to-speech/
def get_user_audio_and_convert_to_text(r, source2):
	''' Speech-to-text function '''

	# wait for a second to let the recognizer
	# adjust the energy threshold based on
	# the surrounding noise level
	r.adjust_for_ambient_noise(source2, duration=0.2)

	#listens for the user's input
	audio2 = r.listen(source2)

	# Using google to recognize audio
	MyText = r.recognize_google(audio2)
	MyText = MyText.lower()

	print(MyText)
	return MyText

# Find out what website the user wants to go to
def get_desired_website(r):
	''' Ask the user what website they want to go to.

		Returns:
			website_to_go_to: the textual representation of the website
				the user said they wanted to go to.
	'''

	while(1):	
	
		# Exception handling to handle exceptions at the runtime
		try:
		
			# use the microphone as source for input.
			with sr.Microphone() as source2:
				text_to_speak = "Please say the name of the website that you would like to go to"
				SpeakText(text_to_speak)

				website_to_go_to = get_user_audio_and_convert_to_text(r, source2)

				text_to_speak = "Did you say you want to go to: " + website_to_go_to + "?"
				SpeakText(text_to_speak)

				verifying_website = get_user_audio_and_convert_to_text(r, source2)
				if (verifying_website == "yes"):
					return website_to_go_to

		except sr.RequestError as e:
			print("Could not request results; {0}".format(e))
		
		except sr.UnknownValueError:
			print("unknown error occured")

def get_best_match_websites(popular_websites, spoken_website_name):
	''' Returns the URL of the popular website that the user most likely said. '''

	best_pop_website_match_score = -1
	best_pop_website_url_match = ""

	for curr_pop_website in popular_websites.keys():
		curr_match_score = SequenceMatcher(None, curr_pop_website, spoken_website_name).ratio()
		if best_pop_website_match_score == -1 or best_pop_website_match_score < curr_match_score:
			best_pop_website_match_score = curr_match_score
			best_pop_website_url_match = popular_websites[curr_pop_website]
	return best_pop_website_url_match

#helper function for NVDA mapping of commands
def get_speech_mappings(text_file):
	''' takes a text file of mappings and converts to an actual mapping.
		Returns:
			a dictionary
	'''
	m = {}
	with open(text_file, "r", encoding='utf-8') as mapping:
		lst = mapping.readlines()
		for ls in lst:
			if ls == '\n':
				continue
			keys_and_commands = ls.split(":")
			key = keys_and_commands[0]
			command_keywords = keys_and_commands[1].split(",")
			m[key] = command_keywords

	return m

# now that we have a mapping of all the commands, 
# we can simply say that if the text corresponds to a command set
# we execute the mapping NVDA command
# 
def map_command(mappings, text):
	# discern the best guess of what the text is asking for based on 
	# the highest similarity score
	best_score = -1
	best_command = ""
	# Remove "asoe" from text
	text = text.split(' ', 1)[1]
	for curr_mapping in mappings:
		set_of_commands = mappings[curr_mapping]
		for command in set_of_commands:
			curr_score = SequenceMatcher(None, text, command).ratio()
			if best_score == -1 or best_score < curr_score:
				best_score = curr_score
				best_command = curr_mapping
	
	return best_command


# General Function to return if strings are similar
def similarStrings(potential_command, text):
	score = SequenceMatcher(None, potential_command, text).ratio()
	if score > 0:
		return True
	return False


# Execute the keyboard command
def execute_command(command):
	print("Executing " + command)
	if (command == ""):
		return
	keyboard.send(command)


def main():
	# Initialize the recognizer and command mappings
	r = sr.Recognizer()
	m = get_speech_mappings('mapingOtherNVDACommands.txt')

	# get the website tha the user wants to go to
	# website_to_go_to = get_desired_website(r)

	# Notify user ASOE is listening
	SpeakText("ASOE is on, and listening. To perform a command say ASOE followed by the command. Say quit to quit ASOE.")
	with sr.Microphone() as source2:
		while True:
			potential_command = get_user_audio_and_convert_to_text(r, source2)
			if similarStrings(potential_command, "asoe"):
				# Execute commands beginning with ASOEQ
				execute_command(map_command(m, potential_command))
			else:
				if similarStrings(potential_command, "quit"):
					SpeakText("Quitting")
					return

	# use string similarity techniques to determine which website URL the user meant
	# popular_websites = {
	# 	"the new york times" : "https://www.nytimes.com/",
	# 	"netflix": "https://www.netflix.com/",
	# 	"google": "https://www.google.com/"}
	# website_url = get_best_match_websites(popular_websites, website_to_go_to)

	# text_to_speak = "Going to " + website_url
	# SpeakText(text_to_speak)

	# # go to the best-match website
	# webbrowser.open(website_url)

	# # GET request to get the HTML code of the website
	# r = requests.get(website_url)
	# # #with a session
	# # cd = { 'sessionid': '123..'}
	# # r = requests.get(url, cookies=cd)

	# ##print(r.content)
	# #print(r.text)
	
	# # save HTML code in example.html file (in current working directory)
	# file = open('example.html', 'w')
	# file.write(r.text)
	# file.close()
	# print("Saved html source code for " + website_url + " in example.html")

if __name__ == "__main__":
	main()
