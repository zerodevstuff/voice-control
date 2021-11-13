import speech_recognition
import mygui

recognizer = speech_recognition.Recognizer()
gui = mygui.gui_control()
print ("First Threshold:" + str(recognizer.energy_threshold))

with speech_recognition.Microphone() as src:
    while True:
        try:
            audio = recognizer.adjust_for_ambient_noise(src)
            print("\n\nThreshold After optimization:" + str(recognizer.energy_threshold))
            print("\nYou May Now Speak:")
            audio = recognizer.listen(src)
            text = recognizer.recognize_google(audio).lower()
        except Exception as ex:
            print("What Did You Say?\n\n")
            continue
            
        print("I Heard : " + text)

        if (text == "quit") or (text == "exit"):
        	break
        elif text == "mouse up" or text == "move up":
        	gui.mouse_up(recognizer, src)