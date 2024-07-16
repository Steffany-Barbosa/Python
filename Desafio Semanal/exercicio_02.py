# Crie um programa que permita ao usuário inserir o preço de várias frutas e, em seguida, calcule o preço total.

# Dicas que podem ser seguidas ou não: 
# - Crie um loop para solicitar ao usuário o preço de cada fruta.
# - Mantenha uma variável para armazenar o preço total.
# - Adicione o preço de cada fruta ao preço total.
# - Após inserir todos os preços, imprima o preço total.



def calcular_preco_final ():
  preco_total = 0.0

  continuar = True #Quando o usuario digitar Fim, ele para.

  while continuar:
    name_fruit = input ("Digite o nome da fruta (ou digite 'soma' para somar): ")
    if name_fruit.lower() == 'soma' :
      continuar = False #fazendo a troca
    else:
        try:
          preco = float(input(f"Digite o preço da fruta: {name_fruit} R$ "))
          preco_total += preco
        except ValueError:
          print(f"Por favor, digite um preço válido para a fruta {name_fruit}.")
          
  print(f"Calculo final das frutas é de: R$ {preco_total} ")
          
calcular_preco_final()

        



#lower () = formatação padrão das palavras no caso fim, será igual para todas as escritas.
#.format = vai puxar o nome das frutas p/ o preço
#try = envolve o código que tenta converter a entrada do usuário em um número de ponto flutuante e adicionar esse número ao preço total.
#except = e a conversão falhar e uma exceção ValueError for levantada (por exemplo, se o usuário digitar uma entrada que não pode ser convertida em um número de ponto flutuante, como uma letra), o Python irá executar o bloco except. Neste caso, o programa imprime uma mensagem de erro, instruindo o usuário a digitar um preço válido.


  