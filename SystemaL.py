import turtle

pila=[]

def aplicacionReglas(entrada: str, reglas: dict) -> str:
    """
    Aplica las reglas del sistema L a la entrada dada.

    Args:
        entrada (str): La cadena de entrada.
        reglas (dict): Un diccionario que mapea caracteres a sus reemplazos.

    Returns:
        str: La cadena generada después de aplicar las reglas.
    """
    generacion= ''.join(reglas.get(caracter,caracter) for caracter in entrada)
    return generacion

def dibujarSistema(dibujante, generaciones: int, angulo: int, axioma: str, reglas: dict) -> None:
    """
    Dibuja el sistema L con las especificaciones dadas.

    Args:
        dibujante: Un objeto Turtle para dibujar.
        generaciones (int): El número de generaciones.
        angulo (int): El ángulo de rotación.
        axioma (str): El axioma inicial.
        reglas (dict): Un diccionario que mapea caracteres a sus reemplazos.

    Returns:
        None
    """
    res=axioma
    for i in range(generaciones):
        res=aplicacionReglas(res,reglas)
        print(res)
        for car in res:
            if car == "[":
                coordenada= dibujante.position()
                ang= dibujante.heading()
                pila.append((coordenada,ang))
            elif car == "]":
                tupla= pila.pop()
                dibujante.penup()
                dibujante.goto(tupla[0])
                dibujante.setheading(tupla[1])
                dibujante.pendown()
            else:
                if car == "F":
                    dibujante.forward(10)
                elif car == "+":
                    dibujante.right(angulo)
                elif car == "-":
                    dibujante.left(angulo)
                elif car == "B":
                    dibujante.backward(10)
                elif car == "0":
                    dibujante.color("brown")
                elif car == "1":
                    dibujante.color("green")
                elif car == "2":
                    dibujante.color("green")

def dibuja(generaciones: int, angulo: int, axioma: str, reglas: dict) -> None:
    """
    Dibuja el sistema L con las especificaciones dadas utilizando la biblioteca Turtle.

    Args:
        generaciones (int): El número de generaciones.
        angulo (int): El ángulo de rotación.
        axioma (str): El axioma inicial.
        reglas (dict): Un diccionario que mapea caracteres a sus reemplazos.

    Returns:
        None
    """
    dibujante = turtle.Turtle()
    dibujante.color("green")
    dibujante.speed(10)
    dibujante.penup()
    dibujante.goto(0, 0)
    dibujante.pendown()
    dibujarSistema(dibujante,generaciones,angulo,axioma,reglas)

