import tkinter as tk

root = tk.Tk()
root.title('Weather App')
root.geometry("300x400")

title = tk.Label(root,text="Weather App",font=("Arial", 20, "bold"))
title.place(x=70,y=50)

enter_button = tk.Button(root,text="Enter",font=("Arial", 15, "bold"))
enter_button.place(x=125,y=200)

root.mainloop()