#Desconto de 5% no produto 
 
preco = float(input('Qual o preço do produto?'))
print('O valor do produto com desconto fica {}'.format(preco - (preco * 0.05)))

#Ou

preco = float(input('Qual o preço do produto?'))
print('O valor do produto com desconto fica {}'.format(preco - (preco * 5 / 100)))

#Ou 

preco = float(input('Qual o preço do produto?'))
desconto = preco - (preco * 0.05)
print('O valor do produto com desconto fica {}'.format(desconto))

#Ou 

preco = float(input('Qual o preço do produto?'))
desconto = preco - (preco * 5 / 100)
print('O valor do produto com desconto fica {}'.format(desconto))
