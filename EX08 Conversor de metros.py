#Conversor de metros para centímetros e milímetros 
 
metros = int(input('Qual a metragem a ser convertida?'))
print('Para {}m temos {} centímetros e {} milímetros!' .format(metros, metros*100, metros*1000))

#Ou

metros = int(input('Qual a metragem a ser convertida?'))
cent = metros * 100
mili = metros * 1000
print('Para {}m temos {} centímetros e {} milímetros!' .format(metros, cent, mili))