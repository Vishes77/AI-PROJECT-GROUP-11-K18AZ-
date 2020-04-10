#main
# import tkinter module 
#main project
import re
from tkinter import * 
import numpy as np
import cv2,time

def buttonclickcamera():
    print("Camera Button Clicked cameraone")
    detector= cv2.CascadeClassifier('C:/Users/princ/Anaconda3/Library/etc/haarcascades/haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)

    while(True):
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        cv2.imshow('frame',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    

    time.sleep(3)
    cv2.waitKey(0) # close the window if any key is pressed.
    cap.release()
    cv2.destroyAllWindows()
    
def buttonclickvid():
    print("Camera Button Clicked videoone")

#"C:\\Users\\princ\\OneDrive\\Pictures\\Screenshots\\a.jpg"
#for picture detection
def display():
    def disp(a):
        stri = e1.get()
        print(str(stri))
#         stri=str(stri)
#         print(stri)
        face_cascade = cv2.CascadeClassifier("C:/Users/princ/Anaconda3/Library/etc/haarcascades/haarcascade_frontalface_default.xml")
        img = cv2.imread(stri)

        gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray_img,scaleFactor = 1.05,minNeighbors =5)

        for x,y,w,h in faces:
            img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,3),3)
    
        resized= cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))

        cv2.imshow("Gray",resized)

        cv2.waitKey(0)

        cv2.destroyAllWindows()
        #function completed.    
    nextbutton = int(var.get())
    e1=Entry(master, width=25, fg='blue', bg='yellow',font=('Arial', 14))
    e1.grid(row = 3, column = 1,columnspan = 2, ipady = 28,ipadx=115)
    e1.bind('<Return>',disp)
    messageVarV = Message(master, text = ourMessage) 
    messageVarV.config(bg='lightgreen',font=instfntss)
    messageVarV.grid(row = 4, column = 1,columnspan = 2, ipady = 28,ipadx=221)

def displayv():
    nextbutton = int(var.get())
    camera=Button(master, text='Open Camera', width=2, height=1,command =buttonclickcamera)
    camera.grid(row = 4, column = 1,columnspan = 2, ipady = 28,ipadx=241)
#     camera=Button(master, text='Upload Video', width=2, height=1, command =buttonclickvid)
#     camera.grid(row = 4, column = 2, ipady = 28,ipadx=115)
    messageVar = Message(master, text = ourMessage) 
    messageVar.config(bg='lightgreen',font=instfntss)
    messageVar.grid(row = 3, column = 1,columnspan = 2, ipady = 28,ipadx=221)
    
master = Tk()
#Necessary elements.
fnt=('Times', 25, 'bold')
instfnt=('Times',15,'bold')
instfnts=('Times',13,'bold')
instfntss=('Times',11,'bold')
nextbutton = 0
var = IntVar()
ourMessage ="Locked"

#Layoutpart

tittle = Label(master, text = "FACE DETECTION SYSTEM",font=fnt,fg = "light green",bg = "blue")  
instructions= Label(master, text = "INSTRUCTION'S",fg = "Black",font=instfnt,bg = "orange")
choiceselection = Label(master, text = "Kindly follow the Instructions",font=instfnt,fg = "light green",bg = "blue")
instructions1= Label(master, text = "Slect the Mode By which you Want to detect  >>>",fg = "Black",font=instfnts,bg = "orange")
# byphotoselection= Checkbutton(master, bg = 'yellow', fg='green',font=('Georgia', 20, 'underline'), text='By Photo')
# byphotoVideo= Checkbutton(master, bg = 'yellow', fg='green',font=('Georgia', 20, 'underline'), text='By Video')
byphotoselection=Radiobutton(master, bg='yellow', fg='green', font=('Georgia', 20),text='BY Photo', variable=var, value=1, command=display)
byphotoVideo=Radiobutton(master, bg='yellow', fg='green', font=('Georgia', 20),text='By Video', variable=var, value=2, command=displayv)
instructions2= Label(master, text = "PLease Use Double BackSlash For Location >>> \n C:\\\\Users\\\\princ\\\\OneDrive\\\\Pictures\\\\Screenshots\\\\a.jpg",fg = "Black",font=instfnts,bg = "orange")
instructions3= Label(master, text = "Please Choose Any One :  >>> \n Press 'q' to quit ",fg = "Black",font=instfnts,bg = "orange")

messageVar = Message(master, text = ourMessage) 
messageVar.config(bg='lightgreen',font=instfntss)

messageVarV = Message(master, text = ourMessage) 
messageVarV.config(bg='lightgreen',font=instfntss)



#alignment part

tittle.grid(row = 0, column = 0,columnspan = 3, ipady = 28,ipadx=247)
instructions.grid(row = 1, column = 0, ipady = 20,ipadx=133)
choiceselection.grid(row = 1, column = 1,columnspan = 2, ipady = 20,ipadx=130)
instructions1.grid(row = 2, column = 0, ipady = 20,ipadx=30)
byphotoselection.grid(row = 2, column = 1,ipady = 10,ipadx=52)
byphotoVideo.grid(row = 2, column = 2,ipady = 10,ipadx=53)
instructions2.grid(row = 3, column = 0,ipady = 20,ipadx=1)
instructions3.grid(row = 4, column = 0,ipady = 19,ipadx=102)
messageVar.grid(row = 3, column = 1,columnspan = 2, ipady = 28,ipadx=221)
messageVarV.grid(row = 4, column = 1,columnspan = 2, ipady = 28,ipadx=221)

mainloop() 
