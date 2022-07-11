import sympy
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
import os

t = sympy.Symbol('t')
s = sympy.Symbol('s')
#Window settings
window = Tk()
window.title('Laplace Transforms')
window.iconphoto(True, PhotoImage(file=r'transform.png'))
window.geometry('500x500')
window.resizable(False, False)
window.configure(bg = '#99CCFF')
frame = tk.Frame(window, bg = '#99CCFF')

#Label settings
label = tk.Label(frame, text = "Which operation do you want to perform?", font = ("Arial",15), bg = '#99CCFF')
label.pack()

#Combobox settings
select = ttk.Combobox(frame, values = ["Laplace Transform", "Inverse Laplace Transform"],width=26, font = "Arial 15", state = "readonly")
select.pack(pady = 20)
select.current(0)

#Function Label settings
function_label = tk.Label(frame, text = "Type the function to transform", font = ("Arial",15), bg = '#99CCFF')
function_label.pack()

#Function Entry settings
f = tk.StringVar()
function_entry = ttk.Entry(frame, textvariable=f, width=50)
function_entry.pack(pady=20)

#Writing instructions
inst_label = tk.Label(frame, text =
 "Remember that the variable used for Laplace transform is\n t (not x) and for the inverse Laplace transform is s\n and that t and s must be in parentheses (e.g. sin(t) not sint)\n For exponentiation use ** (e.g. t**2) and for exponentiation of e use exp(t)", font = ("Arial",10),
 bg = '#99CCFF')
inst_label.pack(pady = 5)

def laplace():
    try:
        fun = function_entry.get()
        trasformed = sympy.laplace_transform(fun, t, s, noconds = True)
        result_label.config(text=trasformed)
    except ValueError as error:
        showerror(title = 'Error', message = error)

def antilap():
    try:
        fun = function_entry.get()
        #w = sympy.Symbol('w', real = True)
        t = sympy.Symbol('t', positive = True)
        trasformed = sympy.inverse_laplace_transform(fun, s, t)
        result_label.config(text=trasformed)
    except ValueError as error:
        showerror(title = 'Error', message = error)

#Run Button settings
transform_button = tk.Button(frame, text="Run", bg = 'white')
transform_button.pack(pady = 20)
if (select.current() == 0):
    transform_button.configure(command = laplace)
else:
    transform_button.configure(command = antilap)

#Result Label
result_label = tk.Label(frame, font = ("Arial",20), bg = '#99CCFF')
result_label.pack(pady = 20)

frame.pack()
window.mainloop()


        
