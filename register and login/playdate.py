from tkinter import*
from PIL import Image,ImageTk  #pip install Pillow

class Playdate:
    def __init__(self,root):
        self.root=root
        self.root.title("playdate Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="pink") #window color

        #background image
        self.bg=ImageTk.PhotoImage(file ="PLAYDATE.png")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,width=1300,height=650)

        #find_mate button
        btn_find_mate=Button(self.root,text="Find Perfect Mate",font=("times new roman",20),bg="#002e54",fg="#ffdeb3",bd=0,cursor="hand2").place(x=55,y=450,width=250,height=60)

        #chat button
        btn_chat=Button(self.root,text="Connect to Everyone",font=("times new roman",20),bd=0,cursor="hand2",bg="#002e54",fg="#ffdeb3").place(x=360,y=450,width=250,height=60)

        #email_chat button
        btn_email_chat=Button(self.root,command=self.email_chat,text="Email personally",font=("times new roman",20),bg="#002e54",fg="#ffdeb3",bd=0,cursor="hand2").place(x=680,y=450,width=250,height=60)

        #search button
        btn_search=Button(self.root,command=self.search,text="search more about pet",font=("times new roman",20),bd=0,cursor="hand2",bg="#002e54",fg="#ffdeb3").place(x=985,y=450,width=250,height=60)
       
        #game button
        btn_game=Button(self.root,text="Floof-Plus",font=("times new roman",20),bd=0,cursor="hand2",bg="yellow",fg="#002e54").place(x=520,y=550,width=250,height=60)
    
        
    # def find_mate(self):
    #     self.root.destroy()
    #     import find_mate

    # def chat(self):
    #     self.root.destroy()
    #     import register
    
    def email_chat(self):
        self.root.destroy()
        import email_chat

    def search(self):
        self.root.destroy()
        import search
    
    # def vir_pet(self):
    #     self.root.destroy()
    #     import vir_pet
root = Tk()
obj=Playdate(root)
root.mainloop()        