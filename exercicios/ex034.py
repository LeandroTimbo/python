salário = float(input('Qual o salário do funcionário? R$ '))
if salário <= 1250 :
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salário, novo))