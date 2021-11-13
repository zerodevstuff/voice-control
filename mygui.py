import pyautogui

speedy=150
slower=20

class gui_control:
	def __init__(self):
		pyautogui.PAUSE = 1
		pyautogui.FAILSAFE = True
		pyautogui.size()

		def mouse_up(self,recognizer, src):
			while True:
				text = ""
				pyautogui.moveRel(0, -1*slower,duration=0.25)
				try:
					audio = recognizer.listen(src)
					text = recognizer.recognize_google(audio).lower()
				except:
					pass
					print("mouse up : " + text)
					if text == "stop":
						break
					elif text == "faster":
						pyautogui.moveRel(0, -1*speedy, duration=0.25)
					elif text == "slower":
						pyautogui.moveRel(0, -1*slower, duration=0.25)