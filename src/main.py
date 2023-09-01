import sys

def main_input(name):
    entrada = input()
    if entrada == "Stop!":
        return f"Adios {name}"


def ohce(hora_actual):
    if  len(sys.argv) > 0:
        if hora_actual >= 6 and hora_actual <= 12:
            return f'¡Buenos días {sys.argv[1]}!'
        elif hora_actual > 12 and hora_actual < 20:
            return f'¡Buenas tardes {sys.argv[1]}!'
        else:
            return f'¡Buenas noches {sys.argv[1]}!'
    

""" if __name__ == "__main__":
   print (main_input("Gustavo"))
 """
