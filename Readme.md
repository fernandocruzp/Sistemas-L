Interfaz gráfica para sistemas Lindenmayer.

Este proyecto consiste en una interfaz gráfica de usuario (GUI) en Python para generar y visualizar sistemas L utilizando la biblioteca tkinter para la interfaz y la biblioteca Turtle para dibujar los resultados de las gramáticas Lindenmayer.

Requerimientos:
python 3.1

Instalación
En la terminal instala las dependencias utilizando pip
pip install tk

Clona el repositorio con
git clone https://github.com/fernandocruzp/Sistemas-L

Uso

python GUI.py

Una vez iniciada la apliación se le mostraran los campos de Iteraciones, ángulo, axioma, regla 1, regla2, regla 3, regla4, regla5.

Ejemplo de uso

Iteraciones: 4
ángulo: 60
Axioma:FXF--FF--F
regla1:F=FF
regla2:X=--FXF++FXF++FXF--
regla3:
regla4:
regla5:

Esto dibujará un triángulo de Sierpinski

Indicaciones:
F indica forward, + giro a la derecha , - giro a la izquierda y B atrás. Demás literales serán utilizadas como constantes.
Las reglas deben estar escritas de la forma A=AB++A.

 Referencias
 Prusinkiewicz, P., & Hanan, J. (2016). Lindenmayer Systems, Fractals and Plants. Springer International Publishing. pp. 23-51.