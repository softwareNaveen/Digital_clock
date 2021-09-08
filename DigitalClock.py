from  tkinter import Tk,Label

window=Tk()

window.title("Digital clock")
window.geometry("600x300")
window.configure(bg="yellow")

label=Label(window,text="welcome to tkinter",bg="cyan",font=("Arial",25,"bold"))
label.pack(pady=50)

window.mainloop()
