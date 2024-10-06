# Q8. Elabore um algoritmo que solicita duas informações do usuário.
#  A primeira, pergunta se possui bolsa família (S ou N), e a segunda
#  , se possui mais de três filhos (S ou N). Se for contemplado pelo
#   bolsa família e possuir mais de três filhos, deverá retornar
#   Verdadeiro, significando que pode acessar à vaga de cotista.



bolsafamilia = input('possui bolsa família?\ns - sim\nn - não\n')
quantidadefilhos = input('possui mais de 3 filhos?\ns - sim\nn - não\n')

if(bolsafamilia == 's' and quantidadefilhos == 's'):
    print('você pode acessar à vaga de cotista')
else:
    print('você não pode acessar à vaga de cotista')