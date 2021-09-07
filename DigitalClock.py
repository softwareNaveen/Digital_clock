from tkinter import Tk,Label

window=Tk()

window.title("Digital clock")
window.geometry("400x400")
window.configure(bg="cyan")

label=Label(window,text="welcome" ,font=("Arial Black",78,"bold") ,bg="steelblue")
label.pack(pady=100)
window.mainloop()
