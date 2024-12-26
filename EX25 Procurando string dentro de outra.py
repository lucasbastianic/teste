#Procurando string

nome = str(input('Digite seu nome')).strip().title()
print('Analisando nome...')
print('Seu nome tem Silva? {}' .format('Silva' in nome))