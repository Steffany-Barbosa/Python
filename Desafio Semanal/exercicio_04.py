# Crie um programa que conte quantas vezes cada tipo de fruta aparece em uma lista.

# Dicas que podem ser seguidas ou não: 
# - Utilize um dicionário para armazenar o número de ocorrências de cada fruta.
# - Passe pela lista e incremente o valor do dicionário para cada fruta encontrada.
# - No final, imprima o dicionário.

#lista
#dicionario
#função para que não aja tanta repetição da mesma coisa

def contagem_frutas(lista_frutas):
  # Inicializa um dicionário vazio para armazenar a contagem de frutas
  armazenamento_frutas = {}
  
   # Itera sobre cada fruta na lista
  for frutas in lista_frutas:
    
    # Se a fruta já existe, incrementa o contador
    if frutas in armazenamento_frutas:
      armazenamento_frutas[frutas] += 1
      
      # Se a fruta ainda não existe, adiciona ao dicionário com contador igual a 1
    else:   
      armazenamento_frutas[frutas] = 1
      
       # Retorna o dicionário de contagem de frutas
  return armazenamento_frutas
      
lista_frutas = ["banana", "tomate", "maçã", "pera", "banana", "manga", "maçã", "manga", "pera"]   


resultado = contagem_frutas(lista_frutas)
 
    #dicionário
for fruta, quantidade in resultado.items():
  print(f"{fruta}: {quantidade}")
  
  
#usando o método .items(), que retorna uma sequência de tuplas (chave, valor) representando cada par chave-valor no dicionário.
#no dicionario estamos usando a atribuição multipla.
#print: vai aparece fruta tal: e a quantidade que tem dela.
