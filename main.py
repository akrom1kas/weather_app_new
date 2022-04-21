import tkinter as tk
from tkinter import *
from tkinter import messagebox
import requests, base64
from PIL import Image, ImageTk
import datetime

# Api key
api_key = "421e28f9e40b05f6974d0fdc39099dec"

home = Tk()
home.geometry('400x400')
home.resizable(0, 0)
home.title('Orų programėlė')
home.configure(bg="#1e202b")

dt = datetime.datetime.now()

# Background image
img = Image.open('weather_icons/bg.jpg')
img = img.resize((600, 500), Image.ANTIALIAS)
img_photo = ImageTk.PhotoImage(img)
bg_lbl = tk.Label(home, image=img_photo)
bg_lbl.place(x=0, y=0, width=600, height=500)



def search():
    city = cit.get()
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
            citypressure = y["pressure"]
            cityhumidity = y["humidity"]
            icon_name = x['weather'][0]["icon"]
            cityweather_description = z[0]["description"]

            def get_icon_data(self):
                icon_id = x['weather'][0]["icon"]
                url = 'http://openweathermap.org/img/wn/{icon}.png'.format(icon=icon_id)
                response = requests.get(url, stream=True)
                return base64.encodebytes(response.raw.read())

            Label(home, font='Helvetica 24 bold', bg="#1e202b", foreground="red",text='' + str(round(citytemp)) + '°C').place(x=100, y=120)
            Label(home, font='Helvetica 12 bold', bg="#1e202b", foreground="white", text= cit.get() + ":" ' ' + str(cityname)).place(x=100, y=180)
            Label(home, font='Helvetica 12 bold', bg="#1e202b", foreground="white", text='Vėjo greitis: ' + str(citywind) + ' m/s').place(x=100, y=210)
            Label(home, font='Helvetica 12 bold', bg="#1e202b", foreground="white", text='Šiuo metu: ' + str(cityweather_description)).place(x=100, y=240)
            Label(home, font='Helvetica 12 bold', bg="#1e202b", foreground="white", text='Drėgmė: ' + str(cityhumidity)).place(x=100, y=270)
            Label(home, font='Helvetica 12 bold', bg="#1e202b", foreground="white", text='Atmosferos slėgis: ' + str(citypressure) + ' hPa').place(x=100, y=300)
            Label(home, font='Helvetica 12 bold', bg="#1e202b", foreground="white", text='Šiandien' ' ' + str(dt)).place(x=100, y=330)

cit = StringVar()

Label(home, font='Helvetica 12 bold', bg="#1e202b", foreground="white", text='Įveskite miestą :').place(x=130, y=10)
Entry(home, font='Helvetica 12 bold', bg="#1e202b", foreground="white", textvariable=cit).place(x=100, y=40)
Button(home, text='Vykdyti', font='Helvetica 10 bold', bg="#074986", foreground="white", command=search).place(x=160, y=80)


home.mainloop()