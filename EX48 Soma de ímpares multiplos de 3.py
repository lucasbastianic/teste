#Contagem de todos números impares múltiplos de 3

x = 0 
for i in range (0, 501):
    if i % 2 != 0 and i % 3 == 0:
        x += i
print (x)
        