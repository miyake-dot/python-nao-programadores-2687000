# Declare 4 variáveis do tipo numérica
x = 30
y = 10
w = 5
z = 26


# Crie uma estrutura condicional para comparar dois números
if w > z:
    print(False)
else:
    print(True)


# Se a condição for verdadeira, imprima na tela uma mensagem informando que a condição foi cumprida e informando o número de maior valor
if x > w:
    print(f'Nesse caso, {x} é maior do que {w}')


# Se a condição não for cumprida, imprima na tela uma mensagem informando que a condição é negativa e informe o número de maior valor
if w > y:
    print(f'Condição cumprida, {w} é maior que {y}.')
else:
    print(f'Condição não cumprida, {y} é maior valor do que {w}.')

# Insira outras condições na estrutura condicional usando o elif
if x > y:
    print(f'Condição foi cumprida, {x} é maior do que {y}.')
elif y > w:
    print(f'Condição foi cumprida, {y} é maior do que {w}.')
else:
    print(f'Condição não foi satisfeita. O valor {w} é maior do que {y}.')

# Incremente a estrutura condicional já existente com expressões lógicas utilizando "and" ou "or"
if w > y or y < w:
    print(f'Condição cumprida, {w} é maior que {y}, ou {w} é maior do que {y}.')
if x > z and x > y:
    print(f'Condição foi cumprida, {x} é maior valor quando comparado com {y} e {z}.')

# Crie uma estrutura condicional onde mais de uma condição seja verdadeira, e use apenas a palavra reservada "if"
if x > w:
    print(f'Condição satisfeita, {x} maior do que {w}.')
if y > w:
    print(f'Condição satisfeita, {y} maior do que {w}.')
if w > z:
    print(f'Condição satisfeita, {w} maior do que {z}.')