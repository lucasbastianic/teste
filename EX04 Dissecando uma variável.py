#Dissecando uma variável

palavra = str(input('Digite algo'))
print('O tipo primitivo dessa palavra é {}'.format(type(palavra)))
print('Só tem espaços?', palavra.isspace())
print('É um número?', palavra.isnumeric())
print('É alfabético?', palavra.isalpha())
print('É alfanumérico?' ,palavra.isalnum())
print('Está em maiúsculas?' ,palavra.isupper())
print('Está em minúsculas?' ,palavra.islower())
print('Está capitalizada?', palavra.istitle())