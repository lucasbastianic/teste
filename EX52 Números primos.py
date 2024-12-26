#Verificando se é um número primo

n1 = int(input('Qual seu número? '))
if n1 > 1:  
    for i in range(2, n1):
        if n1 % i == 0:  
            print('Número não primo')
            break
    else:
        print('Número primo')
else:
    print('Número não primo')