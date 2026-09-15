lista = [2, 8, 5, 3, 9, 4, 1]

# Empezamos desde la segunda posición porque el primer número ya se considera ordenado
for posicion in range(1, len(lista)):

    # Guardamos el número que vamos a colocar
    numero = lista[posicion]

    # Comenzamos a comparar con el número anterior
    comparar = posicion - 1

    # Mientras haya números para comparar y el número anterior sea mayor
    while comparar >= 0 and lista[comparar] > numero:

        # Movemos el número mayor una posición a la derecha
        lista[comparar + 1] = lista[comparar]

        # Retrocedemos para seguir comparando
        comparar = comparar - 1

    # Colocamos el número en su posición correcta
    lista[comparar + 1] = numero

    print("Pasada", posicion, ":", lista)

print("Lista ordenada:", lista) 