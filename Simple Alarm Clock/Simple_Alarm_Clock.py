import datetime as dt
from playsound import playsound


Time = int(input("Enter your alarm time(hour): "))
Time2 = int(input("Enter your alarm time(minite): "))
AMorPM = input("AM or PM? : ")
alarmTime = (f"{Time}:{Time2}{AMorPM.upper()}")

while True:
    now=dt.datetime.now()
    t = now.strftime("%H:%M%p")
    if t == alarmTime:
        print("Weak up!!!!")
        playsound('E:/python_project/python_project_for_beginners/Simple Alarm Clock/alarm-clock-short-6402.mp3')
        break
        






