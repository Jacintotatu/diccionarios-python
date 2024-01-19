lugares_favoritos = {
    'tarantino': ['california', 'san francico', 'mexico'],
    'michael': ['perin', 'santa barbara', 'tayante'],
    'brad': ['los angeles', 'calasparra', 'cehegín'],
}

for amigo, ciudades in lugares_favoritos.items():
    print(f"\nLas ciudades favoritas de {amigo.title()} son: ")
    for ciudad in ciudades:
        if amigo == 'tarantino' and ciudad == 'california':
            ciudad = 'California is the best'
        elif amigo == 'michael' and ciudad == 'tayante':
            ciudad = 'Tayante is the best'
        elif amigo == 'brad' and ciudad == 'calasparra':
            ciudad = 'Calasparra is the best'
            

        print(f"\t*  {ciudad.title()}")
