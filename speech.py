import speech_recognition as shit
import pyaudio
r=shit.Recognizer()
with shit.Microphone() as f:
    print("Bolo ji ......")
    audio=r.listen(f)

try:
    text=r.recognize_google(audio)
    print("You said : ",text)
except r.UnknownError:
    print("Sorry")
except r.RequestError:
    print('Error 404')
if(text==)