# Crie uma lista apenas com elementos numéricos
Lista = [0,1,2,3,4]

# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
Aleatório = ['Ana',2,[1,2,3,4],True]

# Imprima na tela apenas os 5 primeiros elementos da lista
print(Lista[0:5])

# Crie um slice na lista para que imprima na tela os elementos de índice par
elementos_indice_par = Lista[0:-1:2]
print(elementos_indice_par)

# Remova da lista o último item
Lista.pop()
print(Lista)

# Insira na lista um novo item
Lista.append(5)
print(Lista)

# Remova da lista um item específico
Lista.remove(2)
print(Lista)