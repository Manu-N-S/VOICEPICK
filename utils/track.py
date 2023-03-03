import subprocess
import speech_recognition
import pyttsx3

apple = "python detect.py --weights yolov5s.pt --source 0 --class 47 "
orange = "python detect.py --weights yolov5s.pt --source 0 --class 49 "
banana = "python detect.py --weights yolov5s.pt --source 0 --class 46 "
bottle = "python detect.py --weights yolov5s.pt --source 0 --class 39 "
sandwich = "python detect.py --weights yolov5s.pt --source 0 --class 48 "
cellphone = "python detect.py --weights yolov5s.pt --source 0 --class 67 "
cup = "python detect.py --weights yolov5s.pt --source 0 --class 41 "
mouse = "python detect.py --weights yolov5s.pt --source 0 --class 64 "
remote = "python detect.py --weights yolov5s.pt --source 0 --class 65 "
cake = "python detect.py --weights yolov5s.pt --source 0 --class 55 "
default = "python detect.py --weights yolov5s.pt --source 0 "



def check_for_class(text):
    if text is "":
        return default
    if "apple"or "Apple" in text:
        print("INITIALISING WITH APPLE.... ")
        return apple
    if "orange" or "Orange" in text:
        print("INITIALISING WITH ORANGE.... ")
        return orange
    if "banana" or "Banana" in text:
        print("INITIALISING WITH BANANA.... ")
        return banana
    if "bottle" or "Bottle" in text:
        print("INITIALISING WITH BOTTLE.... ")
        return bottle
    if "sandwich" or "Sandwich" in text:
        print("INITIALISING WITH SANDWICH.... ")
        return sandwich
    if "cellphone" or "Cellphone" in text:
        print("INITIALISING WITH CELLPHONE.... ")
        return cellphone
    if "cup" or "Cup" in text:
        print("INITIALISING WITH CUP.... ")
        return cup
    if "mouse" or "Mouse" in text:
        print("INITIALISING WITH MOUSE.... ")
        return mouse
    if "remote" or "Remote" in text:
        print("INITIALISING WITH REMOTE.... ")
        return remote
    if "cake" or "Cake" in text:
        print("INITIALISING WITH CAKE.... ")
        return cake
    else:
        return 0

recognizer = speech_recognition.Recognizer()

try:
    with speech_recognition.Microphone() as mic:
        print("START SPEAKING.......")
        recognizer.adjust_for_ambient_noise(mic,duration=5)
        audio =recognizer.listen(mic)

        text = recognizer.recognize_google(audio)
        text=text.lower()

        print(f"Recognized {text}")
except speech_recognition.UnknownValueError():
    recognizer = speech_recognition.Recognizer()



command = check_for_class(text)

process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
print(output.decode())