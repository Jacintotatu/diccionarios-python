favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
favorite_languages['maikel'] = 'java'
favorite_languages['tolomeo'] = 'c'
favorite_languages['edward'] = 'sql'
favorite_languages['phil'] = 'django'
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
