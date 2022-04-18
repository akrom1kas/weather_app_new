
from tkinter import *
from tkinter import messagebox
import requests, base64

api_key = "421e28f9e40b05f6974d0fdc39099dec"
class OpenWeatherMap:
    APPID = 'c73d9cdb31fd6a386bee66158b116cd0'
home = Tk()
home.geometry('400x350')
home.resizable(0, 0)
home.title('Orų programėlė')
home.configure(bg="#1e202b")


def get_icon_data(self):
    icon_id = x['weather'][0]['icon']
    url = 'http://openweathermap.org/img/wn/{icon}.png'.format(icon=icon_id)
    response = requests.get(url, stream=True)
    return base64.encodebytes(response.raw.read())

class HomeconLabel(Tk):
    def __init__(self, parent, **kwargs):
        weather_icon = kwargs.pop('weather_icons', None)
        if weather_icon is not None:
            self.photo = tk.PhotoImage(data=weather_icon)
            kwargs['image'] = self.photo

        super().__init__(parent, **kwargs)
    
def search():
    city = cit.get()
    if city == '':
        return messagebox.showerror('Klaida', 'įveskite miestą')
    elif api_key == 'įveskite api raktą':
        return messagebox.showerror('Klaida', 'įveskite savo api raktą')
    else:
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        cityname = city
        lang = 'lt'
        units = 'Metric'
        complete_url = base_url + "appid=" + api_key + '&units=' + units + '&lang=' + lang + "&q=" + cityname
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            z = x["weather"]
            cityname = x["sys"]["country"]
            citywind = x["wind"]["speed"]
            citytemp = y["temp"]
            citypressure = y["pressure"]
            cityhumidiy = y["humidity"]
            # cityicon = x['weather'][0]["icon"]
            cityweather_description = z[0]["description"]



            Label(home, font='Helvetica 12 bold', bg="#1e202b", foreground="white", text= cit.get() + ":" + str(cityname)).place(x=100, y=180)
            Label(home, font='Helvetica 24 bold', bg="#1e202b", foreground="red", text='' + str(round(citytemp)) + '°C').place(x=100, y=120)
            Label(home, font='Helvetica 12 bold', bg="#1e202b", foreground="white", text='Vėjo greitis: ' + str(citywind) + ' m/s').place(x=100, y=210)
            Label(home, font='Helvetica 12 bold', bg="#1e202b", foreground="white", text='Šiuo metu: ' + str(cityweather_description)).place(x=100, y=240)
            Label(home, font='Helvetica 12 bold', bg="#1e202b", foreground="white", text='Drėgmė: ' + str(cityhumidiy)).place(x=100, y=270)
            Label(home, font='Helvetica 12 bold', bg="#1e202b", foreground="white", text='Atmosferos slėgis: ' + str(citypressure) + ' hPa').place(x=100, y=300)
            temp_icon = homeconLabel(weather_icon=owm.get_icon_data())
            temp_icon.grid(row=0, column=0)

cit = StringVar()

Label(home, font='Helvetica 12 bold', bg="#1e202b", foreground="white", text='Įveskite miestą :').place(x=130, y=10)
Entry(home, font='Helvetica 12 bold', bg="#1e202b", foreground="white", textvariable=cit).place(x=100, y=40)
Button(home, text='Vykdyti', font='Helvetica 10 bold', bg="#074986", foreground="white", command=search).place(x=160, y=80)


home.mainloop()