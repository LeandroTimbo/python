palavras = ('aprender', 'progamar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'progamador', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos',end=' ')
    for letra in p:
        if letra in 'AaEeIiOoUu':
            print(f'{letra}', end=' ')
