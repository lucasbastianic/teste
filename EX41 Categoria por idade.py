#Categorizando alunos por idade

from datetime import datetime

ano = int(input('Qual o ano do seu nascimento? '))
anoat = datetime.now().year

if anoat - ano <= 9:
    print('Categoria MIRIM')
elif anoat - ano <= 14:
    print('Categoria INFANTIL')
elif anoat - ano <= 19:
    print('Categoria JUNIOR')
elif anoat - ano == 25:
    print('Categoria SÊNIOR')
else:
    print('Categoria MASTER')
