
lista = '[<Tamanho: 1>, <Tamanho: 2>, <Tamanho: 3>, <Tamanho: 4>, <Tamanho: 5>, <Tamanho: 6>, <Tamanho: 7>, <Tamanho: 8>, <Tamanho: 9>, <Tamanho: 10>, <Tamanho: 11>, <Tamanho: 12>, <Tamanho: 13>, <Tamanho: 14>, <Tamanho: 15>, <Tamanho: 16>, <Tamanho: 17>, <Tamanho: 18>, <Tamanho: 19>, <Tamanho: 20>, <Tamanho: 21>, <Tamanho: 22>, <Tamanho: 23>, <Tamanho: 24>, <Tamanho: 25>, <Tamanho: 26>, <Tamanho: 27>, <Tamanho: 28>, <Tamanho: 29>, <Tamanho: 30>, <Tamanho: 31>, <Tamanho: 32>, <Tamanho: 33>]'

lista2 = lista.split('>, <Tamanho: ')

# '[<Tamanho: 1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33>]'

carac = '[<Tamanho: '
carac2 = '>]'
lista4 = []

for n in lista2:
    characters = "'!?"
    string = ''.join( x for x in n if x not in carac2 and n if x not in carac)
    lista4.append(string)

print(', '.join([m for m in lista4]))


