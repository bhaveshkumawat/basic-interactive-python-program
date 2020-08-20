import pyttsx3
import os

pyttsx3.speak("Welcome to my ,  Basic tools program ! ")


while True:
	print("chat with me with your requirements : "  , end='')
	p = input()
	p.lower()




	if ("dont" in p) or ("no" in p):
	  continue

	elif (("run" in p) or  ("execute" in p ) or ("open" in p) or ("surf" in p) or ("access" in p))  and  (("chrome" in p) or ("internet" in p) or ("web" in p)):
		pyttsx3.speak("opening chrome")
		os.system("chrome")

	elif (("run" in p) or  ("execute" in p ) or ("open" in p)) and  (("notepad" in p) or ("editor" in p) or ("write" in p) ) :
		pyttsx3.speak("opening notepad for you")
		os.system("notepad")

	elif ("exit" in p) or ("quit" in p) or ("close" in p) or ("stop" in p):
		pyttsx3.speak("Thanks for , choosing my services.")
		break

	elif (("run" in p) or  ("execute" in p ) or ("open" in p)) and  (("paint" in p) or ("draw" in p) or ("figure" in p)):
		pyttsx3.speak("opening paint for you")
		os.system("mspaint")

	elif (("run" in p) or ("open" in p))  and (("player" in p) or ("play" in p))  and (("media" in p) or ("video" in p) or ("music" in p)):
		pyttsx3.speak("opening media player")
		os.system("wmplayer")

	elif (("change" in p) or ("computer" in p) or ("open" in p) or ("access" in p)) and (("settings in p") or ("control panel" in p) ):
		pyttsx3.speak("opening program for your purpose")
		os.system("control panel")

	elif (("run" in p) or  ("start" in p ) or ("open" in p) or ("record" in p)) and  (("recording" in p)  or ("screen" in p) ) :
		pyttsx3.speak("Here you go for Screen recording")
		os.system("psr")

	elif (("take" in p) or ("capture" in p) or ("snipping")) and  (("screen" in p) or ("screenshot" in p) or ("tool" in p)):
		pyttsx3.speak("here you Go for Screen shot")
		os.system("SnippingTool")

	else:
		pyttsx3.speak("I didn't get your ,requirements.")
		print("Please specify your requirement  clearly.")
