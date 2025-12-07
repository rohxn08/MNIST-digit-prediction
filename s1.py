import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except Exception:
    ctypes.windll.user32.SetProcessDPIAware()

import tkinter as tk
from tkinter import *
from PIL import Image,ImageGrab
import numpy as np
#CNN model
import tensorflow as tf
from tensorflow.keras.models import load_model

import cv2

# Load the model
model=load_model('model.h5')

# Create main window
a=tk.Tk()
a.title("Digit Recognition")
a.geometry("500x650")

def draw(event):
    x1,y1=(event.x-1),(event.y-1)
    x2,y2=(event.x+1),(event.y+1)
    canvas.create_oval(x1,y1,x2,y2,fill="black",width=10)

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

def predict_digit():
    try:
        img=capture_canvas(canvas)
        processed=preprocessing(img)
        prediction=model.predict(processed,verbose=0)
        digit=np.argmax(prediction)
        confidence=prediction[0][digit]*100
        result_label.config(text=f"Predicted Digit: {digit}\nConfidence: {confidence:.2f}%")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")

def clear_canvas():
    canvas.delete("all")
    result_label.config(text="Draw a digit and click Predict")

canvas=tk.Canvas(a,width=400,height=400,bg="white",cursor="pencil")
canvas.pack(pady=10)
canvas.bind('<B1-Motion>',draw)

# Button frame
button_frame=tk.Frame(a)
button_frame.pack(pady=10)

# Predict button
predict_btn=tk.Button(button_frame,text="Predict Digit",command=predict_digit,
                     bg="#4CAF50",fg="white",font=("Arial",12,"bold"),
                     padx=20,pady=10)
predict_btn.pack(side=tk.LEFT,padx=5)

# Clear button
clear_btn=tk.Button(button_frame,text="Clear",command=clear_canvas,
                   bg="#f44336",fg="white",font=("Arial",12,"bold"),
                   padx=20,pady=10)
clear_btn.pack(side=tk.LEFT,padx=5)

# Result label
result_label=tk.Label(a,text="Draw a digit and click Predict",
                     font=("Arial",14,"bold"),fg="#2196F3")
result_label.pack(pady=10)

a.mainloop()


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
