def es_palindromo(cadena):
    # Eliminar espacios y convertir a minúsculas
    cadena = cadena.replace(" ", "").lower()
    
    # Comparar la cadena original con su inversa
    return cadena == cadena[::-1]


print(es_palindromo("radar"))  # True
print(es_palindromo("Anita lava la tina"))  # True
print(es_palindromo("Python"))  # False
print(es_palindromo("Hola mundo"))  # False