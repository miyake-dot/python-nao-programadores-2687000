ano_nascimento = 1989
ano_formatura = 2010

# Considerando que as variáveis acima correspondem a 'Gerlaine', descubra a idade dela no ano da sua formatura
print(ano_formatura-ano_nascimento)

# Escreva expressões comparativas usando os operadores relacionais >, <= e ==. Imprima na tela as respostas
print(ano_formatura>ano_nascimento)
print(ano_formatura==ano_nascimento)
print(ano_formatura<=ano_nascimento)

# Crie expressões comparativas mais complexas utilizando operadores lógicos and, or e not. Imprima na tela as respostas
print(ano_formatura>ano_nascimento) or (ano_formatura==ano_nascimento)
print(ano_nascimento==2000)and(ano_formatura<=2100)
print(not(ano_formatura<ano_nascimento))