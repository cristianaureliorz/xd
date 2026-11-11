def calcular_promedio(notas):
    #Sumar todas las notas de la lista
    #Dividir la suma entre la cantidad de notas para obtener el promedio
    promedio = sum(notas) / len(notas)
    
    #Obtener la nota más baja de la lista
    minima = min(notas)
    
    #Obtener la nota más alta de la lista
    maxima = max(notas)
    
    #Retornar los 3 valores juntos
    return promedio, minima, maxima


def mostrar_resultado(nombre, notas):
    #Llamar a calcular_promedio(notas) y desempaquetar la tupla que retorna
    # en 3 variables: prom (promedio), mn (mínima), mx (máxima)
    prom, mn, mx = calcular_promedio(notas)
    
    #Imprimir un encabezado con el nombre del alumno
    print(f"--- Reporte de {nombre} ---")
    
    #Imprimir la lista completa de notas ingresadas
    print(f"Notas: {notas}")
    
    #Imprimir el promedio con 2 decimales (:.2f)
    print(f"Promedio: {prom:.2f}")
    
    #Imprimir la nota mínima
    print(f"Nota mínima: {mn}")
    
    #Imprimir la nota máxima
    print(f"Nota máxima: {mx}")
    # Esta función NO tiene return: solo imprime en pantalla (función void)

#Pedir el nombre del alumno como texto
nombre_alumno = input("Ingrese el nombre del alumno: ")

#Pedir cuántas notas se van a ingresar, y convertirlo a entero
cantidad = int(input("¿Cuántas notas desea ingresar? "))

#Crear una lista vacía donde se guardarán las notas
lista_notas = []

#Repetir "cantidad" veces para pedir cada nota
for i in range(cantidad):
    #Pedir la nota al usuario y convertirla a float
    nota = float(input(f"Ingrese la nota {i + 1}: "))
    #Agregar la nota a la lista
    lista_notas.append(nota)

print()  #linea en blanco para separar

#Mostrar_resultado, que internamente usa calcular_promedio
mostrar_resultado(nombre_alumno, lista_notas)