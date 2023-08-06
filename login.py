from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Ruta de inicio de sesión
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Verificar las credenciales del usuario (aquí puedes agregar tu lógica de autenticación)
        username = request.form['username']
        password = request.form['password']

        # Lógica de autenticación (ejemplo básico)
        if username == 'usuario' and password == 'contraseña':
            # Si las credenciales son válidas, redirige al panel de control o página de inicio
            return redirect(url_for('dashboard'))
        else:
            # Si las credenciales son inválidas, muestra un mensaje de error
            error = 'Credenciales inválidas. Por favor, intenta de nuevo.'
            return render_template('login.html', error=error)

    # Si es una solicitud GET, muestra el formulario de inicio de sesión
    return render_template('login.html')

# Ruta del panel de control o página de inicio
@app.route('/dashboard')
def dashboard():
    # Verificar si el usuario está autenticado (puedes agregar tu propia lógica de autenticación aquí)
    # Si el usuario no está autenticado, redirigir al formulario de inicio de sesión
    # De lo contrario, mostrar el panel de control o página de inicio
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run()