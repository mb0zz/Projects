#!/usr/bin/env python3
import speech_recognition as sr

def start():
	running = True

	while(running):

		response = ""
		r = sr.Recognizer()
		with sr.Microphone() as source:
			print("Say something!")
			audio = r.listen(source)

		try:
			response = r.recognize_google(audio)
			#print("Google Speech Recognition thinks you said " + response)
		except sr.UnknownValueError:
			print("Google Speech Recognition could not understand audio")
		except sr.RequestError as e:
			print("Could not request results from Google Speech Recognition service; {0}".format(e))
			
			
		
			
		if "off" in response:
			running = False

start()