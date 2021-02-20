from tkinter import*
from PIL import Image,ImageTk

class Welcome_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Welcome Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        #background image
        self.bg=ImageTk.PhotoImage(file ="rainbow.jpg")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

        #left image
        self.left=ImageTk.PhotoImage(file="dog_couple.jpg")
        left=Label(self.root,image = self.left).place(x=80,y=100,width=400,height=500)

        #login frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

        #frame title
        title=Label(frame1,text="WELCOME TO PLAYDATE",font=("times new roman",30,"bold"),bg="white",fg="#002e54").place(x=80,y=50)

        #frame body
        body=Label(frame1,text="We Plyclans believe every paw friend needs a pawfriend too!!",font=("times new roman",15,"bold"),bg="white",fg="#002e54").place(x=80,y=100)

        #sign in button
        btn_login=Button(self.root,command=self.login_window,text="Sign In",font=("times new roman",20),bg="#002e54",fg="#ffdeb3",bd=0,cursor="hand2").place(x=700,y=300,width=180,height=40)

        #register button
        btn_register=Button(self.root,command=self.register_window,text="Register",font=("times new roman",20),bd=0,cursor="hand2",bg="green",fg="white").place(x=700,y=360,width=180,height=40)
    
    def login_window(self):
        self.root.destroy()
        import login

    def register_window(self):
        self.root.destroy()
        import register

root = Tk()
obj=Welcome_window(root)
root.mainloop()        