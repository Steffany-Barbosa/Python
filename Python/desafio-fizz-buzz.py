# se o número for multiplo de 3 print FIZZ ... Múltiplo de 3: 6%3 == 0
# se o número for multiplo de 5 print BUZZ ... 
# se o número for multiplo de 5 e de 3 print FIZZBUZZ ... 
# se o número não for multiplo de 3 nem de 5 imprime o próprio número

# numero = int(input("Digite um número: "))

# for x in range (1,numero +1): #range gera uma lista de nº
#   if x %5 == 0 and x %3 == 0:
#     print ("FIZZBUZZ")
#   elif x %5 == 0:
#     print("BUZZ")
#   elif x %3 == 0:
#     print ("FIZZ")
#   else:
#     print(x)


# contador = 0
# while contador < 10 :
#     print(contador)
#     contador += 1

number = int(input("Digite um número: "))
cont = 0

while (cont <= number):
  if cont %5 == 0 and cont %3 == 0 and cont != 0:
     print(f"posição - {cont} - FIZZBUZZ")

  elif cont %5 == 0 and cont != 0:
     print(f"posição - {cont} - BUZZ")

  elif cont %3 == 0 and cont != 0:
     print(f"posição - {cont} - FIZZ")

  else:
     print(f"Não é multiplo de 3 e 5 - {cont}")
  cont += 1




# Este código implementa a lógica do popular jogo FizzBuzz. Aqui está como ele é lido:

# Primeiro, o programa solicita ao usuário que insira um número inteiro através da função input().
# Em seguida, ele itera de 1 até o número inserido pelo usuário usando um loop for com a função range().
# Durante cada iteração, o programa verifica se o número atual (x) é divisível por 3, por 5 ou por ambos.
# Se o número for divisível por ambos (3 e 5), o programa imprime "FIZZBUZZ".
# Se o número for divisível apenas por 5, ele imprime "BUZZ".
# Se o número for divisível apenas por 3, ele imprime "FIZZ".
# Se o número não for divisível nem por 3 nem por 5, ele simplesmente imprime o próprio número.
# Aqui está uma leitura do código:

# O usuário insere um número inteiro.
# O programa então itera de 1 até o número inserido.
# Durante cada iteração, ele verifica se o número é divisível por 3, 5 ou ambos.
# Dependendo das condições, o programa imprime "FIZZ", "BUZZ", "FIZZBUZZ" ou o próprio número.
# Essa é uma implementação clássica do problema FizzBuzz, comum em entrevistas de programação e frequentemente usado para ensinar conceitos básicos de programação.