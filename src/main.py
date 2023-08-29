import sys
import datetime

def ohce(hora_actual):
    if hora_actual >= 6 and hora_actual <= 12:
        return f'¡Buenos días {sys.argv[1]}!'
    elif hora_actual > 12 and hora_actual < 20:
        return f'¡Buenas tardes {sys.argv[1]}!'
    else:
        return f'¡Buenas noches {sys.argv[1]}!'