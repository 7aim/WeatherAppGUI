import requests as re
import tkinter as tk
from tkinter import messagebox

API_KEY = "9acd0597ae349fa651ff17893ec5b7e2"

MAIN_COLOR = "#363763"
BG_MAIN = "#2d2e52"

root = tk.Tk()
root.title('Weather App')
root.geometry("300x300")
root.configure(bg=BG_MAIN)

title = tk.Label(root,text="Weather App",font=("Arial", 20, "bold"),bg=BG_MAIN,fg="White")
title.place(x=60,y=50)

city_entry = tk.Entry(root, font=("Arial", 18),bg=MAIN_COLOR,fg="White")
city_entry.place(x=18,y=110)

def prt():
    city = city_entry.get()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    if re.get(url).status_code == 200:
        response = re.get(url)
        data = response.json()
        messagebox.showinfo(f"Weather",f"Country : {data["sys"]["country"]}, Weather : {data["weather"][0]["main"]}, Temp : {int(data["main"]["temp"])}")
    else:
         messagebox.showinfo("Invalid entry","Invalid entry")
enter_button = tk.Button(root,text="Enter",font=("Arial", 15, "bold"),bg=MAIN_COLOR,fg="White",command=prt)
enter_button.place(x=120,y=170)

root.mainloop()