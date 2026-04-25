# verificacao simples de temperatura
class Temperatura:
    def __init__(self, cidade, graus):
        self.cidade = cidade
        self.graus = graus

    def verificar_clima(self):
        clima = "quente" if self.graus >= 30 else "agradavel"  # uso de ternario
        return clima

    def exibir_dados(self):
        print(f"cidade: {self.cidade}")
        print(f"temperatura: {self.graus}°C")
        print(f"clima: {self.verificar_clima()}")


cidade = input("digite o nome da cidade: ")
graus = float(input("digite a temperatura atual: "))

# instancia
temperatura = Temperatura(cidade, graus)
temperatura.exibir_dados()
