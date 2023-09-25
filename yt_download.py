import youtube_dl

# Ingresar la URL para descargar
url = input("Ingresa la URL del video: ")

ydl_opts = {}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("¡Video descargado exitosamente!")