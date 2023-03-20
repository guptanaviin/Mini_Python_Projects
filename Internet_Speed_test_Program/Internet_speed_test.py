from tkinter import *
import speedtest

def speedcheck():
    speed_test = speedtest.Speedtest()                  #speedtest ---> Module  Speedtest ---> class
    speed_test.get_servers()                            #get_servers ----> function
    download = str(round(speed_test.download()/(10**6),3)) + "Mbps"
    upload = str(round(speed_test.upload()/(10**6),3)) + "Mbps"
    lab_down.config(text = download)
    lab_up.config(text=upload)

speed_test = Tk()

speed_test.title("Internet_Speed_Test")
speed_test.geometry("600x620")
speed_test.config(bg="skyblue")

lab = Label(speed_test,text="INTERNET SPEED TEST",font=("Comic Sans",30,"bold"),bg="skyblue",fg="green")
lab.place(x=50,y=10,width=500,height=80)

lab = Label(speed_test,text="DOWLOADING SPEED",font=("Times New Roman",25,"bold"))
lab.place(x=100,y=100,width=400,height=80)

lab_down = Label(speed_test,text="00",font=("Times New Roman",25,"bold"))
lab_down.place(x=100,y=190,width=400,height=80)

lab = Label(speed_test,text="UPLOADING SPEED",font=("Times New Roman",25,"bold"))
lab.place(x=100,y=280,width=400,height=80)

lab_up = Label(speed_test,text="00",font=("Times New Roman",25,"bold"))
lab_up.place(x=100,y=370,width=400,height=80)

speed_test_button = Button(speed_test,text="CHECK SPEED",font=("Times New Roman",25,"bold"),relief=RAISED,command=speedcheck,fg="red")
speed_test_button.place(x=100,y=480,width=400,height=80)

speed_test.mainloop()
