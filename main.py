"""
Um módulo é um arquivo contendo definições
e instruções Python que podem ser importados para
utilização de seus recursos.
https://docs.python.org/pt-br/3/tutorial/modules.html
"""

from operacoes import *
# import operacoes from operacoes import * desaconselhavel utilizar importe apenas o que for utilizar pois se
# importar tudo sera rodado todo código importado from operacoes import somar, subtrair, multiplicar, nome_empresa
#
# print(multiplicar(1, 3))
# print(somar(1, 3))
# print(subtrair(1, 3))
# print(nome_empresa)
print(__name__)
