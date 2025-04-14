import tkinter as tk
from tkinter import simpledialog

root = tk.Tk()
root.title('Weather App')
root.geometry("300x300")

title = tk.Label(root,text="Weather App",font=("Arial", 20, "bold"))
title.place(x=65,y=50)

enter_button = tk.Button(root,text="Enter",font=("Arial", 15, "bold"))
enter_button.place(x=125,y=170)

city_entry = tk.Entry(root, font=("Arial", 18))
city_entry.place(x=20,y=110)

root.mainloop()