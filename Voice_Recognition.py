import speech_recognition as sr
from datetime import date
from datetime import datetime

def main():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Speak now ! ")
        audio = r.listen(source)
    if 'date' in r.recognize_google(audio):
        dates = date.today()
        print(dates)
    elif 'time' in r.recognize_google(audio):
        now = datetime.now()

        print("now =", now)

        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print("date and time =", dt_string)
    else:
        pass


    try:
        print("You have said "+ r.recognize_google(audio))
        print("Audio recorder successfully \n")

    except Exception as e:
        print("Error : " + str(e))
if __name__ == "__main__":
    main()