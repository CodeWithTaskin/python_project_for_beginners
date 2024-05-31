import datetime as dt
from time import sleep
from playsound import playsound


Time = int(input("Enter your alarm time(hour): "))
Time2 = int(input("Enter your alarm time(minite): "))
AMorPM = input("AM or PM? : ")
if Time < 10:
    alarmTime = (f"0{Time}:{Time2}{AMorPM.upper()}")
else:
    alarmTime = (f"{Time}:{Time2}{AMorPM.upper()}")

while True:
    now=dt.datetime.now()
    t = now.strftime("%I:%M%p")
    if  t == alarmTime :
        print("Weak up!!!!")
        playsound('E:/python_project/python_project_for_beginners/Simple Alarm Clock/alarm-clock-short-6402.mp3')
        break
        
