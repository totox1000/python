from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    users = [
        {'first_name' : 'Andres', 'last_name' : 'Becerra'},
        {'first_name' : 'Patricio', 'last_name' : 'Olivares'},
        {'first_name' : 'Vicente ', 'last_name' : 'Herrera'},
        {'first_name' : 'Marcelo', 'last_name' : 'Argotti'}
    ]
    return render_template("index.html",users=users)

if __name__=="__main__":
    app.run(debug=True)