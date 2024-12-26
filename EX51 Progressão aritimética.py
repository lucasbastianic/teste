#Calculando razão aritimética
termo = int(input('Qual o primeiro termo da PA?   '))
razao = int(input('Qual a razão da da PA?   '))
decimo = termo + (10-1) * razao
x = 0

for i in range (termo, decimo + razao, razao):
    x += i
print(x)