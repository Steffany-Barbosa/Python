# se o número for multiplo de 3 print FIZZ ... Múltiplo de 3: 6%3 == 0
# se o número for multiplo de 5 print BUZZ ... 
# se o número for multiplo de 5 e de 3 print FIZZBUZZ ... 
# se o número não for multiplo de 3 nem de 5 imprime o próprio número.

# divisores = [3,5]
# palavras = ["FIZZ", "BUZZ"]
# saida = " "
# numero = int(input("Entre com um número: ")) #vai chamar o input e ele só vai aceitar nº inteiro
# for i in range (len(divisores)):  # Verifica se o número é divisível pelo divisor atual  o len verifica o tamanho da linha, o range vai criar uma lista de 0, 1 para antes do 3.
#     if (numero % divisores[i]) == 0:  # Se for divisível, adiciona a palavra correspondente à saída
#         saida += palavras [i]  # saida = saida + paravra [i] que está na posição i
# print (saida)

# if saida == "":
#     print = (numero)
# else:
#     print(saida)

#Prof

numero = int(input("Entre com um número: "))

if numero % 15  == 0:
    print ("FIZZBUZZ")
elif numero % 5 == 0:
    print ("BUZZ")
elif numero % 3 == 0:
    print ("FIZZ")
else:
    print (numero) 
