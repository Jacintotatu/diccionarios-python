nombres = ['rogelio', 'jen', 'maikel', 'sarah', 'edward', 'gorka', 'jesus', 'phil']

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for i in nombres:
    if i not in favorite_languages.keys():
        print(f'{i.title()}, no te olvides de participar en el sondeo.')
    else:
        print(f'{i.title()}, muchas gracias por participar.')
    
