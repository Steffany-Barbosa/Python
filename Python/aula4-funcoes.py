numero = int(input ('numero'))

def fizzbuzz(meu_numero): # def é igual o function no JS
    for num in range (1, meu_numero + 1): # meu_numero parâmetro da função
      if num % 15 == 0:
          print("FIZZBUZZ")
      elif num % 5 == 0:
          print("BUZZ")
      elif num % 3 == 0:
          print("FIZZ")
      else:
          print(num)

fizzbuzz(numero)

# somatorio
# somatorio(5) ==15
# somatorio(1) ==1
# somatorio(0) ==1
# 5+4+3+2+1 ==15




