import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import numpy as np

from keras.models import load_model

# Initialize the GUI
top = tk.Tk()
top.geometry("800x600")
top.title("Age and Gender Detector")
top.configure(background='#CDCDCD')

# One label for age one for gender
label1 = Label(top, background='#CDCDCD', font=('arial', 15, 'bold'))
label2 = Label(top, background='#CDCDCD', font=('arial', 15, 'bold'))

