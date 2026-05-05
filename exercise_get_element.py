# Ejercicio 2: Obtener elemento en posición específica

def get_element(lista, indice):
    """
    Retorna el elemento en la posición indicada.
    Si el índice está fuera de rango, retorna None.

    Args:
        lista: Una lista de cualquier tipo de elementos
        indice: Índice del elemento a obtener

    Returns:
        El elemento en la posición indicada o None si está fuera de rango
    """
    if indice >= len(lista):
        return None
    elif indice <= len(lista) and indice >= -len(lista):
        return lista[indice]
