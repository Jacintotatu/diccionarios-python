users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },

    }

users['mknigth'] = {'first': 'Michael', 'last': 'Knigth', 'location': 'E.E.U.U.',}
users['ijones'] = {'first': 'Indiana', 'last': 'Jones', 'location': 'reino unido',}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

        

    print(f"\t*-----Full name: {full_name.title()}.")
    print(f"\t*-----Location: {location.title()}.")
