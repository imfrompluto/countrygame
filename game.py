# from curses import BUTTON3_CLICKED
import tkinter as tk
import random
import flags
from functools import partial

window = tk.Tk()
randomnumber = random.randint(0,len(flags.flags))
scorenumber = 0
score = tk.Label(text='score: ' + str(scorenumber))
score.config(font =(None, 15))
flag = tk.Label(text=flags.flags[randomnumber])
flag.config(font =(None,150))
countries = [
    flags.countries[random.randint(0,len(flags.flags))],
    flags.countries[random.randint(0,len(flags.flags))],
    flags.countries[random.randint(0,len(flags.flags))],
    ]

countries.insert(random.randrange(4),flags.countries[randomnumber])
def checkflag(country):
    global scorenumber
    global randomnumber
    global countries
    global button
    global button2
    global button3
    global button4

    print(country, flags.countries[randomnumber])
    if country == flags.countries[randomnumber]: 
        scorenumber = scorenumber + 1
        score.config(text='score: ' + str(scorenumber))
        randomnumber = random.randint(0,len(flags.flags))
        flag.config(text=flags.flags[randomnumber])
        countries = [
            flags.countries[random.randint(0,len(flags.flags))],
            flags.countries[random.randint(0,len(flags.flags))],
            flags.countries[random.randint(0,len(flags.flags))],
        ]
        countries.insert(random.randrange(4),flags.countries[randomnumber])
        button.config(text=countries[0])
        button2.config(text=countries[1])
        button3.config(text=countries[2])
        button4.config(text=countries[3])




button = tk.Button(window, text = countries[0], fg='black', bg="black", command=partial(checkflag, countries[0]))
button2 = tk.Button(window, text = countries[1], fg="black", bg="black", command=partial(checkflag, countries[1]))
button3 = tk.Button(window, text = countries[2], fg="black", bg="black", command=partial(checkflag, countries[2]))
button4 = tk.Button(window, text = countries[3], fg="black", bg="black", command=partial(checkflag, countries[3]))



flag.pack()
score.pack()
button.pack()
button2.pack()
button3.pack()
button4.pack()
window.mainloop()

# revise the code
