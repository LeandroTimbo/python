ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    apc = int(input('Mostar notas de qual aluno? (999 interrompe): '))
    if apc == 999:
        print('FINALIZANDO...')
        break
    if apc <= len(ficha) - 1:
        print(f'Notas de {ficha[apc] [0]} são {ficha[apc] [1]}')
print('<<< VOLTE SEMPRE >>>')
