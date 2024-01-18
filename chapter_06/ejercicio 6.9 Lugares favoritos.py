lugares_favoritos = {
    'tarantino': ['california', 'san francico', 'mexico'],
    'michael': ['perin', 'santa barbara', 'tayante'],
    'brad': ['los angeles', 'calasparra', 'cehegín'],
}

for amigo, ciudades in lugares_favoritos.items():
    print(f"\nLas ciudades favoritas de {amigo.title()} son: ")
    for ciudad in ciudades:
        if amigo == 'tarantino':

            print(f"\t*  {ciudad[1]}")