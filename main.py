import requests as re
import tkinter as tk
from tkinter import messagebox

API_KEY = "9acd0597ae349fa651ff17893ec5b7e2"



root = tk.Tk()
root.title('Weather App')
root.geometry("300x300")

title = tk.Label(root,text="Weather App",font=("Arial", 20, "bold"))
title.place(x=65,y=50)

city_entry = tk.Entry(root, font=("Arial", 18))
city_entry.place(x=20,y=110)

def prt():
    city = city_entry.get()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = re.get(url)
    data = response.json()
    messagebox.showinfo(f"Weather",f"Country : {data["sys"]["country"]}, Weather : {data["weather"][0]["main"]}, Temp : {int(data["main"]["temp"])}")

enter_button = tk.Button(root,text="Enter",font=("Arial", 15, "bold"),command=prt)
enter_button.place(x=125,y=170)

root.mainloop()