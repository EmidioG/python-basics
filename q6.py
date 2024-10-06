# Q6. Elabore um algoritmo para representar um sistema 
# de compra de produtos agrícolas de uma feira, mas 
# que só permite compras à vista.

produtos = ['abobora', 'melancia', 'banana' , "manga"]

print('digite o produto que deseja, temos:')

for x in produtos:
    print(x)

produto = input()

formadepagamento = int(input('digite a forma de pagamento\n1 - avista\n2 - parcelado\n'))

if(formadepagamento == 1):
    print('compra finalizada tenha um bom dia')
else:
    print('infelizmente não aceitamos essa forma de pagamento')