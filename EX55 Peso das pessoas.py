#Mostrando quem é mais pesado e mais leve

menor = 0
maior = 0

for p in range (0,5):
    peso = int(input('Qual o peso?   '))
    if p == 1:
        maior = p
        menor = p
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(menor)
print(maior)