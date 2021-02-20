from tkinter import *
import wikipedia
# from PIL import Image,ImageTk

def get_me():
    entry_value = entry.get()
    result.delete(1.0,END)
    try:
        result_value = wikipedia.summary(entry_value)
        result.insert(INSERT, result_value)

    except:
        result.insert(INSERT,"Please check your input or internet connection")

root = Tk()
root.geometry("1350x700")
root.config(bg="#008a99") #window color

topframe = Frame(root)
topframe.pack()

entry = Entry(topframe)
entry.pack(padx = 30, pady = 5)

button = Button(topframe, text='Search your dog breed', command=get_me)
button.pack(padx=20,pady=5)

bottomframe = Frame(root)
bottomframe.place(x=480, y=400 ,width =700, height= 500)

scroll = Scrollbar(bottomframe)
scroll.pack(side=RIGHT, fill= Y)
result = Text(bottomframe, width = 30, height = 20, yscrollcommand = scroll.set, wrap = WORD)
scroll.config(command=result.yview)
result.pack()

bottomframe.pack(padx=10,pady=50)

def playdate():
    root.destroy()
    import playdate   

#playdate button
btn_playdate=Button(root,command=playdate,text="Back to HomePage",font=("times new roman",12),bg="yellow",fg="blue",bd=0,cursor="hand2").place(x=538,y=500,width=200)

root.mainloop()
