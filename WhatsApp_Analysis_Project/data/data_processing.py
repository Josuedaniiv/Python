def read_chat_file(file_path = '/home/TuUsuario/Directorio/WhatsApp_Analysis_Project/data/chat.txt'):
    with open(file_path, 'r', encoding='utf-8') as file:
        chat_data = file.readlines()
    return chat_data


def process_chat_data(chat_data):
    processed_data = []
    for line in chat_data:
        # Aquí puedes realizar el procesamiento específico según el formato de tu archivo de chat
        # Puedes extraer el nombre del remitente, la fecha, el mensaje, etc., utilizando expresiones regulares o métodos de manipulación de cadenas
        # Por ejemplo:
        # processed_line = process_line(line)
        # processed_data.append(processed_line)
        pass
    return processed_data


def main():
    file_path = 'data/chat.txt'  # Ruta al archivo de chat
    chat_data = read_chat_file(file_path)
    processed_data = process_chat_data(chat_data)
    
    # Aquí puedes realizar más operaciones con los datos procesados, como el análisis, la visualización, etc.
    # Puedes utilizar bibliotecas como Pandas y Matplotlib para facilitar estas tareas

    # Ejemplo: Imprimir los primeros 10 mensajes procesados
    for line in processed_data[:10]:
        print(line)


if __name__ == "__main__":
    main()