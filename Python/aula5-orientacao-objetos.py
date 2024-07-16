from operacoes import OperacoesMatematicas

instanciada_operacoes = OperacoesMatematicas()

primeiro_numero = int (input("Diga-me o primeiro numero: "))
segundo_numero  = int (input("Diga-me o segundo numero: "))

resultado_da_soma = instanciada_operacoes.soma (primeiro_numero, segundo_numero)
print (f"O resultado da soma é: {resultado_da_soma}")

resultado_da_subtracao = instanciada_operacoes.subtracao (primeiro_numero, segundo_numero)
print (f"O resultado da subtracao é: {resultado_da_subtracao}")

resultado_da_divisao = instanciada_operacoes.divisao (primeiro_numero, segundo_numero)
print (f"O resultado da divisao é: {resultado_da_divisao}")

resultado_da_multiplicacao = instanciada_operacoes.multiplicacao (primeiro_numero, segundo_numero)
print (f"O resultado da multiplicacao é: {resultado_da_multiplicacao}")
