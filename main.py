"""
Um módulo é um arquivo contendo definições
e instruções Python que podem ser importados para
utilização de seus recursos.
https://docs.python.org/pt-br/3/tutorial/modules.html
"""

# from operacoes import *
# import operacoes from operacoes import * desaconselhavel utilizar importe apenas o que for utilizar pois se
# importar tudo sera rodado todo código importado from operacoes import somar, subtrair, multiplicar, nome_empresa
#
# print(multiplicar(1, 3))
# print(somar(1, 3))
# print(subtrair(1, 3))
# print(nome_empresa)
# print(__name__)

# # import estoque.produto
# from estoque.produto import cadastrar_produto
# produto = {'nome': 'Notebook', 'preco': 1200}
# cadastrar_produto(produto)

# from estoque.inventario import atualizar_quantidade_produto
# produto = {'nome': 'Notebook', 'quantidade': 100}
# atualizar_quantidade_produto(produto)

from estoque.utilidades.moeda import formatar_real

lista_produtos = [
    {'nome': 'Notebook', 'preco': 1200},
    {'nome': 'Xbox', 'preco': 3500.80},
    {'nome': 'Fone de Ouvido', 'preco': 99.90}
]

for produto in lista_produtos:
    nome = produto['nome']
    preco = formatar_real(produto['preco'])
    print(f'produto: {nome}, preco:{preco}')
