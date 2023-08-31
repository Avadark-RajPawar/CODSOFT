from tkinter import *
from configparser import ConfigParser
import requests
from tkinter import messagebox

Default = ("Arial", 20, "bold")
Times = ("Times", 16, "bold")

Green = '#37B61D'

url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

config_file = 'Config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['API_Key']['key']
print(api_key)


def get_weather(value):
    result = requests.get(url.format(value, api_key))
    if result:
        # print(result.content)
        json = result.json()
        city = json['name']
        country = json['sys']['country']
        temp_k = json['main']['temp']
        temp_c = temp_k - 273.15
        temp_f = temp_c * 9 / 5 + 32
        icon = json['weather'][0]['icon']
        weather = json['weather'][0]['main']
        final = (city, country, temp_c, temp_f, icon, weather)
        return final
    else:
        return None


def search():
    city = city_input.get()
    weather = get_weather(city)
    if weather:
        location['text'] = '{}, {}'.format(weather[0], weather[1])
        icon_image['file'] = 'Images/{}.png'.format(weather[4])
        temp['text'] = '{:.2f}°C, {:.2f}°F'.format(weather[2], weather[3])
        weather_info['text'] = '{}'.format(weather[5])
    else:
        messagebox.showerror('ERROR', 'Cannot find the city {}'.format(city))



window = Tk()
window.title("Weather App")
window.geometry("700x540")
window.resizable(width=False, height=False)

Icon = PhotoImage(file="Images/weather_icon.png")
window.iconphoto(False, Icon)

Top_frame = Frame(window, bg='#37B61D', width=100, height=110)
Top_frame.pack(fill=BOTH)

Heading = Label(window, text="WEATHER APP", font="ariel 30 bold", bg=Green)
Heading.place(x=200, y=30)

weather_image = PhotoImage(file='Images/weather_top.png')
Label(window, image=weather_image, bg=Green).place(x=100, y=30)

city_name = StringVar()
city_input = Entry(window, textvariable=city_name, font=('Times', 24), width=50)
city_input.pack(fill=BOTH, padx=50, pady=20)

search_btn = Button(window, text="Search", width=12, font=('Times', 14), fg='white', bg='#1CBADD', borderwidth=0, command=lambda: search())
search_btn.pack(pady=10)

location = Label(window, text="", font=Default)
location.pack()

icon_image = PhotoImage(file='')
Label(window, image=icon_image, bg='#CCEDFF').pack(pady=10)

temp = Label(window, text="", font=Times)
temp.pack(fill=BOTH, pady=10)

weather_info = Label(window, text="", font=Times)
weather_info.pack(fill=BOTH, pady=10)

window.mainloop()
