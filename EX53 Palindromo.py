#Verificando se uma palavra é palíndromo

frase = str(input('Digite sua frase:   ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range (len(junto) -1, -1, -1):
    inverso += junto[letra]

if inverso == junto:
    print('Sua palavra é palíndromo')
else:
    print('Sua frase não é um palíndromo')