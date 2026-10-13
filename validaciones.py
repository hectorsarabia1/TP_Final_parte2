def validar_rango(valor: int, min_val: int, max_val: int) -> bool:
    """
    Valida si un número está dentro de un rango
    
    """
    return min_val <= valor <= max_val

def es_par(numero: int) -> bool:
    """
    Valida si un número es par
    
    """
    if numero == 0:
        return True
    elif numero == 1 or numero == -1:
        return False
    elif numero > 0:
        return es_par(numero - 2)
    else:
        return es_par(numero + 2)

def es_primo(numero: int, divisor: int = None) -> bool:
    """
    Valida si un número es primo
    
    """
    if numero <= 1:
        return False
    if divisor is None:
        divisor = numero - 1
    if divisor == 1:
        return True
    if numero % divisor == 0:
        return False
    return es_primo(numero, divisor - 1)

def es_multiplo(numero: int, divisor: int) -> bool:
    """
    Valida si un número es múltiplo de otro
    
    """
    if divisor == 0:
        return False
    if numero == 0:
        return True
    if numero == divisor:
        return True
    elif numero < divisor:
        return False
    return es_multiplo(numero - divisor, divisor)