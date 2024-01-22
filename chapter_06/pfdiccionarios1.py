colores = {
    1 : "rojo",
    2 : "azul",
    3 : "verde",
    4 : "amarillo"
}

colores[5] = 'naranja'

for numero, color in colores.items():
    print(f"{numero} - {color.title()}")