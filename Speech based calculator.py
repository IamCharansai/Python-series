import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(" Speak now...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print(" You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand.")
        return ""
    except sr.RequestError:
        speak("Service unavailable.")
        return ""

def calculate(command):
    if "add" in command:
        nums = [int(s) for s in command.split() if s.isdigit()]
        result = sum(nums)
    elif "subtract" in command:
        nums = [int(s) for s in command.split() if s.isdigit()]
        result = nums[0] - nums[1]
    elif "multiply" in command:
        nums = [int(s) for s in command.split() if s.isdigit()]
        result = nums[0] * nums[1]
    elif "divide" in command:
        nums = [int(s) for s in command.split() if s.isdigit()]
        if nums[1] != 0:
            result = nums[0] / nums[1]
        else:
            speak("Cannot divide by zero.")
            return
    else:
        speak("Sorry, I can't process that.")
        return
    speak(f"The result is {result}")
    print(" Result:", result)

speak("Welcome to voice calculator. Please say your operation.")
query = get_audio()
if query:
    calculate(query)
