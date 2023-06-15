import socket

try:
    url = input("https://trainme.trainme-staging.com/")
    direccion_ip = socket.gethostbyname(url)
    print(f"La dirección IP de {url} es: {direccion_ip}")
except socket.gaierror:
    print("Error: No se pudo resolver la dirección de la página web. Asegúrese de que la URL sea válida y de que tenga una conexión a Internet activa.")