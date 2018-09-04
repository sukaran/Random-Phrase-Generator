import tkinter as tk

import random

window = tk.TK()
window.title("greetings_________")

window = tk.geometry("400*400")

def phrase_generator():

	phrases = ["Hello", "Wat's Up", " HOLA!!", "WELCOME"]

	name= str(entry1.get())

	return phrases[random.randint(0,3)] + name
	




def  phrase_display():
	greeting=phrase_generator()

	greeting_display = tk.Text(master=window, height=10, width=30)
	greeting_display.grid(column=0, row=0)

	greeting_display.insert(tk.END,greeting)


label1 = tk.Label(text="Welcome to my app")
label1.grid(column=0, row=0)


label2 = tk.Label(text="What's Your Name?")
label2.grid(column=0, row=1)


entry1=tk.Entry()
entry1.grid(column=1, row=1)

button1 = tk.Button(text="CLICK ME!", command = phrase_display)
button1.grid(column=0, row=2)

window.mainloop()



