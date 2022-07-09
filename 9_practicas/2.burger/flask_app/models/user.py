from curses import flash
import re	# el módulo regex
# crea un objeto de expresión regular que usaremos más adelante
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class User:
    @staticmethod
    def validate_user( user ):
        is_valid = True
        # prueba si un campo coincide con el patrón
        if not EMAIL_REGEX.match(user['email']): 
            flash ("Invalid email address!")
            is_valid = False
        return is_valid