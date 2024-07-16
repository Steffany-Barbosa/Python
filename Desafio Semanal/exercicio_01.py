# Escreva um programa que remova todas as duplicatas de uma lista e imprima a lista resultante.

# Dicas que podem ser seguidas ou não: 
# Remover duplicatas de uma lista:
# - Você pode utilizar conjuntos (sets) para remover duplicatas, já que conjuntos não permitem elementos duplicados.
# - Caso queira, converta a lista para um conjunto. Em seguida, converta o conjunto de volta para uma lista.
# - Imprima a lista resultante.

# lista = [1, 2, 3, 4, 3, 2, 1]
# lista_sem_duplicatas = list(dict.fromkeys(lista))
# print(lista_sem_duplicatas)

lista = ["banana", "maça", "manga", "manga", "banana"]
not_duplicates = list (dict.fromkeys(lista))
print(not_duplicates)
