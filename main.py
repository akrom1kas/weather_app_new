import tkinter as tk
from tkinter import *
from tkinter import messagebox
import requests
import time

# Api key
api_key = "421e28f9e40b05f6974d0fdc39099dec"

# Window Settings
home = Tk()
home.geometry('900x500')
home.resizable(0, 0)
home.title('Orų programėlė')
home.configure(bg="#f0f0f0")
dt = time.strftime("%H:%M")

# # Background image
home.iconbitmap('sunrise.ico')

def search():
    city = textfield.get()
    if city == '':
        return messagebox.showerror('Klaida', 'įveskite miestą')
    else:
        url = "http://api.openweathermap.org/data/2.5/weather?"
        cityname = city
        lang = 'lt'
        units = 'Metric'
        complete_url = url + "appid=" + api_key + '&units=' + units + '&lang=' + lang + "&q=" + cityname
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] :
            y = x["main"]
            z = x["weather"]
            cityname = x["sys"]["country"]
            citywind = x["wind"]["speed"]
            citytemp = y["temp"]
            cityweather_description = z[0]["description"]

            Label1=Label(home, font='Helvetica 52 bold', bg="#f0f0f0", foreground="red",text='' + str(round(citytemp)) + '°C')
            Label1.place(x=30, y=150)
            Label2=Label(home, font='Helvetica 21 bold', bg="#f0f0f0", text= textfield.get() +  ":"  ' ' + str(cityname))
            Label2.place(x=390, y=180)
            Label3=Label(home, font='Helvetica 21 bold', bg="#f0f0f0", text='Vėjas' + ":" ' '  + str(citywind) + ' m/s')
            Label3.place(x=390, y=260)
            Label4=Label(home, font='Helvetica 21 bold', bg="#f0f0f0", text='Šiuo metu' + ":" ' '  + str(cityweather_description))
            Label4.place(x=390, y=220)
            Label5 = Label(home, font='Helvetica 21 bold', bg="#f0f0f0", text='Šiandien' + ":"' ' + str(dt))
            Label5.place(x=390, y=300)

w=Label(text="Šiandien:", font=("arial", 20, "bold"))
w.place(x=390, y=300)
b=Label(text="Šiuo metu:", font=("arial", 20, "bold"))
b.place(x=390, y=220)
r=Label(text="Vėjas:", font=("arial", 20, "bold"))
r.place(x=390, y=260)
q=Label(text="Miestas:", font=("arial", 20, "bold"))
q.place(x=390, y=180)

Search_image=PhotoImage(file="search.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(home, justify="center", width=17, font=("poppins", 25, "bold"),bg="#404040", border=0,fg="white",)
textfield.place(x=50, y=40)
textfield.focus()

Search_icon=PhotoImage(file="search_icon.png")
myimage_icon=Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040",command=search)
myimage_icon.place(x=400, y=34)

Weather_icon=PhotoImage(file="logoweather.png")
myimage=Label(image=Weather_icon)
myimage.place(x=150,y=150)



home.mainloop()