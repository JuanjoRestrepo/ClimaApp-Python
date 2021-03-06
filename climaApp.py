from tkinter import *
import requests

#bd070f6f9b842c11c7dd46db13e6570a
#api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}

def mostrar_respuesta(clima):
    try:
        nombre_ciudad = clima["name"]
        desc = clima["weather"][0]["description"]
        temp = clima["main"]["temp"]

        ciudad["text"] = nombre_ciudad
        temperatura["text"] = str(int(temp)) + "°C"
        descripcion["text"] = desc
    except:
        ciudad["text"] = "Intenta nuevamente"

def clima_JSON(ciudad):
    try:
        API_key = "bd070f6f9b842c11c7dd46db13e6570a"
        URL = "https://api.openweathermap.org/data/2.5/weather"
        parametros = {"APPID" : API_key, "q": ciudad, "units": "metric", "lang": "es"}
        response = requests.get(URL, params = parametros)
        clima = response.json()
        mostrar_respuesta(clima)
    except:
        print("ERROR")

    
    
    
ventana = Tk()
ventana.geometry("350x550")

texto_ciudad = Entry(ventana, font = ("Courier", 20, "normal"), justify = "center") 
texto_ciudad.pack(padx = 30, pady = 30)

obtener_clima = Button(ventana, text="Obtener Clima", font = ("Courier", 20, "normal"), command = lambda: clima_JSON(texto_ciudad.get()))
obtener_clima.pack()

ciudad = Label(font = ("Courier", 20, "normal"))
ciudad.pack(padx = 20, pady = 20)

temperatura = Label(font = ("Courier", 50, "normal"))
temperatura.pack(padx = 10, pady = 10)

descripcion = Label(font = ("Courier", 20, "normal"))
descripcion.pack(padx = 10, pady = 10)


ventana.mainloop()
