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


def ledToggle(pin: int):
    print(f"button pressed {sharedVariable.get()}")
    # if led.is_lit:
    #     led.off()
    #     v.set(0)


def diselectAllBtns():
    # turn off LEDs
    sharedVariable.set("")


def close():
    # turn led off
    # GPIO.cleanup()
    print("closing program")
    # exit program
    mainWindow.destroy()


availableColors = {
    'red': {
        'label': 'Red',
        'hexCode': "#ff0000",
        'value': 'red',
        'pin': 2,
    }, 'blue': {
        'label': 'Blue',
        'hexCode': '#3944bc',
        'value': 'blue',
        'pin': 2,
    },
    'green': {
        'label': 'Green',
        'hexCode': '#3cb043',
        'value': 'green',
        'pin': 2,
    },

}

### WIDGETS ###

sharedVariable = tk.StringVar(mainWindow, "")

noneBtn = tk.Radiobutton(mainWindow, indicatoron=0, variable=sharedVariable, value="", text="None", font=myFont,
                         command=lambda: diselectAllBtns(), bg="gray", width=24).grid()

redbtn = tk.Radiobutton(mainWindow, indicatoron=0, variable=sharedVariable, value=availableColors['red']['value'], text=availableColors['red']['label'], font=myFont,
                        command=lambda: ledToggle(pin=availableColors['red']['pin']), bg=availableColors['red']['hexCode'], width=24).grid()

greeBtn = tk.Radiobutton(mainWindow, indicatoron=0, variable=sharedVariable, value=availableColors['green']['value'], text=availableColors['green']['label'], font=myFont,
                         command=lambda: ledToggle(pin=availableColors['green']['pin']), bg=availableColors['green']['hexCode'], width=24).grid()

blueBtn = tk.Radiobutton(mainWindow, indicatoron=0, variable=sharedVariable, value=availableColors['blue']['value'], text=availableColors['blue']['label'], font=myFont,
                         command=lambda: ledToggle(pin=availableColors['blue']['pin']), bg=availableColors['blue']['hexCode'], width=24).grid()


# for value in availableColors.values():
#     tk.Radiobutton(mainWindow, indicatoron=0, value=value['value'], text=value['label'], font=myFont,
#                    command=lambda: ledToggle(btn=value['value'], pin=2, currValue=sharedVariable.get()), bg=value['hexCode'], width=24).grid()


exitBtn = tk.Button(mainWindow, text="Exit", font=myFont,
                    command=close, bg="gray", width=24).grid()

mainWindow.protocol("WM_DELETE_WINDOW", close)

mainWindow.mainloop()
