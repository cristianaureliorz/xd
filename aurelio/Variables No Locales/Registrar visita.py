visitas = 0  # Crea la variable global 'visitas' e inicia en 0.


def registrar_visita():  # Define la función.
    global visitas  # Permite modificar la variable 'visitas' de afuera.
    visitas += 1  # Suma 1 al contador global.
    print(f"Visita #{visitas} registrada") # Muestra la visita actual en consola.


registrar_visita()  # Primera llamada -> Incrementa a 1 e imprime "Visita #1 registrada".
registrar_visita()  # Segunda llamada -> Incrementa a 2 e imprime "Visita #2 registrada".

print(f"Total: {visitas}")  # Muestra el acumulado final -> Imprime "Total: 2".