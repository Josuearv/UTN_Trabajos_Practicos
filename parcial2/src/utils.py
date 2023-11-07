# Lista de secuencias que representan genes mutantes
gens_mutan = ["A"*4, "T"*4, "C"*4, "G"*4]

# Función principal para determinar si hay un gen mutante en la secuencia de ADN
def is_mutan(adn):
    count_mutan_gen = 0

    # Llama a las funciones de búsqueda vertical y horizontal y suma sus resultados
    count_mutan_gen += vertical_search_gen(adn)
    count_mutan_gen += horizontal_search_gen(adn)
    count_mutan_gen += left_diagonal_search_gen(adn)
    count_mutan_gen+= right_diagonal_search_gen(adn)
    # Si hay más de un gen mutante, devuelve True, de lo contrario, devuelve False
    if count_mutan_gen > 1:
        return True
    else:
        return False

# Función para buscar genes mutantes en sentido vertical
def vertical_search_gen(adn):
    count = 0
    for i in range(6):
        column = ''
        for j in adn:
            # Construye la columna concatenando los elementos en la posición i
            column += j[i]
        # Comprueba si alguna secuencia mutante está presente en la columna
        for gen in gens_mutan:
            if gen in column:
                count += 1
    return count

# Función para buscar genes mutantes en sentido horizontal
def horizontal_search_gen(adn):
    count = 0
    for i in adn:
        # Comprueba si alguna secuencia mutante está presente en la fila
        for gen in gens_mutan:
            if gen in i:
                count += 1
    return count

# Función para buscar genes mutantes en diagonales hacia la izquierda
def left_diagonal_search_gen(adn):
    position = 0
    count = 0
    for i in range(len(adn)):
        decrement = 0
        diagonal = ""
        diagonal += adn[0][i]

        # Construye la diagonal hacia la izquierda concatenando los elementos en posiciones específicas
        if position != 0:
            for j in range(1, position + 1):
                if position - 1 != 0:
                    for k in range(position, position + 1):
                        decrement += 1
                        diagonal += adn[j][k - decrement]
                else:
                    diagonal += adn[j][position - 1]

        # Comprueba si alguna secuencia mutante está presente en la diagonal
        for gen in gens_mutan:
            if gen in diagonal:
                count += 1

        position += 1
    return count

# Función para buscar genes mutantes en diagonales hacia la derecha
def right_diagonal_search_gen(adn):
    columns = 6
    row = 1
    count = 0
    for i in range(len(adn) - 1, -1, -1):
        decrement = 5
        diagonal = ""
        diagonal += adn[0][i]
        # Construye la diagonal hacia la derecha concatenando los elementos en posiciones específicas
        if columns != 6:
            for j in range(1, row):
                diagonal += adn[j][decrement]
                decrement -= 1
        # Comprueba si alguna secuencia mutante está presente en la diagonal
        for gen in gens_mutan:
            if gen in diagonal:
                count += 1

        columns -= 1
        row += 1
    return count
