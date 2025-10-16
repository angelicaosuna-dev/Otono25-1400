"""
PROYECTO DE PROGRAMACIÓN: Funciones con cadenas, listas y diccionarios

Instrucciones:
Este archivo contiene varias tareas relacionadas con el uso de cadenas, listas y diccionarios.
Completa las tareas, terminando los tres TODO.

Puedes probar tus funciones utilizando el bloque "if __name__ == '__main__':" al final del archivo.
"""

# ============================
# TAREA 1: duplicado
# ============================

def duplicados(seq):
    """
    Devuelve True si hay elementos duplicados en la secuencia (lista o cadena), de lo contrario False.

    seq: lista o cadena

    Ejemplos:
    duplicados('hola') -> False #no tiene letras duplicadas
    duplicados('llama') -> True  #si tiene letras duplicadas
    """
    # TODO: Termina la funcion
    pass


# ============================
# TAREA 2: encontrar_repeticiones
# ============================

def encontrar_repeticiones(counter):
    """
    Devuelve una lista de claves cuyo valor en el diccionario es mayor que 1.

    counter: diccionario que asigna claves a contadores (por ejemplo, {'a': 3, 'b': 1})

    returns: lista de claves repetidas

    Ejemplo:
    encontrar_repeticiones({'a': 2, 'b': 1, 'c': 3}) -> ['a', 'c']
    """
    # TODO: Termina la funcion
    return []


# ============================
# TAREA 3: sumando_counters
# ============================

def suma_counters(dict1, dict2):
    """
    Combina dos diccionarios sumando los valores de las claves que aparecen en ambos.

    dict1, dict2: diccionarios con letras como claves y números como valores

    returns: nuevo diccionario combinado

    Ejemplo:
    dict1 = {'a': 2, 'b': 1}
    dict2 = {'a': 1, 'c': 4}
    sumando_counters(dict1, dict2) -> {'a': 3, 'b': 1, 'c': 4}
    """
    # TODO: Termina la funcion
    pass


# ============================
# is_interlocking
# ============================

def is_interlocking(word, word_list):
    """
    Devuelve True si la palabra se puede dividir en dos palabras válidas usando letras alternas.

    word: cadena a evaluar
    word_list: lista o conjunto de palabras válidas (por ejemplo, un diccionario en español)

    Ejemplo:
    is_interlocking('escolarizado', {'zapato', 'frío', 'es', 'colar', 'izado'}) -> True
    porque 'zapato' = word[0::2], 'frío' = word[1::2]

    Nota: Puedes asumir que las palabras del word_list están en minúsculas.

    Tip: Usa word[::2] y word[1::2] para obtener las dos mitades entrelazadas.
    """
   
    pass


# ============================
# FUNCION DE APOYO
# ============================

def contar_valores(word):
    """
    Cuenta cuántas veces aparece cada letra en una palabra.

    word: cadena

    returns: diccionario {letra: cantidad}

    Ejemplo:
    contar_valores('banana') -> {'b':1, 'a':3, 'n':2}
    """
    counter = {}
    for letter in word:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1
    return counter


# ============================
# PRUEBAS
# ============================

if __name__ == '__main__':
    # Puedes descomentar estas pruebas y añadir más para verificar tu código

    print("--- Pruebas de has_duplicates ---")
    print(duplicados('hola'))        # False
    print(duplicados('llama'))       # True

    print("\n--- Pruebas de find_repeats ---")
    test_counter = encontrar_repeticiones('banana')
    print(test_counter)  # {'b': 1, 'a': 3, 'n': 2}
    print(encontrar_repeticiones(test_counter))    # ['a', 'n']

    print("\n--- Pruebas de add_counters ---")
    c1 = encontrar_repeticiones('brontosaurios')
    c2 = encontrar_repeticiones('apatosaurios')
    print(suma_counters(c1, c2))

    print("\n--- Pruebas de is_interlocking ---")
    diccionario = {'zapato', 'frío', 'pato', 'cielo', 'dado'}
    print(is_interlocking('escolarizado', diccionario))  # True o False dependiendo del set

    # Agrega más pruebas según necesites
