# Q9. Elabore um algoritmo para que só possa autorizar 
# a entrada na loja, àqueles que estão com a anuidade
#  de associação em dia ou pagar o valor de 25 reais na entrada.

anuidade = input('bem vindo, você está com a anuidade da associação em dia?\ns - sim\nn - não\n')
if(anuidade =='s'):
    print("bem vindo a loja")
else:
    entrada = input('por favor pague 25 reais para entrada\ns - sim\nn - não\n')
    if(entrada == "s"):
        print("bem vindo a loja")
    else:
        print('o senhor está convidado a se retirar')