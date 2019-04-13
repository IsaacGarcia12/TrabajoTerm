import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('A ver hablale: ')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print('Dijiste: {}'.format(text))
    except:
        print('Perdon no pude reconocer lo que me dijiste')