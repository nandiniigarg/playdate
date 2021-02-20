from tkinter import*
from PIL import Image,ImageTk  #pip install Pillow
from tkinter import ttk,messagebox     
import pymysql #pip install pymysql

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white") #window color

        #background image
        self.bg=ImageTk.PhotoImage(file ="rainbow.jpg")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

        #left image
        self.left=ImageTk.PhotoImage(file="old.bg.jpg")
        left=Label(self.root,image = self.left).place(x=80,y=100,width=400,height=500)

        #register frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

        #frame title
        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)

        #first name and it's Entry field
        f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font =("times new roman", 15),bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)

        #last name and it's Entry field
        l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font =("times new roman", 15),bg="lightgray")
        self.txt_lname.place(x=370,y=130,width=250)

        #contact and it's Entry field
        contact=Label(frame1,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font =("times new roman", 15),bg="lightgray")
        self.txt_contact.place(x=50,y=200,width=250)

        #email and it's Entry field
        email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
        self.txt_email=Entry(frame1,font =("times new roman", 15),bg="lightgray")
        self.txt_email.place(x=370,y=200,width=250)

        #security question
        question=Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)
        
        #combobox
        self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=CENTER)
        self.cmb_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
        self.cmb_quest.place(x=50,y=270,width=250)
        self.cmb_quest.current(0)  

        #answer of security question and it's Entry field
        answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
        self.txt_answer=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_answer.place(x=370,y=270,width=250)
        
        #password and it's Entry field
        password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=310)
        self.txt_password=Entry(frame1,show="*",font=("times new roman",15),bg="lightgray")
        self.txt_password.place(x=50,y=340,width=250)

        #comfirm password and it's Entry
        cpassword=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=310)
        self.txt_cpassword=Entry(frame1,show="*",font=("times new roman",15),bg="lightgray")
        self.txt_cpassword.place(x=370,y=340,width=250)

        #checkbutton
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=50,y=380)
        
        #Register button
        self.btn_img=ImageTk.PhotoImage(file="register1.png")
        btn_register=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data).place(x=400,y=420)
        
        #sign in button
        btn_login=Button(self.root,command=self.login_window,text="Sign In",font=("times new roman",20),bd=0,cursor="hand2").place(x=350,y=543)

    def login_window(self):
        self.root.destroy()
        import login    
    
    
    
    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)
        self.txt_answer.delete(0,END)
        self.cmb_quest.current(0)
 
 
    def register_data(self):        
        
        if self.txt_fname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        elif self.txt_password.get()!=self.txt_cpassword.get():
            messagebox.showerror("Error","Password and Comfirm Password must be same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="playdate")
                cur=con.cursor()
                cur.execute("select * from playdate_users where email=%s",self.txt_email.get())
                row=cur.fetchone()
                print(row)
                if row!=None:
                    messagebox.showerror("Error","User already Exist,Please try with another Email",parent=self.root)
                else:
                    cur.execute("insert into playdate_users (f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                                    (self.txt_fname.get(),
                                    self.txt_lname.get(),
                                    self.txt_contact.get(),
                                    self.txt_email.get(),
                                    self.cmb_quest.get(),
                                    self.txt_answer.get(),
                                    self.txt_password.get()
                                    ))
                    con.commit()
                    con.close() 
                    messagebox.showinfo("SUCCESS","You are Registered.please SIGN IN",parent=self.root) 
                    self.clear()              

            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)    
           



root = Tk()
obj=Register(root)
root.mainloop()

