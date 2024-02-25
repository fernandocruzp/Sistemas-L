import tkinter as tk
import SystemaL as sistema


def iniciar():
    """
    Inicia el proceso de dibujo del sistema L con los valores ingresados por el usuario.
    """
    # Obtener los valores ingresados por el usuario desde los campos de entrada
    iteraciones = iteraciones_entry.get()
    angulo = angulo_entry.get()
    axioma = axioma_entry.get()
    regla1 = regla1_entry.get()
    regla2 = regla2_entry.get()
    regla3 = regla3_entry.get()
    regla4 = regla4_entry.get()
    regla5 = regla5_entry.get()

    # Obtener los valores procesados para el dibujo del sistema L
    valores = obtenerValores(iteraciones, angulo, axioma, regla1, regla2, regla3, regla4, regla5)

    # Iniciar el dibujo del sistema L
    sistema.dibuja(valores[0], valores[1], valores[2], valores[3])


def obtenerValores(iteraciones, angulo, axioma, regla1, regla2, regla3, regla4, regla5):
    """
    Procesa los valores ingresados por el usuario para el dibujo del sistema L.

    Args:
        iteraciones (str): Número de iteraciones.
        angulo (str): Ángulo de rotación.
        axioma (str): Axioma inicial.
        regla1 (str): Primera regla.
        regla2 (str): Segunda regla.
        regla3 (str): Tercera regla.
        regla4 (str): Cuarta regla.
        regla5 (str): Quinta regla.

    Returns:
        list: Lista que contiene el número de iteraciones, el ángulo, el axioma y las reglas procesadas.
    """
    valores = []
    reglas = {}

    # Procesar el número de iteraciones
    valores.append(5 if iteraciones == "" else int(iteraciones))

    # Procesar el ángulo
    valores.append(45 if angulo == "" else int(angulo))

    # Procesar el axioma
    valores.append("F" if axioma == "" else axioma)

    # Procesar las reglas
    for regla_entry in [regla1, regla2, regla3, regla4, regla5]:
        if regla_entry != "":
            regla = obtenRegla(regla_entry)
            reglas[regla[0]] = regla[1]

    valores.append(reglas)
    return valores


def obtenRegla(regla: str):
    """
    Obtiene una regla a partir de una cadena de entrada.

    Args:
        regla (str): Cadena que representa una regla en el formato "clave=valor".

    Returns:
        tuple: Tupla que contiene la clave y el valor de la regla.
    """
    return regla.split("=", 1)


# Crear la ventana principal
root = tk.Tk()
root.title("Sistemas L")

# Crear etiquetas y campos de entrada
tk.Label(root, text="Iteraciones:").grid(row=0, column=0)
iteraciones_entry = tk.Entry(root)
iteraciones_entry.grid(row=0, column=1)

tk.Label(root, text="Ángulo:").grid(row=1, column=0)
angulo_entry = tk.Entry(root)
angulo_entry.grid(row=1, column=1)

tk.Label(root, text="Axioma:").grid(row=2, column=0)
axioma_entry = tk.Entry(root)
axioma_entry.grid(row=2, column=1)

tk.Label(root, text="Regla 1:").grid(row=3, column=0)
regla1_entry = tk.Entry(root)
regla1_entry.grid(row=3, column=1)

tk.Label(root, text="Regla 2:").grid(row=4, column=0)
regla2_entry = tk.Entry(root)
regla2_entry.grid(row=4, column=1)

tk.Label(root, text="Regla 3:").grid(row=5, column=0)
regla3_entry = tk.Entry(root)
regla3_entry.grid(row=5, column=1)

tk.Label(root, text="Regla 4:").grid(row=6, column=0)
regla4_entry = tk.Entry(root)
regla4_entry.grid(row=6, column=1)

tk.Label(root, text="Regla 5:").grid(row=7, column=0)
regla5_entry = tk.Entry(root)
regla5_entry.grid(row=7, column=1)

# Botón de inicio
iniciar_button = tk.Button(root, text="Iniciar", command=iniciar)
iniciar_button.grid(row=8, columnspan=2)

# Ejecutar el bucle de eventos
root.mainloop()

