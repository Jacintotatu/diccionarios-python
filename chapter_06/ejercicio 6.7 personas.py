personas = {
    'ind1': {
    'nombre': 'Jacinto',
    'apellido': 'Conesa',
    'edad': 46,
    "ciudad": 'Cartagena'
    },

    'ind2': {
    'nombre': 'Pedro',
    'apellido': 'Guachi',
    'edad': 24,
    "ciudad": 'Perin'
    },

    'ind3': {
    'nombre': 'Maikel',
    'apellido': 'Moreno',
    'edad': 37,
    "ciudad": 'Benidorm'
    },

    }

for i,ind in personas.items():
    print(f'\nUsuario: {i}')
    nombre_completo = f"{ind['nombre']} {ind['apellido']}"
    años = ind['edad']
    localidad = ind['ciudad']

    print(f"\tNombre completo: {nombre_completo.title()}")
    print(f"\tEdad: {años}")
    print(f"\tCiudad: {localidad.title()}")
