def somar(a, b):
    return a + b

def dividir(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida")
    return a / b

def isEven(a):
    return a % 2 == 0