num_fav = {
    'pedro': [3, 8, 45, 13],
    'ana': [9, 11, 25, 56],
    'andres': [78, 57, 36, 65],
    'julai': [34, 98, 85, 74],
    'pepino': [21, 7, 14, 66],
    }

for nombres, numeros in num_fav.items():
    print(f"Los numeros favoritos de {nombres.title()} son: ")
    for numero in numeros:
        print(f"\t-     {numero}")









"""
print(f"El numero favorito de pedro es el {num_fav['pedro']}")
print(f"El numero favorito de ana es el {num_fav['ana']}")
print(f"El numero favorito de andres es el {num_fav['andres']}")
print(f"El numero favorito de julai es el {num_fav['julai']}")
print(f"El numero favorito de pepino es el {num_fav['pepino']}")
"""