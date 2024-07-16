#ctrl + ; comenta uma parte do código
  

 


# print ("Diga-me, sim(s) ou não (n)?")
# resposta = input() #python espera entrada do usuário

# if resposta == "sim" or resposta =="s":
#     print ("resposta positiva")
# elif resposta == "não" or resposta =="n":
#     print ("resposta negativa")
# else:
#     print ("resposta desconhecida")

print ("Diga-me, sim(s) ou não (n)?")
resposta = int(input()) #vai chamar o input e ele só vai aceitar nº inteiro

if resposta == 1:
    print ("resposta positiva")
elif resposta == 2:
    print ("resposta negativa")
else:
    print ("resposta desconhecida")