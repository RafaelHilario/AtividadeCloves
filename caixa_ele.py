class CaixaEletronico:
    def __init__(self):
        self.saldo = 0

    def ver_saldo(self):
        return self.saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        else:
            return False

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False

# Função principal
def main():
    caixa = CaixaEletronico()

    while True:
        print("\nMenu:")
        print("1. Ver Saldo")
        print("2. Sacar")
        print("3. Depositar")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("Saldo disponível: R$ {}".format(caixa.ver_saldo()))
        elif opcao == "2":
            valor = float(input("Digite o valor que deseja sacar: R$ "))
            if caixa.sacar(valor):
                print("Saque de R$ {} realizado com sucesso.".format(valor))
            else:
                print("Saldo insuficiente ou valor inválido.")
        elif opcao == "3":
            valor = float(input("Digite o valor que deseja depositar: R$ "))
            if caixa.depositar(valor):
                print("Depósito de R$ {} realizado com sucesso.".format(valor))
            else:
                print("Valor inválido.")
        elif opcao == "4":
            print("Saindo do caixa eletrônico. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
