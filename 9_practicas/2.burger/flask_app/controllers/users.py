from flask_app.models.user import User

@app.route('/register', methods=['POST'])

def register():
    if not User.validate_user(request.form):
        # redirigimos a la plantilla con el formulario
        return redirect('/')
# ...hacer otras cosas
    return redirect ('/dashboard')
