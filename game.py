# from curses import BUTTON3_CLICKED
import tkinter as tk
import random
import flags
from functools import partial

window = tk.Tk()
randomnumber = random.randint(0,len(flags.flags))
scorenumber = 0
score = tk.Label(text='score: ' + str(scorenumber))
score.config(font =(None,50))
flag = tk.Label(text=flags.flags[randomnumber])
flag.config(font =(None,150))
countries = [
    flags.countries[random.randint(0,len(flags.flags))],
    flags.countries[random.randint(0,len(flags.flags))],
    flags.countries[random.randint(0,len(flags.flags))],
    
    ]
countries.insert(random.randrange(4),flags.countries[randomnumber])

def checkflag(n):
    print("aaa")
    n = n + 1
    score.config(text='score: ' + str(n))

button = tk.Button(window, text = countries[0], fg='black', bg="black", command=partial(checkflag,scorenumber))
button2 = tk.Button(window, text = countries[1], fg="black", bg="black")
button3 = tk.Button(window, text = countries[2], fg="black", bg="black")
button4 = tk.Button(window, text = countries[3], fg="black", bg="black")



flag.pack()
score.pack()
button.pack()
button2.pack()
button3.pack()
button4.pack()
window.mainloop()


