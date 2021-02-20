from tkinter import *
import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


root= Tk()
root.geometry('500x660')
root.title("Play Date Email Sending GUI")

Label_0=Label(root, text="Set Your Play Date Account", width=25, fg="green", font=("Calibri",20))
Label_0.place(x=90,y=33)

Label_1=Label(root, text="Your Email Account:", width=20, font=("bold",10))
Label_1.place(x=40,y=110)
#######################################
#for getting entry input
Rmail=StringVar()
Rpswrd=StringVar()
Rsender=StringVar()
Rsubject=StringVar()
#######################################

emailE=Entry(root, width=40, textvariable=Rmail)
emailE.place(x=200, y=110)

Label_2=Label(root, text="Your Password:", width=20, font=("bold",10))
Label_2.place(x=40,y=160)


passwordE=Entry(root, width=40, show="*", textvariable=Rpswrd)
passwordE.place(x=200, y=160)

compose=Label(root, text="Compose", width=20, font=("bold",15))
compose.place(x=180,y=210)

Label_3=Label(root, text="Sent To Email:", width=20, font=("bold",10))
Label_3.place(x=40,y=260)


senderE=Entry(root, width=40, textvariable=Rsender)
senderE.place(x=200, y=260)

Label_4=Label(root, text="Subject:", width=20, font=("bold",10))
Label_4.place(x=40,y=310)


subjectE=Entry(root, width=40, textvariable=Rsubject)
subjectE.place(x=200, y=310)


Label_5=Label(root, text="Message:", width=20, font=("bold",10))
Label_5.place(x=40,y=360)


msgbodyE=Text(root, width=30, height=10)
msgbodyE.place(x=200, y=360)




 


def sendemail():

    
   



    try:
        mymsg=MIMEMultipart()
        mymsg['From']=str(Rmail.get())
        mymsg['To']= str(Rsender.get())
        mymsg['Subject']= str(Rsubject.get())

        mymsg.attach(MIMEText(msgbodyE.get(1.0,'end'), 'plain'))

        server=smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(str(Rmail.get()), str(Rpswrd.get()))
        text=mymsg.as_string()
        server.sendmail(str(Rmail.get()), str(Rsender.get()), text)

        Label_6=Label(root, text="Done!", width=20,fg='green', font=("bold",15))
        Label_6.place(x=140,y=550)

        server.quit()
    except:
        Label_6=Label(root, text="something went wrong!", width=20,fg='red', font=("bold",15))
        Label_6.place(x=140,y=550)



Button(root,text="Send", width=20, bg='brown',fg="white", command=sendemail).place(x=180, y=540)


def playdate():
    root.destroy()
    import playdate   


#playdate button
btn_playdate=Button(root,command=playdate,text="Back to HomePage",font=("times new roman",12),bg="green",fg="white",bd=0,cursor="hand2").place(x=187,y=590)

root.mainloop()



