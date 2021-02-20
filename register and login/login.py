from tkinter import*
from PIL import Image,ImageTk
import pymysql #pip install pymysql
from tkinter import messagebox,ttk

class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        #background image
        self.bg=ImageTk.PhotoImage(file ="rainbow.jpg")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

        #left image
        self.left=ImageTk.PhotoImage(file="login.jpg")
        left=Label(self.root,image = self.left).place(x=80,y=100,width=400,height=500)

        #login frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

        #frame title
        title=Label(frame1,text="LOGIN HERE",font=("times new roman",30,"bold"),bg="white",fg="#002e54").place(x=80,y=50)

        #email and it's Entry field
        email=Label(frame1,text="EMAIL ADDRESS",font=("times new roman",18,"bold"),bg="white",fg="gray").place(x=80,y=150)
        self.txt_email=Entry(frame1,font =("times new roman", 15),bg="lightgray")
        self.txt_email.place(x=80,y=180,width=350,height=35)

        #password and it's Entry field
        password=Label(frame1,text="PASSWORD",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=80,y=250)
        self.txt_password=Entry(frame1,show="*",font=("times new roman",15),bg="lightgray")
        self.txt_password.place(x=80,y=280,width=350,height=35)

        #register button
        btn_reg=Button(frame1,command=self.register_window,cursor="hand2",text="Register new Account?",font=("times new roman",14),bg="white",bd=0,fg="#002e54").place(x=80,y=350)

        #forget button
        btn_forget=Button(frame1,command=self.forget_password_window,cursor="hand2",text="Forget Password?",font=("times new roman",14),bg="white",bd=0,fg="red").place(x=290,y=350)
        
        #login button
        btn_login=Button(frame1,cursor="hand2",text="LOGIN",command=self.login,font=("times new roman",18),bg="#002e54",fg="#ffdeb3").place(x=80,y=390,width=180,height=40)

    #reset function
    def reset(self):
        self.txt_email.delete(0,END)
        self.cmb_quest.current(0)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_new_pass.delete(0,END)
    
    
    #forget password logic
    def forget_password(self):
        if self.cmb_quest.get()=="Select" or self.txt_answer.get=="" or self.txt_new_pass.get()=="":
            messagebox.showerror("Error","ALL fields are required!!",parent=self.root2)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="playdate")
                cur=con.cursor()
                cur.execute("select * from playdate_users where email=%s and question=%s and answer=%s",(self.txt_email.get(),self.cmb_quest.get(),self.txt_answer.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please Select th Correct Security Question / Enter Answer",parent=self.root2)
                else:
                    cur.execute("update playdate_users set password=%s where email=%s",(self.txt_new_pass.get(),self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","your password has been reset,Please login with your new password",parent=self.root2)
                    
                    self.reset()
                    self.root2.destroy()

            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)

   
    #forget password window 
    def forget_password_window(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error","Please enter your email to change your password",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="playdate")
                cur=con.cursor()
                cur.execute("select * from playdate_users where email=%s",self.txt_email.get(),)
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please enter your registered email to change the password",parent=self.root)
                else: 
                    con.close()    
                    self.root2=Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("350x400+495+150")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    t=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=0,y=10,relwidth=1)

                    #security question
                    question=Label(self.root2,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        
                    #combobox
                    self.cmb_quest=ttk.Combobox(self.root2,font=("times new roman",13),state='readonly',justify=CENTER)
                    self.cmb_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
                    self.cmb_quest.place(x=50,y=130,width=250)
                    self.cmb_quest.current(0)  
 
                    #answer of security question and it's Entry field
                    answer=Label(self.root2,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=180)
                    self.txt_answer=Entry(self.root2,font=("times new roman",15),bg="lightgray")
                    self.txt_answer.place(x=50,y=210,width=250)

                    #new password and it's field
                    new_pass=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=260)
                    self.txt_new_pass=Entry(self.root2,font=("times new roman",15),bg="lightgray")
                    self.txt_new_pass.place(x=50,y=290,width=250)

                    #change password button
                    btn_change_password=Button(self.root2,cursor="hand2",command=self.forget_password,text="Reset Password",font=("times new roman",15,"bold"),bg="green",fg="white").place(x=90,y=340)


            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
        
    
    #register button redirect
    def register_window(self):
        self.root.destroy()
        import register

    #login button to welcome page
    def login(self):
        if self.txt_email.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("Error","all fields are required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="playdate")
                cur=con.cursor()
                cur.execute("select * from playdate_users where email=%s and password=%s",(self.txt_email.get(),self.txt_password.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid USERNAME & PASSWORD",parent=self.root)
                else:
                    messagebox.showinfo("SUCCESS","WELCOME",parent=self.root)
                    self.root.destroy()
                    import playdate
                con.close()    

            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)


root = Tk()
obj=Login_window(root)
root.mainloop()
