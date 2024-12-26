#Ocorrência de letras na frase

frase = str(input('Digite sua frase...')).strip().upper()
print('A letra A aparece {} vezes' .format(frase.count('A')))
print('A letra A aparece a primeira vez na posição {}' . format(frase.find('A')+1))
print('A letra A aparece a primeira vez na posição {}' . format(frase.rfind('A')+1))