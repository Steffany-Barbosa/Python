# Crie um programa que ordene uma lista de frutas em ordem alfabética.

# Dicas que podem ser seguidas ou não: 
# - Use o método sort() para ordenar a lista em ordem alfabética.
# - Certifique-se de usar o argumento key=str.lower para que a ordenação seja case-insensitive.

# Primeiro criar uma função
# lista de frutas usando o metodo .sort(key=str.lower)
# retornar o valor da lista de frutas
#depois chamamos uma variavel frutas sla, com uma lista aleatória de frutas
#após isso é feito a "troca" O resultado da função ordenar_frutas, que é a lista de frutas ordenadas, é então atribuído à variável frutas_ordenadas.
#depois usamos o print de "ordem alfabetica das frutas", com a função de fruits_order

def order_fruits (fruit_list):
  fruit_list.sort(key=str.lower)
  return fruit_list

fruits = ["Manga", "Mamão", "Caqui", "Abacaxi", "Abacate", "Jabuticaba", "Limão", "Laranja", "Graviola"]
fruits_order = order_fruits(fruits)
print(f"Ordem alfabética das frutas: {fruits_order}")






# def ordenar_frutas(lista_frutas):
#     lista_frutas.sort(key=str.lower)
#     return lista_frutas

# frutas = ["Banana", "maçã", "Abacaxi", "laranja", "uva", "Pêssego"]
# frutas_ordenadas = ordenar_frutas(frutas)

# print("Frutas ordenadas:", frutas_ordenadas)