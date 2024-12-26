#Somando números pares digitados

x = 0
for i in range (0,6):
    n = int(input('Digite um valor:'   ))
    if n % 2 == 0:
        x +=n
print (x)