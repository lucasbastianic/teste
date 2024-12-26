#exum = int(input("Digite um número"))
#print("Seu número é {}, seu antecessor é {} e seu sucessor é {}".format(exum, exum-1, exum+1))

#exdois = int(input("Digite um número"))
#print("Seu número é {}, o dobro é {} o tríplo é {} e a raiz é {}". format(exdois, exdois*2, exdois*2, exdois**(1/2)))

#nota1 = int(input("Digite a nota um"))
#nota2 = int(input("Digite a nota dois"))
#print("Sua média é {:.2f}".format((nota1+nota2)/2))

#exmetros = int(input("Digite os metros"))
#print("Em centímetros {}, em milimetros {}".format(exmetros*100, exmetros*1000))

#n = int(input("Digite seu dinheiro"))
#print("Você pode comprar {:.0f} dolar".format(n//3.27))

#largura = int(input("Digite a largura"))
#altura = int(input("Digite a altura"))
#area = largura * altura
#tinta = area / 2
#print("Sua área é {} e você vai precisar de {} baldes de tinta".format(area,tinta))

#preco = int(input("Digite o preco"))
#desconto = preco * 0.05
#descontoo = preco - desconto
#print(descontoo)

#salario = int(input("Digite o salário"))
#aumento = salario * 0.15
#aumentoo = salario + aumento
#print(aumentoo)

#temperatura = int(input("Digite a temperatura"))
#f = temperatura * 1.8 +32
#print(f)

#km = int(input("KM percorridos"))
#dias = int(input("Dias utilizados"))

#valor = (dias * 60) + (km * 0.15)
#print(valor)

#import math
#n = float(input("Digite um número"))
#print("Seu número é {}".format(math.floor(n)))

#a = float(input("CATETO OPOSTO"))
#b = float(input("CATETO ADJACENTE"))
#h = ((a**2) + (b**2)) ** (1/2)
#print(h)

#import math
#a = float(input("CATETO OPOSTO"))
#b = float(input("CATETO ADJACENTE"))
#c = math.hypot(a,b)
#print(c)


#import math
#a = int(input("Qual o angulo"))
#sin = math.sin(math.radians(a))
#cos = math.cos(math.radians(a))
#tan = math.tan(math.radians(a))
#print("seno {} cosseno {} tangente {}".format(sin, cos, tan))

#from random import choice
#a = str(input("Qual o primeiro aluno "))
#b = str(input("Qaul o segundo aluno "))
#c = str(input("Qaul o terceiro aluno "))
#d = str(input("Qaul o quarto aluno "))
#lista = [a,b,c,d]
#escolhido = choice(lista)
#print(escolhido)

#from random import shuffle
#a = str(input("Qual o primeiro nome"))
#b = str(input("Qual o segundo nome"))
#c = str(input("Qual o terceiro nome"))
#d = str(input("Qual o quarto nome"))
#lista = [a,b,c,d]
#shuffle(lista)
#print(lista)

#nome = str(input("Digite seu nome"))
#print(nome.upper())
#print(nome.lower())
    #print(len(nome.replace(" ","")))
    #print(len(nome) - nome.count(' '))
#split = nome.split()
#print(len(split[0]))

#numero = int(input("Qual o numero"))
# u = numero // 1 % 10
# d = numero // 10 % 10
# c = numero // 100 % 10 
# m = numero // 1000 % 10
#print(u)
#print(d)
#print(c)
#print(m)

#cid = str(input("Digite a cidade")).strip()
#captalize = cid.capitalize() 
#print(captalize[:5] == "Santo")

#nome = str(input("Qual seu nome completo")).strip()
#x = nome.title()
#print('Seu nome possui Silva? {}'.format('Silva' in x))]

#nome = str(input('Qual seu nome')).strip()
#x = nome.upper()
#print('A letra A aparece {} vezes na frase.'. format(x.count('A')))
#print('A primeira letra A aparece na posição {}'.format(x.find('A')+1))
#print('A primeira letra A aparece na posição {}'.format(x.rfind('A')+1))

#nome = str(input("Digite seu nome completo")).upper().strip()
#n = nome.split()
#print('Seu primeiro nome é {}'.format(n[0]))
#print('Seu ultimo nome é {}'.format(n[len(n)-1]))

#from random import randint
#numero = randint(0,5)
#escolha = int(input("Qual seu número"))
#if escolha == numero:
#    print("Você acertou")
#else:
#    print("Você errou")

#velocidade = int(input('Qual a velocidade'))
#if velocidade <= 80:
#    print('Você não foi multado')
#else:
#    print('Você foi multado, sua multa é {}'.format((velocidade - 80)*7))

#n = int(input('Qual o número'))
#if n % 2 == 0:
#    print('Seu número é par')
#else:
#    print('Seu número é impar')

#viagem = int(input("Qual o KM da viagem"))
#if viagem <= 200:
#    print('O valor da viagem é {}'.format(viagem * 0.5))
#else:
#    print('O valor da viagem é {}'.format(viagem * 0.45))

#ano = int(input('Qual ano você nasceu'))
#if ano % 4 == 0 and ano % 100 != 100 or ano % 400 ==0:
#    print('Ano bi')
#else:
#    print('Ano não bi')

#a = int(input('primeiro'))
#b = int(input('segundo'))
#c = int(input('terceiro'))
#menor = a 
#if b < a and b < c:
#    menor = b
#if c < a and c < b:
#   menor = c
#maior = a
#if b > a and b > c:
#    maior = b
#if c > a and c > b:
#    maior = c
#print('O menor valor foi {} e o maior foi {}'. format(menor, maior))

#salario = int(input('Qual o salario'))
#if salario <= 1250:
#    print('O novo salário é {}'.format(salario * 15 / 100))
#else:
#    print('O novo salario é {}'.format(salario * 10 / 100))

#a = int(input('Primeiro'))
#b = int(input('Segundo'))
#c = int(input('Terceiro'))

#if a+b > c and a+c > b and b+c > a:
#    print('Da pra criar')
#else:
#    print('Não da')


#from time import sleep
# = 0

#while x <= 60:
#    x +=1
#    sleep(0.01)
#    print(x)

from time import sleep

print('\33[33m-=-'*30 + '\33[m')
print('\33[34m-=-'*11 + '   Bem vindos ao Game   ' + '-=-'*11 + '\33[m')
print('\33[33m-=-'*30 + '\33[m')

print('Vamos começar seu cadastro!')

email = ''

while '@' not in email or '.com' not in email:
    email = str(input('Digite seu e-mail:   ')).lower()
    print('\33[34m Processando ...' + '\33[m')
    sleep(1)
    if '@' not in email or '.com' not in email:
        print('\33[31m E-mail incorreto, preencha algo como: xxxxxxx@xxx.com  \33[m')

remail = ''
while remail != email:
    remail = str(input('Confirme seu e-mail:   ')).lower()
    print('\33[34m Processando ...' + '\33[m')
    sleep(1)   
    if remail != email:
        print('\33[31m O e-mail deve ser identico ao digitado anteriormente  \33[m')

nome = str(input('Digite seu nome:   ')).title()
user = str(input('Digite seu usuário para login:   ')).lower()

print('\33[33m Carregando 🕑' + '\33[m')
sleep(2)

print('Vamos definir uma senha.')
print('\33[36m Sua senha deve conter no mínimo 8 caracteres, uma maiúscula e minúscula, um dígito e um caracter especial \33[m')

def validar_senha(senha):
    if len(senha) < 8:
        return "\33[31mSenha muito curta! Deve ter pelo menos 8 caracteres.\33[m"
    if not any(char.isdigit() for char in senha):
        return "\33[31mSenha deve conter pelo menos um número.\33[m"
    if not any(char.isupper() for char in senha):
        return "\33[31mSenha deve conter pelo menos uma letra maiúscula.\33[m"
    if not any(char.islower() for char in senha):
        return "\33[31mSenha deve conter pelo menos uma letra minúscula.\33[m"
    if not any(char in "!@#$%^&*()-_+=<>?/" for char in senha):
        return "\33[31mSenha deve conter pelo menos um caractere especial.\33[m"
    return "Senha válida!"  # Retorno fixado para comparação no loop

senha = ""
while True:  # Loop infinito até a senha ser válida
    senha = input("Digite sua senha:   ")
    resultado = validar_senha(senha)
    if resultado == "Senha válida!":
        print("\33[34mSenha salva!\33[m")  # Mensagem para senha válida
        repeatsenha = ''
        while repeatsenha != senha:
            repeatsenha = str(input('Confirme sua senha:   '))
            print('\33[34m Processando ...' + '\33[m')
            sleep(1)   
            if repeatsenha != senha:
                print('\33[31m A senha deve ser a mesma digitada anteriormente  \33[m')
        print('Vamos realizar seu primeiro login')
        sleep(3)
        break  # Sai do loop se a senha for válida
    else:
        print(resultado)  # Mostra o erro e continua pedindo

print('.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n')

luser = str(input('Digite seu usuário:   '))
lsenha = ''

if luser == user:
    while lsenha != senha:
        lsenha = input('Digite sua senha:   ')
        print('\33[34m Processando ...' + '\33[m')
        sleep(1)
        if lsenha != senha:
            print('\33[31m Senha incorreta, tente novamente:   \33[m')

if luser == user:
    print('Bem vindo(a) {}!' .format(nome))

        






