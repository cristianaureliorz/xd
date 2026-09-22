def es_par(numero):
    return numero % 2 == 0

def mostrar_paridad(numero):
    if es_par(numero):
        print(f"El numero {numero} es PAR.")
    else:
        print(f"El numero {numero} es IMPAR.")


# Ingreso por el usuario
num = int(input("Ingresa un numero entero: "))
mostrar_paridad(num)