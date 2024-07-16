

# divisoes = (3, 5, 15)

# for elemento in divisoes: #nome da variavel
#     if elemento ==  5: # numero
#         continue
#     print (elemento)

# 3 é igual a 5? não então ele vai imprimir o 3

# divisoes = (3,5,15)
# for elemento in divisoes:
#     print(elemento)

#loop percorre os valores na tupla divisoes e imprime cada um deles separadamente.




#Outra possibilidade de fazer loop

# contador = 0
# while contador < 10 :
#     print(contador)
#     contador += 1

#Bateria de exercicios
#Exercicio 1 calculadora simples

operador = input("Entre com uma operação: (+ - * /): ")
num1 = float(input("Digite o 1º numero: "))
num2 = float(input("Digite o 2º numero: "))

if operador == "+":
    resultado = num1 + num2
    
elif operador == "-":
    resultado = num1 - num2
    
elif operador == "*":
    resultado = num1 * num2
   
elif operador == "/":
    if num2 != 0:  
        resultado = num1 / num2
    else:
        print("ERROR")
        resultado = None
else:
    print(f"{operador}operador inválido")

if resultado is not None: 
    print ("O resultado da operação é: ", resultado)
    
