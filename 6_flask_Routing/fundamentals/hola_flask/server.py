from flask import Flask  # Importa Flask para permitirnos crear nuestra aplicación

app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def hola_mundo():
    return 'Hola Mundo!'  # Devuelve la cadena '¡Hola Mundo!' como respuesta

# sentencias import, tal vez algunas otras rutas
    
@app.route('/dojo')
def success():
    return "dojo!"

# # app.run(debug=True) debería ser la última sentencia 


@app.route('/say/<name>') # para una ruta '/hola /____' cualquier cosa después de que '/hola/' se pase como una variable 'name'
def say_name(name):
    return f"Hi {name.capitalize()}"

@app.route('/repeat/<int:num>/<string:word>') # para una ruta '/users/____/____', dos parámetros en la url se pasan como nombre de usuario e id
def repeat_word(num, word):
    output = ''

    for i in range (0, num):
        output += f"<p>{word}</p>"

    return output

if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración