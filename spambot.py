import pyautogui as tastatur
import time

try:
    print("8=================------------------{ AutoTyper }------------------=================8")
    text = input("Was willst du spammen lassen? (Benutze '/n' um eine neue Zeile zu beginnen!)\n> ")
    reps = abs(int(input("Wie oft soll die Nachricht wiederholt werden? (Ganzzahl)\n> ")))
    speed = float(input("Zeit zwischen Nachrichten? (t in s) (Punkt statt Komma)\n> "))
    print("8=================-------------------------------------------------=================8")
except Exception:
    print("Syntax Fehler!")
    input("Press any button to exit!")
    quit()

start = input("Start? Du hast 5 Sekunden bis zum Start! (y / n)\n>").lower()
if start == "y":
    for i in range(-5, 0):
        print(-i)
        time.sleep(1)

    print("LEZ GO")

    for i in range(reps):
        textArgs = text.split("/n")
        for textArg in textArgs:
            tastatur.typewrite(textArg)
            tastatur.press("enter")
        time.sleep(speed)
else:
    print("aight c ya")