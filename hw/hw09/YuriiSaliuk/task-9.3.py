import tkinter as tk
from tkinter import font
from pyowm import OWM

HEIGHT = 350
WIDTH = 450
API_KEY = 'ef2206ff5da67de63306d0b143e20872'
owm = OWM(API_KEY)
mgr = owm.weather_manager()

def get_weather():
   city = entry_field.get()
   observation = mgr.weather_at_place(city)
   w = observation.weather
   wind = w.wind()
   temp = w.temperature('celsius')
   label["text"] =(f"Status:{w.detailed_status}"
                   f"\nWindspeed:{wind['speed']}"
                   f"\nWinddeg:{wind['deg']}"
                   f"\nWindgust:{wind['gust']}"
                   f"\nTemp:{temp['temp']}"
                   f"\nTempMin:{temp['temp_min']}"
                   f"\nTempMax:{temp['temp_max']}"
                   f"\nHumidity:{w.humidity}"
                   f"\nRain:{w.rain}"
                   f"\nHeat:{w.heat_index}"
                   f"\nClouds:{w.clouds}")
 

root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()



frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.7, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)



root.mainloop()