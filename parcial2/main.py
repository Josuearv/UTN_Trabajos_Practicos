# Importa la función is_mutant del módulo src.utils
from src.utils import is_mutan

# Define la función principal llamada run
def run():
    # Define las bases nitrogenadas
    nitrogen_base = ["A", "G", "T", "C"]
    
    # Inicializa variables
    input_size = 0
    adn = list()
    check_chain_adn = False

    # Ciclo para obtener 6 cadenas de ADN
    while input_size < 6:
        # Solicita al usuario que ingrese una cadena de ADN
        chain_adn = input(f'Digite la cadena N{input_size + 1} de ADN: ').upper()

        # Validación de la cadena de ADN
        while not check_chain_adn:
            count = 0
            for i in chain_adn:
                # Verifica si los caracteres son bases nitrogenadas
                if i not in nitrogen_base:
                    count += 1

            # Si hay caracteres no válidos, pide al usuario que ingrese la cadena nuevamente
            if count > 0:
                print('ERROR: Recuerda que las bases nitrogenadas son A, T, G, C')
                chain_adn = input('Digite de nuevo la cadena de ADN: ').upper()
            # Si la longitud no es 6, pide al usuario que ingrese la cadena nuevamente
            elif len(chain_adn) != 6:
                print('ERROR: Recuerda que la longitud de la cadena debe ser de 6')
                chain_adn = input('Digite de nuevo la cadena de ADN: ').upper()
            else:
                check_chain_adn = True

        # Agrega la cadena de ADN a la lista
        adn.append(chain_adn)

        # Incrementa el tamaño de entrada
        input_size += 1

    # Imprime la secuencia de ADN ingresada por el usuario
    print(f"La secuencia de ADN es:", adn)

    # Llama a la función is_mutant y muestra el resultado
    print('El resultado de si es mutante es:', is_mutan(adn))


# Se ejecuta la función run si este script es ejecutado directamente
if __name__ == '__main__':
    run()
