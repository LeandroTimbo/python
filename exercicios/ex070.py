total = totmil = menor = cont = 0
barato = ' '
mb = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continua? [S/N] ')).upper().strip() [0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGAMA'))
print(f'O total de compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
