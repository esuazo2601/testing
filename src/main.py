import sys
import datetime
hora_actual = datetime.datetime.now().hour
def ohce(mensaje):
    return f'{mensaje} {sys.argv[1]}!' 