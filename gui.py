import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk
import numpy as np

from keras.models import load_model
from tensorflow.keras.losses import MeanAbsoluteError

# load the model
custom_objects = {'mae': MeanAbsoluteError()}
model = load_model('Age_Gender_Detection.h5', custom_objects=custom_objects)

# Recompile with the same optimizer, loss, and metrics used during training
model.compile(optimizer='adam', loss=['binary_crossentropy', 'mae'], metrics=['accuracy', 'accuracy'])

# Initialize the GUI
top = tk.Tk()
top.geometry("800x600")
top.title("Age and Gender Detector")
top.configure(background='#CDCDCD')

# Defining detect function which detects the age and gender of the person in the image using the model
def detect(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((48, 48))
    image = np.expand_dims(image, axis=0)
    image = np.array(image)
    image = np.delete(image, 0, 1) # delete the first channel
    image = np.resize(image, (48, 48, 3))
    
    genders_f = ["Male", "Female"]
    image = np.array([image])/255
    pred = model.predict(image)
    age = int(np.round(pred[1][0]))
    gender = int(np.round(pred[0][0]))
    
    label1.configure(foreground='#011638', text="Age: " + str(age))
    label2.configure(foreground='#011638', text="Gender: " + str(genders_f[gender]))
    
def show_detect_button(file_path):
    detect_button = Button(top, text="Detect Age and Gender", command=lambda: detect(file_path), padx=10, pady=5)
    detect_button.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))
    detect_button.place(relx=0.79, rely=0.46)
    
def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25), (top.winfo_height()/2.25)))
        im = ImageTk.PhotoImage(uploaded)
        
        sign_image.configure(image=im)
        sign_image.image = im
        label1.configure(text='')
        label2.configure(text='')
        show_detect_button(file_path)
    except:
        pass

# One label for age one for gender
label1 = Label(top, background='#CDCDCD', font=('arial', 15, 'bold'))
label2 = Label(top, background='#CDCDCD', font=('arial', 15, 'bold'))
sign_image = Label(top)
label1.pack(side='bottom', expand=True)
label2.pack(side='bottom', expand=True)

# configuring upload button
upload = Button(top, text="Upload an image", command=upload_image, padx=10, pady=5)
upload.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))
upload.pack(side='bottom', pady=50, expand=True)
sign_image.pack(side='bottom', expand=True)

heading = Label(top, text="Age and Gender Detector", pady=20, font=('arial', 20, 'bold'), background='#CDCDCD')
heading.configure(background='#CDCDCD', foreground='#364156')
heading.pack()
top.mainloop()
