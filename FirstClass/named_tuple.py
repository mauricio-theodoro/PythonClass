"""
@Modulo Collection - Named Tuple

# Recapitulando tuplas
tupla = (1, 2, 3)
print(tupla[1])

Named Tuple -> São tupla, diferenciadas onde, especificamos um nome para a mesma e também parâmetros
"""
#Importantando
from collections import namedtuple

# Precisamos definir o nome e parâmetros.

#Forma 1

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 = Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')

#Forma 3 - Declaração Named Tuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando

ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray',)

# Acessando os dados
#Forma 1
print(ray)
print(ray[0]) # Idade
print(ray[1]) # Raça
print(ray[2]) # Nome

#Forma 2

print(ray.idade) # Idade
print(ray.raca) # Raça
print(ray.nome) # Nome

print(ray.index('Chow-Chow'))
print(ray.count('Chow-Chow'))



