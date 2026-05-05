import tkinter as tk
from tkinter import font
from pyowm import OWM
import KEY

HEIGHT = 350
WIDTH = 450


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()



frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)


API_KEY = KEY.KEY

owm = OWM(API_KEY)
mgr = owm.weather_manager()

def weather_response(input_city):
    
    

    observation = mgr.weather_at_place(input_city)
    w = observation.weather
    values = [
        w.detailed_status,
        str(round(w.wind()['speed']*3.6)) + " km/h",
        str(w.humidity) + " %",
        str(w.temperature('celsius')['temp']) + " °C",
        str(w.rain.get('1h', 0)) + "mm",
        str(w.heat_index) if w.heat_index else "N/A",
        str(w.clouds) + " %"
    ]

    for i, val in enumerate(values):
        value_labels[i].config(text=val)
  
def get_weather(input_city):
    weather_response(input_city)


    # print(w.detailed_status)         # 'clouds'
    # print(w.wind())                  # {'speed': 4.6, 'deg': 330}
    # print(w.humidity)                # 87
    # print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    # print(w.rain)                    # {}
    # print(w.heat_index)              # None
    # print(w.clouds)                  # 75




button = tk.Button(frame, 
                   text="Get Weather", 
                   font=('Courier', 8, 'bold'),
                   relief="raised",
                   bd=3,  
                   command=lambda: get_weather(entry_field.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


# label = tk.Label(lower_frame, font=('Courier', 14))
# label.place(relx=0, rely=0, relwidth=1, relheight=1)

labels = ["Weather", "Wind", "Humidity", "Temperature", "Rain", "Heat Index", "Clouds"]

value_labels = []

for i, text in enumerate(labels):
    tk.Label(lower_frame, text=text + ":", anchor="w", width=12).grid(row=i, column=0, sticky="w")

    value = tk.Label(lower_frame, anchor="w", width=12)
    value.grid(row=i, column=1, sticky="w")

    value_labels.append(value)


root.mainloop()

