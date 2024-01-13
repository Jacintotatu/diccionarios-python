rios = {
    'Egipto': 'Nilo',
    'EEUU': 'Mississippi',
    'Brasil': 'Amazonas',
    'Londres': 'Tamesis',
    }

for city,rio in rios.items():
    print(f'Por {city} discurre el rio {rio}.')

for city in rios.keys():
    print(city)

for rio in rios.values():
    print(rio)