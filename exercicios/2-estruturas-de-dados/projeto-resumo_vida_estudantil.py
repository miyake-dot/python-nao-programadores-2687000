# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
estudante = {}
estudante['nome'] = input('Qual o seu nome?')
estudante['LinkedIn'] = int(input('Em que ano conheceu o LinkedIn?'))
estudante['ano_atual'] = int(input('Em que ano estamos?'))
cursos = input('Quais foram os cursos realizados no LinkedIn Learning? (separe por vírculas) ')

estudante['cursos'] = cursos.split (', ')

# 2. Armazene esses dados em um dicionário


# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.
total_anos = estudante['ano_atual']-estudante['LinkedIn']
total_cursos = len(estudante['cursos'])
print(f"Oi, {estudante['nome']}, desde {estudante['LinkedIn']} você conhece o LinkedIn. Nesses {total_anos} anos, você realizou {total_cursos} cursos sendo o primeiro curso {estudante['cursos'][0]} e o último curso {estudante['cursos'][-1]}")