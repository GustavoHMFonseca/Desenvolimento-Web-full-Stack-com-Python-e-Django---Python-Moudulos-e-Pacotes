"""
Um módulo é im arquivo contendo definições
e instruções Python que podem ser importados para
utilização de seus recursos
Permitem expandir as funcionalidades
da linguagem além dos recursos padrões
1) É possível utilizar módulos padrões do Python
2) É possível instalar módulos
https://docs.python.org/pt-br/3/py-modindex.html
"""

# import random
from random import randint  # ctrl + space mostra todos itens dentro do import do random
# Caso clique com o botão direiro no random selecionat go to e implementação
# voce cnseguirá ver a implementação do modulo random
# print(random.randint(1, 10))
print(randint(1, 10))

# from functools import reduce
# from datetime import datetime as date  #date é um apelido
# print(date.now())

# from math import sqrt
# print(sqrt(64))

"""
PIP
pip é um sistema de gerenciamento de pacotes em python
pip3 install --upgrade pip
pip install nome-pacote
pip uninstall nome-pacote
"""
import pymysql


