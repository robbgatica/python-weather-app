import tkinter as tk
import requests, os


def get_weather(city: str) -> None:
    weather_key = "Enter Your API Key Here"
    url = "http://api.openweathermap.org/data/2.5/weather?id="
    params = {"APPID": weather_key, "q": city, "units": "imperial"}
    response = requests.get(url, params=params)
    weather = response.json()
    label["text"] = format_response(weather)


def format_response(weather: "json") -> str:
    try:
        name = weather["name"]
        desc = weather["weather"][0]["description"]
        temp = str(weather["main"]["temp"])

        result = "City: {name} \nConditions: {desc} \nTemperature (F): {temp}".format(
            name=name, desc=desc, temp=temp
        )
    except:
        result = "Cannot retrieve that information"

    return result


def image_path(img_dir_name: str, img_file_name: str) -> "File Path":
    app_folder = os.path.dirname(__file__)
    image_folder = os.path.join(app_folder, img_dir_name)
    return os.path.join(image_folder, img_file_name)


# GUI
# Tkinter window size parameters
HEIGHT = 400
WIDTH = 400

root = tk.Tk()
root.title("Enter City for Current Weather")
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# Background Image
background = tk.PhotoImage(file=image_path("images", "sky.png"))
background_label = tk.Label(root, image=background)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#202024", bd=2)
frame.place(relx=0.5, rely=0.15, relwidth=0.75, relheight=0.1, anchor="n")

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root)
lower_frame.place(relx=0.5, rely=0.35, relwidth=0.75, relheight=0.35, anchor="n")

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()
