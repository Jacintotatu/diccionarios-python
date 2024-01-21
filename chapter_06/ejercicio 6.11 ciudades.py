ciudades = {
    'madrid': {
        'pais': 'españa',
        'poblacion': 40000000,
        'curiosidad': 'Es la capital de España',
        },

    'berlin': {
        'pais': 'alemania',
        'poblacion': 35000000,
        'curiosidad': 'Es la capital de Alemania',
        },
    'paris': {
        'pais': 'francia',
        'poblacion': 56000000,
        'curiosidad': 'Es la capital de Francia',
        },
    }
for ciudad,datos in ciudades.items():
    print(f"\nCiudad: {ciudad.title()}.")
    print(f"Pais: {datos['pais']}.")
    print(f"Población: {datos['poblacion']} habitantes.")
    print(f"Curiosidad: {datos['curiosidad']}.")

