# Q7. Elabore um algoritmo para representar um sistema de 
# compra de produtos agrícolas de uma feira, mas que só 
# permite realizar a compra, se a pessoa tiver dinheiro 
# para pagar à vista e se estiver com a anuidade de 
# associação de produtor rural em dia. 

produtos = ['abobora', 'melancia', 'banana' , "manga"]

print('digite o produto que deseja, temos:')

for x in produtos:
    print(x)

produto = input()

formadepagamento = int(input('digite a forma de pagamento\n1 - avista\n2 - parcelado\n'))
situacaoanuidade = input('sua situação com a anuidade de associação de produtor rural está em dia?\ns - sim\nn - não\n')

if(formadepagamento == 1 and situacaoanuidade == "s"):
    print('compra finalizada tenha um bom dia')
else:
    print('infelizmente sua compra não pode ser efetuada')