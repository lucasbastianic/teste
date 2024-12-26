import requests

from bs4 import BeautifulSoup
request = requests.get("https://dolarhoje.com/")
conteudo = request.content

bsp_obj = BeautifulSoup(conteudo, "html.parser")

conteudo_dv_cotacao = bsp_obj.find("div", {"id": "cotacao"})
valor_do_dolar = conteudo_dv_cotacao.find("input", {"id": "nacional"})

valor_dolar_str = valor_do_dolar.get("value")
dolar = float(valor_dolar_str.replace(",", "."))

valor = float(input("Qual valor em R$ dejesa cotar?"))
print("Com {} você pode comprar {:.2f} dolars!" .format(valor, valor / dolar))
