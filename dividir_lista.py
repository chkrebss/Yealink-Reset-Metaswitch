def dividir_lista(lista):
    sublistas = [[] for _ in range(10)]  # Crear 10 sublistas vacías
    for i, elemento in enumerate(lista):
        sublistas[i % 10].append(elemento)  # Asignar el elemento a la sublista correspondiente
    return sublistas
