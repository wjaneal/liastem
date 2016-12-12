
#from Tkinter import *
import pyserial
#import cv2
#from cv2 import *
#from PIL import Image, ImageTk
import tkinter

class Arduino:
    def writechar(self, char):
        print ("Sending ", char, " to the Arduino")
        #self.connection1.write(char)
        #s = self.connection1.read(21)        # read up to ten bytes (timeout)
        #line = self.connection1.readline()   # read a '\n' terminated line
        #print s, line

    def connection(self):
        return  pyserial.Serial('/dev/ttyACM0', baudrate=9600, timeout=0.1)

    
class App:
    def __init__(self,parent):
        #The frame instance is stored in a local variable 'f'.
        #After creating the widget, we immediately call the 
        #pack method to make the frame visible.

        f = tkinter.Frame(parent, background = "light blue", width = 600)
        f.pack()
        
        #we then create an entry widget,pack it and then 
        #create two more button widgets as children to the frame.
    
        #self.entry = Entry(f,text="enter your choice")
        #self.entry.pack(side= TOP,padx=10,pady=12)
        
        #this time, we pass a number of options to the
        # constructor, as keyword arguments. The first button
        # is labelled "exit"and the second is labelled "Hello". 
        #Both buttons also take a command option. This option 
        #specifies a function, or (as in this
        #case) a bound method, which will be called when the button is clicked.
        
        self.up = tkinter.Button(f, text="Up", font = "Arial 24 bold", background = "blue",foreground = "white", activebackground="yellow",height=2, width=10,command=self.helicopterup).grid(row=0, column=0)
        self.forward = tkinter.Button(f, text="Forward", font = "Arial 24 bold",background = "blue",foreground = "white", activebackground="yellow",height=2, width=10,command=self.helicopterforward).grid(row=1, column=0)
        self.hover = tkinter.Button(f, text="Hover", font = "Arial 24 bold", background = "blue",foreground = "white", activebackground="yellow", height=2, width=10,command=self.helicopterhover).grid(row=0, column=1)
        self.backwards = tkinter.Button(f, text="Backwards", font = "Arial 24 bold", background = "blue",foreground = "white", activebackground="yellow",height=2, width=10,command=self.helicopterbackwards).grid(row=1, column=1)
        self.down = tkinter.Button(f, text="Down", font = "Arial 24 bold", background = "blue",foreground = "white", activebackground="yellow", height=2, width=10,command=self.helicopterdown).grid(row=0, column=2)
        self.vx0 = tkinter.Button(f, text="Vx = 0", font = "Arial 24 bold", background = "blue",foreground = "white", activebackground="yellow",height=2, width=10,command=self.helicoptervx0).grid(row=1, column=2)
        self.off = tkinter.Button(f, text="Off", font = "Arial 24 bold", background = "blue",foreground = "white", activebackground="yellow", height=2, width=10,command=self.helicopteroff).grid(row=0, column=3)
        self.left = tkinter.Button(f, text="Left", font = "Arial 24 bold", background = "blue",foreground = "white", activebackground="yellow",height=2, width=10,command=self.helicopterleft).grid(row=2, column=0)
        self.vy0= tkinter.Button(f, text="Vy = 0", font = "Arial 24 bold", background = "blue",foreground = "white", activebackground="yellow",height=2, width=10,command=self.helicoptervy0).grid(row=2, column=1)
        self.right = tkinter.Button(f, text="Right", font = "Arial 24 bold", background = "blue",foreground = "white", activebackground="yellow",height=2, width=10,command=self.helicopterright).grid(row=2, column=2)
        self.turnleft = tkinter.Button(f, text="Turn Left", font = "Arial 24 bold", background = "blue",foreground = "white", activebackground="yellow",height=2, width=10,command=self.helicopterturnleft).grid(row=3, column=0)
        self.theta0= tkinter.Button(f, text="Theta = 0", font = "Arial 24 bold", background = "blue",foreground = "white", activebackground="yellow",height=2, width=10,command=self.helicoptertheta0).grid(row=3, column=1)
        self.turnright = tkinter.Button(f, text="Turn Right", font = "Arial 24 bold", background = "blue",foreground = "white", activebackground="yellow",height=2, width=10,command=self.helicopterturnright).grid(row=3, column=2)

        self.auto = tkinter.Button(f, text="Autoflight", font = "Arial 24 bold", background = "yellow",foreground = "black", activebackground="yellow", height=2, width=10,command=self.autoflight).grid(row=3,column=3)
        self.openconn = tkinter.Button(f,background = "green",activebackground="blue",foreground = "white",text="Open\n Connection", font = "Arial 24 bold", height=2, width=10,command=self.connect).grid(row=4,column=0)
        self.closeconn = tkinter.Button(f, background = "red", activebackground="red",foreground = "white", text="Close\n Connection", font = "Arial 24 bold", height=2, width=10,command=self.disconnect).grid(row=4,column=1)
        self.exit = tkinter.Button(f, text="Exit", font = "Arial 24 bold", activebackground="red",foreground = "white", background = "orange", height=2, width=10, command=f.destroy).grid(row=4,column=2)


        #self.im = Image.open("heli.jpg")
        #self.im1 = PhotoImage(self.im)
        #self.helipic = Label(f, image=self.im1, width = 200, height = 200).grid(row=1,column=3,rowspan=2)
        #self.disp = Label(f, width = 200, height = 100, background = "purple")
#        C:\Users\gwilm\Documents\NCCI\MCV4U\3D - Motion Tracker\OO_Dev\
        #sself.disp.pack(side = RIGHT)

    def print_this(self):
        print ("this is to be printed")

        #Finally, we provide some script level code that creates
        # a Tk root widget,and one instance of the App class using 
        #the root widget as its parent:

        #The last call is to the mainloop method on the root widget. It enters the
        #Tk event loop, in which the application will stay until the quit method is
        #called (just click the exit button), or the window is closed.
    def helicopterup(self):
        print ("Moving the helicopter up")
        Arduino_Conn.writechar("A255")
        

    def helicopterhover(self):
        print ("Hovering the helicopter")
        Arduino_Conn.writechar("A125")
        

    def helicopterdown(self):
        print ("Moving the helicopter down")
        Arduino_Conn.writechar("A100")
        
    def helicopteroff(self):
        print ("Cutting power to the helicopter")
        Arduino_Conn.writechar("A000")

    def helicopterforward(self):
        #print "Moving the helicopter forward"
        Arduino_Conn.writechar("D250")

    def helicopterbackwards(self):
        #print "Moving the helicopter backwards"
        Arduino_Conn.writechar("D000")

    def helicoptervx0(self):
        #print "Helicopter Vx = 0"
        Arduino_Conn.writechar("D080")

    def helicopterturnleft(self):
        #print "Helicopter turning left"
        Arduino_Conn.writechar("C000")

    def helicoptertheta0(self):
        #print "Helicopter theta = 0"
        Arduino_Conn.writechar("C128")

    def helicopterturnright(self):
        #print "Helicopter turning right"
        Arduino_Conn.writechar("C200")
        
    def helicopterleft(self):
        #print "Helicopter moving left"
        Arduino_Conn.writechar("B000")

    def helicoptervy0(self):
        #print "Helicopter Vy = 0"
        Arduino_Conn.writechar("B100")

    def helicopterright(self):
        #print "Helicopter moving right"
        Arduino_Conn.writechar("B255")

    def throttle(self, level):
        level = int(level)
        if level < 0:
            level = 0
        if level >255:
            level = 255
            
        if level < 10:
            Arduino_Conn.writechar("A00"+str(level))
        elif level < 100:
            Arduino_Conn.writechar("A0"+str(level))
        else:
            Arduino_Conn.writechar("A"+str(level))

    def autoflight(self):
            count = 0
            delaytime = 1200
            while count < 18:
                self.throttle(200)
                self.helicopterleft()
                delay = 0
                while delay < delaytime:
                    delay +=1
                count +=1
            count = 0
            while count < 18:
                self.throttle(100)
                #self.helicopterbackwards()
                #self.helicopterright()
                delay = 0
                while delay < delaytime:
                    delay +=1
                count +=1
            count = 0
            #self.helicoptervy0()
            while count < 38:
                self.throttle(50)
                #self.helicopterleft() 
                delay = 0
                while delay < delaytime:
                    delay +=1
                count +=1
            self.throttle(0)
            self.helicoptervx0()
            
                
                 
    def connect(self):
        print ("The connection to the arduino is being established")
        Arduino_Conn.connection1 = Arduino_Conn.connection()
        print ("The connection seems to have been established")
    
    def disconnect(self):
        Arduino_Conn.connection1.flushInput()
        Arduino_Conn.connection1.flushOutput()
        Arduino_Conn.connection1.close()
        print ("Disconnected")
        

Arduino_Conn = Arduino()
 
root = tkinter.Tk()
root.title('Helicopter Test Flight Application')
app = App(root)

root.mainloop()
