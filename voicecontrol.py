import speech_recognition

recognizer = speech_recognition.Recognizer()

with speech_recognition.Microphone() as src:
	try:
		audio = recognizer.adjust_for_ambient_noise(src)
		print("threshold:" + str(recognizer.energy_threshold))
		print("you may now speak:")
		audio = recognizer.listen(src)
		speech_to_txt = recognizer.recognize_google(audio).lower()
		print(speech_to_txt)
	except Exception as ex:
		print("didnt Recognize voice input")
		