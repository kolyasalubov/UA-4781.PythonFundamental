import tkinter as tk
from pyowm import OWM

API_KEY = 'ef2206ff5da67de63306d0b143e20872'
owm = OWM(API_KEY)
mgr = owm.weather_manager()

def get_weather_data(city):
    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather
        temp = w.temperature('celsius')['temp']
        details = w.detailed_status
        humidity = w.humidity
        return f"Weather in {city}:\n{details.capitalize()}\nTemperature: {temp}°C\nHumidity: {humidity}%"
    except Exception:
        return "City not found or API error."

def on_button_click():
    city = entry_field.get()
    result = get_weather_data(city)
    label['text'] = result

root = tk.Tk()
root.title("Weather Application")

canvas = tk.Canvas(root, height=350, width=450)
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", bg="gray", fg="white", 
                   font=('Courier', 8), command=on_button_click)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14), justify='left')
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()