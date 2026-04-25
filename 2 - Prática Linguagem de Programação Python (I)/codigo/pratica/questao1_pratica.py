# cadastro de participantes do bootcamp LAMIA, questao mais trabalhada

class Participante:
    def __init__(self, nome, trilha, cards_concluidos):
        self.nome = nome
        self.trilha = trilha
        self.cards_concluidos = cards_concluidos

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Trilha: {self.trilha}")
        print(f"Cards concluídos: {self.cards_concluidos}")

    def verificar_progresso(self):
        # verifica o progresso de acordo com a quantidade de cards concluido
        if self.cards_concluidos >= 20:
            print("Progresso: Avançado")
        elif self.cards_concluidos >= 10:
            print("Progresso: Intermediário")
        else:
            print("Progresso: Inicio")


# lista para armazenar os participantes cadastrados
participantes = []

# quantidade de participantes que serao cadastrados
quantidade = int(input("Quantos participantes deseja cadastrar? "))

for i in range(quantidade):
    print(f"\nCadastro do participante {i + 1}")

    nome = input("Nome: ")

    # escolha da trilha usando repeticao para evitar opcao invalida
    while True:
        print("Escolha a trilha:")
        print("1 - Bootcamp Machine Learning")
        print("2 - Bootcamp FrontEnd")

        opcao_trilha = int(input("Digite a opçao da trilha: "))

        # coloquei duas opções
        if opcao_trilha == 1:
            trilha = "Bootcamp Machine Learning"
            break
        elif opcao_trilha == 2:
            trilha = "Bootcamp Frontend"
            break
        else:
            print("Opção invalida, Tente novamente.\n")

    cards_concluidos = int(input("Qtd de cards concluidos: "))

    # instancia2
    participante = Participante(nome, trilha, cards_concluidos)
    participantes.append(participante)

print("\nParticipantes cadastrados:")

# percorre a lista e exibe os dados de cada participante
for participante in participantes:
    participante.exibir_dados()
    participante.verificar_progresso()
    print('\n')  # da uma 1 linha entre cada participate
