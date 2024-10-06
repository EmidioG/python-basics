# Q5. Faça um algoritmo que irá fazer o cadastro de usuário.
#  Para isso, solicita o nome do usuário, e a senha. Depois,
#   pede que o usuário confirme novamente a senha. O sistema
#    deverá verificar se as senhas digitadas são iguais. Se 
#    forem iguais, informar que o cadastro está correto. Se 
#    não forem iguais, informar que o cadastro não foi 
#    realizado porque as senhas não conferem.

nome = input('digite o nome do usuário\n')
senha = input('digite a senha\n')
confirmasenha= input('digite a senha novamente\n')
if(senha == confirmasenha):
    print('cadastro está correto')
else:
    print('cadastro não realizado, senhas não conferem')