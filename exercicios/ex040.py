nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno e {:.1f}'.format(nota1, nota2, média))
if média < 5:
    print('O aluno está REPROVADO.')
elif 7 > média >= 5:
    print('O aluno está em RECUPERAÇÃO.')
else:
    print('O aluno está APROVADO.')