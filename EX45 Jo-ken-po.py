#Jokenpo

from random import choice

lista = ['pedra', 'papel', 'tesoura']
comp = choice(lista)
pessoa = str(input('Escolha: \n Pedra \n Papel \n Tesoura'))

if pessoa == 'Pedra' and comp == lista[0]:
    print('Empate')
elif pessoa == 'Pedra' and comp == lista[1]:
    print('O computador escolheu {}, você PERDEU!!!'.format(comp))
elif pessoa == 'Pedra' and comp == lista[2]:
    print('O computador escolheu {}, você GANHOU!!!'.format(comp))
elif pessoa == 'Papel' and comp == lista[1]:
    print('Empate')
elif pessoa == 'Pedra' and comp == lista[2]:
    print('O computador escolheu {}, você PERDEU!!!'.format(comp))
elif pessoa == 'Pedra' and comp == lista[0]:
    print('O computador escolheu {}, você GANHOU!!!'.format(comp))
elif pessoa == 'Tesoura' and comp == lista[2]:
    print('Empate')
elif pessoa == 'Pedra' and comp == lista[0]:
    print('O computador escolheu {}, você PERDEU!!!'.format(comp))
elif pessoa == 'Pedra' and comp == lista[1]:
    print('O computador escolheu {}, você GANHOU!!!'.format(comp))

