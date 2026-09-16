def promedio(numeros):
    total = sum(numeros)
    n = len(numeros)
    return total / n if n else 0


print(promedio([10, 20, 30]))