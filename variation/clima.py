import requests
import json

def obtener_reporte_clima(ciudad, unidad_temperatura):
    api_key = "TU_API_KEY"  # Reemplaza "TU_API_KEY" con tu clave de API real

    # Realiza una solicitud a la API del clima
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}"
    respuesta = requests.get(url)
    datos = respuesta.json()

    # Verifica si la solicitud fue exitosa
    if respuesta.status_code != 200 or "main" not in datos or "weather" not in datos:
        print("No se pudo obtener el informe del clima. Por favor, verifica la ciudad ingresada.")
        return

    # Extrae la información relevante del informe del clima
    temperatura_kelvin = datos["main"]["temp"]
    descripcion = datos["weather"][0]["description"]

    # Convierte la temperatura a la unidad especificada por el usuario
    if unidad_temperatura == "C":
        temperatura = temperatura_kelvin - 273.15
        unidad = "°C"
    elif unidad_temperatura == "F":
        temperatura = (temperatura_kelvin - 273.15) * 9/5 + 32
        unidad = "°F"
    else:
        temperatura = temperatura_kelvin
        unidad = "K"

    # Imprime el informe del clima
    print(f"Informe del clima para {ciudad}:")
    print(f"Temperatura: {temperatura:.2f}{unidad}")
    print(f"Descripción: {descripcion}")

# Solicita al usuario el nombre de la ciudad
ciudad = input("Ingrese el nombre de la ciudad: ")

# Solicita al usuario la unidad de temperatura deseada
unidad_temperatura = input("Ingrese la unidad de temperatura (C para Celsius, F para Fahrenheit, K para Kelvin): ")

# Obtiene y muestra el informe del clima
obtener_reporte_clima(ciudad, unidad_temperatura)