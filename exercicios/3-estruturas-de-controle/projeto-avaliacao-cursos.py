# Nesse desafio você verificará dentro de uma lista se o item estar contido nela, caso verdadeiro deverá imprimir na tela essa informação, além disso deverá solicitar avaliação para o item e armazená-la em um dicionário.
# 1. Crie uma lista com 5 diferentes cursos do LinkedIn Learning
lista = 'Python Para Não Programadores, Python: Noções básicas, Análise de CV, Estatística, Aprimoramento de soft skills'

# 2. Crie 3 variáveis do tipo string e associe 1 curso a cada uma delas
curso_1 = 'Python Para Não Programadores'
curso_2 = 'Python: Noções básicas'
curso_3 = 'Estatística'

# 3. Crie um dicionário vazio para armazenar a nota do curso
nota = {}

# 4. Crie uma estrutura condicional para verificar se cada variável está contida na lista

if curso_1 in lista:
  print(f'O curso "{curso_1}" está disponível no LinkedIn Learning. Por favor, avalie o curso.')
  nota[curso_1] = int(input('Qual nota você daria para o curso de 0 a 5?'))
if curso_2 in lista:
  print(f'O curso "{curso_2}" está disponível no LinkedIn Learning. Por favor, avalie o curso.')
  nota[curso_2] = int(input('Qual nota você daria para o curso de 0 a 5?'))
if curso_3 in lista:
  print(f'O curso "{curso_3}" está disponível no LinkedIn Learning. Por favor, avalie o curso.')
  nota[curso_3] = int(input('Qual nota você daria para o curso de 0 a 5?'))
else:
  print('Infelizmente o curso não está disponível no LinkedIn Learning.')

# 5. Se o curso estiver na lista, solicite uma nota para avaliação
# 6. Armazene essa nota no dicionário, sendo a chave o título do curso e o valor a nota
print(nota)