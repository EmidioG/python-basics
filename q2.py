# Q2. Faça um algoritmo que lê dois números, e verifica se o
#  primeiro número é maior ou igual ao segundo número. Se 
#  for, escrever "O número {valor do número 1} é maior ou 
#  igual ao número {valor do número 2}". Se não, escrever 
#  "O número {valor do número 1} é menor ou igual ao número
#   {valor do número 2}".

n1 = int(input('digite o primeiro número\n'))
n2 = int(input('digite o segundo número\n'))
if(n1>=n2):
    print(f'o número {n1} é maior ou igual ao número {n2}')
else:
    print(f'o número {n1} é menor ao número {n2}')
