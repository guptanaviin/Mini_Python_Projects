from tkinter import *                    
import os

def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutsown /r /t 20")
def logout():
    os.system("shutdown -l")
def shutdown():
    os.system("shutdown /r /t 1")


shut = Tk()
shut.title("ShutDown App")
shut.geometry("600x600")
shut.config(bg="skyblue")

restart_button = Button(shut,text="Restart",font=("Times New Roman",30,"bold"),relief=RAISED,cursor="plus",command=restart)
restart_button.place(x=150,y=40,height=100,width=300)

restart_time_button = Button(shut,text="Restart Time",font=("Times New Roman",30,"bold"),relief=RAISED,cursor="plus",command=restart_time)
restart_time_button.place(x=150,y=180,height=100,width=300)

log_off_button = Button(shut,text="Log Off",font=("Times New Roman",30,"bold"),relief=RAISED,cursor="plus",command=logout)
log_off_button.place(x=150,y=320,height=100,width=300)

shutdown_button = Button(shut,text="ShutDown",font=("Times New Roman",30,"bold"),relief=RAISED,cursor="plus",command=shutdown)
shutdown_button.place(x=150,y=460,height=100,width=300)

shut.mainloop()

