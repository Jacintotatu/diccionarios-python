mascotas = {
    'cliente1': {
        'mascota': 'dinosaurio',
        'dueño': 'jaime'
        },

    'cliente2': {
        'mascota': 'critter',
        'dueño': 'tobias'
        },

    'cliente3': {
        'mascota': 'troll',
        'dueño': 'malaquias'
    },
}

for cliente, animal_info in mascotas.items():
    print(f"\nNombre de usuario: {cliente.title()}")
    nombre_mascota = animal_info['mascota']
    dueño = animal_info['dueño']

    print(f"\t* Nombre de mascota: {nombre_mascota.title()}")
    print(f"\t* Nombre del dueño: {dueño.title()}")



