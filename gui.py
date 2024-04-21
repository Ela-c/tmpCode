import tkinter as tk
import tkinter.font as tkfont
# from gpiozero import LED
# import RPi.GPIO as GPIO

# GPIO.setmode(GPIO.BCM)

# hardware
# led = LED(14)

## GUI DEFINITIONS ##
mainWindow = tk.Tk()
mainWindow.title("LED Toggler")
myFont = tkfont.Font(family="Helvetica", size=12, weight="bold")

## EVENT FUNCTIONS ##


def ledToggle(btn: str, pin: int, pressed: bool):

    if pressed:
        v.set(0)
    # if led.is_lit:
    #     led.off()
    #     v.set(0)

    return print(f"{btn} button pressed")


def close():
    # turn led off
    # GPIO.cleanup()
    print("closing program")
    # exit program
    mainWindow.destroy()


### WIDGETS ###

v = tk.IntVar(mainWindow, 1)

noneBtn = tk.Radiobutton(mainWindow, indicatoron=0, value=0, text="None", font=myFont,
                         command=lambda: ledToggle(btn="none", pin=-1, pressed=False), bg="gray", width=24)

redBtn = tk.Radiobutton(mainWindow, indicatoron=0, value=1, text="Red", font=myFont,
                        command=lambda: ledToggle(btn="red", pin=2, pressed=v.get() == 1), bg="#ff0000", activebackground="#7a1712", width=24)
blueBtn = tk.Radiobutton(mainWindow, indicatoron=0, text="Blue", value=2, font=myFont,
                         command=lambda: ledToggle(btn="blue", pin=2, pressed=v.get() == 2), bg="#3944bc", activebackground="#0a1172", width=24)
greenBtn = tk.Radiobutton(mainWindow, indicatoron=0, text="Green", value=3, font=myFont,
                          command=lambda: ledToggle(btn="green", pin=2, pressed=v.get() == 3), bg="#3cb043", activebackground="#028a0f", width=24)

exitBtn = tk.Button(mainWindow, text="Exit", font=myFont,
                    command=close, bg="gray", width=24)

noneBtn.grid()
redBtn.grid()
blueBtn.grid()
greenBtn.grid()
exitBtn.grid()

mainWindow.protocol("WM_DELETE_WINDOW", close)

mainWindow.mainloop()
