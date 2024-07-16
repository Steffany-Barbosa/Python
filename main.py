class PassagemAerea:
    def __init__(self, origem, destino, preco):
        # Inicializa os atributos da passagem aérea
        self.origem = origem
        self.destino = destino
        self.preco = preco

class PassagensAereasManager:
    def __init__(self):
        # Inicializa a lista de passagens aéreas
        self.passagens = []

    def adicionar_passagem(self, passagem):
        # Adiciona uma nova passagem à lista
        self.passagens.append(passagem)

    def listar_passagens(self):
        # Verifica se há passagens na lista e as exibe, caso contrário, exibe uma mensagem informando que nenhuma passagem foi comprada ainda
        if not self.passagens:
            print("Nenhuma passagem foi comprada ainda.")
        else:
            print("Passagens compradas:")
            # Itera sobre a lista de passagens e exibe as informações de cada uma
            for idx, passagem in enumerate(self.passagens, start=1):
                print(f"{idx}. Origem: {passagem.origem}, Destino: {passagem.destino}, Preço: {passagem.preco}")

def comprar_passagem(manager):
    # Solicita ao usuário as informações da passagem (origem, destino e preço)
    origem = input("Origem: ")
    destino = input("Destino: ")
    preco = float(input("Preço: "))
    # Cria um objeto PassagemAerea com as informações fornecidas pelo usuário
    passagem = PassagemAerea(origem, destino, preco)
    # Adiciona a passagem à lista de passagens gerenciada pelo PassagensAereasManager
    manager.adicionar_passagem(passagem)
    print("Passagem comprada com sucesso!")

def menu():
    # Exibe o menu de opções para o usuário
    print("\n-------- AfroCodigosFy - Venda de Passagens no Precinho --------")
    print("1. Comprar Passagem")
    print("2. Listar Passagens Compradas")
    print("3. Sair")

if __name__ == "__main__":
    # Cria uma instância de PassagensAereasManager
    manager = PassagensAereasManager()
    # Loop principal do programa
    while True:
        # Exibe o menu
        menu()
        # Solicita ao usuário que escolha uma opção do menu
        opcao = input("Escolha uma opção: ")
        # Verifica a opção escolhida pelo usuário e executa a ação correspondente
        if opcao == "1":
            comprar_passagem(manager)
        elif opcao == "2":
            manager.listar_passagens()
        elif opcao == "3":
            # Encerra o programa se o usuário escolher a opção de sair
            print("Obrigado por utilizar o AfroCodigosFy. Volte sempre!")
            break
        else:
            # Exibe uma mensagem de erro se o usuário escolher uma opção inválida
            print("Opção inválida. Por favor, escolha uma opção válida.")
