import sys

def main_input(name):
    while(1):
        entrada = input()
        if entrada == "Stop!":
            print (f"Adios {name}")
            return 0


def ohce(hora_actual):
    if  len(sys.argv) > 0:
        nombre = sys.argv[1]
        if hora_actual >= 6 and hora_actual <= 12:
            print (f'¡Buenos días {sys.argv[1]}!')
        elif hora_actual > 12 and hora_actual < 20:
            print (f'¡Buenas tardes {sys.argv[1]}!')
        else:
            print (f'¡Buenas noches {sys.argv[1]}!')

        main_input(nombre)
      
if __name__ == "__main__":
   ohce(17)

