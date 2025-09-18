casa = float(input('Valor do imóvel: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
minimo = salário * 30 /100
print('Para pagar uma casa no valor de R${:.2f} em {}anos'.format(casa, anos))
print('A prestação será no valor de R${:.2f}'.format(prestação))
if prestação <= minimo:
    print('O EMPRESTIMO PODE SER CONCEDIDO!')
else:
    print('EMPRESTIMO NEGADO!!!')
