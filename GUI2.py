from tkinter import*
from tkinter import Text, Tk
from Word import *
from Sentences import *
from Reader import *

#Define click function
def click():
	entered_text = Reader(textentry.get())
#main
window = Tk()
window.geometry("400x400")
window.title("Summarize text")
window.configure (background ="white")

#label
Label (window, text="Enter text:", bg="white", fg="black", font="arial 15") .grid (row=0, column=0, sticky=W)

#entry box
textentry = Text(window, width=50, height=20, background="#f5f5f5")
textentry.grid(row=2, column=0, sticky=W)

#submit
Button(window, text="Submit", width=10, command=click) .grid(row=3, column=0, sticky=W)
"""
#Output Label
Label (window, text="Output", bg="white", fg="black", font="arial 15") .grid(row=4, column=0, sticky=W)

#Output text
output=Text(window, width=38, height=10, background="gray")
output.grid(row=5, column=0, columnspan=2, sticky=W)
"""

#end of program

window.mainloop()