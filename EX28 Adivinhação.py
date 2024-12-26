#Jogo de adivinhação

from random import randint
from time import sleep

print('\033[33m' '-=-' * 20 +'\033[m')
print('\033[34m' 'Vou pensar em um número entre 0 e 5. Tente adivinhar...' + '\033[m')
print('\033[33m' '-=-' * 20 +'\033[m')

n = randint(0,5)

resp = int(input('Em que número eu pensei?'))
print('PROCESSANDO...')

sleep(2)

if resp == n:
    print('Você ganhou')
else:
    print('Você perdeu')

