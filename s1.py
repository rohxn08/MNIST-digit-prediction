import tkinter as tk
from tkinter import *
from PIL import Image,ImageGrab
import numpy as np
#CNN model
from tensorflow.keras.layers import Conv2D,MaxPooling2D
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Flatten
from tensorflow.keras.models import load_model
import cv2

a=tk.Tk()

def draw(event):
    x1,y1=(event.x-1),(event.y-1)
    x2,y2=(event.x+1),(event.y+1)
    canvas.create_oval(x1,y1,x2,y2,fill="black",width=5)

canvas=tk.Canvas(a,width=400,height=400,bg="white")
canvas.pack()
canvas.bind('<B1-Motion>',draw)
a.mainloop()


def capture_canvas(canvas):
    x = a.winfo_rootx() + canvas.winfo_x()
    y = a.winfo_rooty() + canvas.winfo_y()
    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()

    img=ImageGrab.grab().crop((x, y, x1, y1))
    return img

def preprocessing(img):
    cv_img=cv2.cvtColor(np.array(img),cv2.COLOR_RGB2BGR)
    gray=cv2.cvtColor(cv_img,cv2.COLOR_BGR2GRAY)
    resized=cv2.resize(gray,(28,28),interpolation=cv2.INTER_AREA)
    inverted=255-resized
    normalized=inverted/255.0
    processed=normalized.reshape(1,28,28,1)
    return processed





'''def CNNModel():
    model=Sequential()
    model.add(Conv2D(32,(3,3),activation='relu',input_shape=(28,28,1)))
    model.add(MaxPooling2D(2,2))
    model.add(Conv2D(64,(3,3),activation='relu'))
    model.add(MaxPooling2D(2,2))
    model.add(Flatten())
    model.add(Dense(128,activation='relu'))
    model.add(Dense(10,activation='softmax'))
    model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
    
    return model'''


model=load_model('model.h5')

    
    

