from random import randint
v = 0
print('=-' * 20)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' * 20)
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper() [0]
    print(f'Voce jogou {jogador} e o computador {computador}. Total de {total} ', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce VENCEU!')
            v += 1
        else:
            print('Voce PERDEU!')
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('Voce VENCEU!')
            v += 1
        else:
            print('Voce PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')
