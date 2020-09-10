import speech_recognition as uc

t = uc.Recognizer()
with uc.Microphone() as source:
    print("listining now :")
    audio = t.listen(source)

print(t.recognize_google(audio))    
