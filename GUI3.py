from Tkinter import *
root= Tk()
root.title("My First GUI")
root.geometry("800x200")
frame1=Frame(root)
frame1.grid()
label1 = Label(frame1, text = "Here is a label!")
label1.grid()
text1 = Text(frame1, width = 35, height = 5)
text1.grid()
radiobutton1 = Radiobutton(frame1, text= "C Programming", value=0)
radiobutton1.grid()
radiobutton2 =Radiobutton(frame1, text= "Python Programming")
radiobutton2.grid()
root.mainloop()