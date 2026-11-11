def calcular_promedio(notas):
    # Pa q' no falle el codigo si esta vacío la lista, se puede usar el "if not notas:"
    if len(notas) == 0:
        return 0, 0, 0
    
    promedio = sum(notas) / len(notas)
    nota_min = min(notas)
    nota_max = max(notas)
    
    return promedio, nota_min, nota_max

def mostrar_resultado(nombre, notas):
    prom, min, max = calcular_promedio(notas)
    # Print resultadosñ
    print(f"REPORTE DE NOTAS: {nombre}")
    print(f"Notas ingresadas: {notas}")
    print(f"Nota máxima:    {max}")
    print(f"Nota mínima:    {min}")
    print(f"Promedio final: {prom:.2f}")

#Ejemplo
notas_alu = [16, 10, 12, 16, 19]
mostrar_resultado("Juan Reyes", notas_alu)