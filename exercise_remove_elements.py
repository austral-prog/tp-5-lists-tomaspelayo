# Ejercicio 4: Remover elementos en posiciones específicas

def remove_elements(lista):
    """
    Remueve el primer, quinto y sexto elemento de la lista.
    La función debe funcionar con listas de cualquier tamaño.

    Args:
        lista: Una lista de elementos

    Returns:
        La lista después de remover los elementos indicados
    """
    if len(lista) == 6:
        del lista[-2]
        del lista[-1]
        del lista[0]

    elif len(lista) > 6:
        del lista[0]
        del lista[3]
        del lista[3]

    elif len(lista) == 5:
        del lista[0]
        del lista[4]

    elif len(lista) == 0:
        return lista

    elif len(lista) > 0 and len(lista) <= 4:
        del lista[0]

    return lista
