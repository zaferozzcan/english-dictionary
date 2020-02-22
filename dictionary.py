from tkinter import *
window = Tk(baseName=  "English Dictionay")

import json
data = json.load(open("data.json"))
from difflib import get_close_matches

def translator(word):
    word  = word.lower()
    if word in data:
        return data[word][0
                         ]
    elif word.title() in data:
        return data[word.title()]
    elif get_close_matches(word, data.keys()) != 0:
        liste = [i for i in get_close_matches(word, data.keys())][0]
        return data[liste][0]
    else:
        return "There is no such word!"

def translator_command():
    result = translator(e1_value.get())
    for row in result[0]:
        t1.insert(END,result)
        

b1 = Button(window, text = "Search", command = translator_command)
b1.grid(row = 0, column = 3)

e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value)
e1.grid(row = 1, column = 3)

t1 = Text(window, height =10, width = 20)
t1.grid(row = 3, column = 3)

l1 = Label(window, text = "Defination")
l1.grid(row = 2, column = 3)


window.mainloop()