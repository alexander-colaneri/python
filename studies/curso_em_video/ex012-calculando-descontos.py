print()
print('*'*5, 'Cálculo de Desconto', '*'*5)
print()
preço = float(input('Digite o valor do produto ou serviço: R$'))
desc = float(input('Digite a porcentagem de desconto a ser dada: '))
porcent = ((preço * desc)/100)
preçofinal = preço - porcent
print()
print(f'Valor do desconto de {desc}%: R${porcent:.2f}')
print(f'Preço final com {desc}% de desconto: R${preçofinal:.2f}')