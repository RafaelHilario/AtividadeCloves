import json

# Função para mostrar os filmes disponíveis
def mostrar_filmes():
    print("Filmes em exibição:")
    for i, filme in enumerate(filmes):
        print(f"{i + 1}. {filme['titulo']} - {filme['horarios']}")

# Função para realizar a reserva
def fazer_reserva():
    mostrar_filmes()
    escolha_filme = int(input("Escolha o número do filme: ")) - 1
    
    if 0 <= escolha_filme < len(filmes):
        filme_escolhido = filmes[escolha_filme]
        print(f"Você escolheu: {filme_escolhido['titulo']}")
        
        horario_escolhido = input("Escolha o horário: ")
        if horario_escolhido in filme_escolhido['horarios']:
            nome_cliente = input("Digite seu nome: ")
            reserva = {
                "filme": filme_escolhido['titulo'],
                "horario": horario_escolhido,
                "cliente": nome_cliente
            }
            with open("reservas.txt", "a") as file:
                file.write(json.dumps(reserva) + "\n")
            print("Reserva feita com sucesso!")
        else:
            print("Horário inválido.")
    else:
        print("Filme inválido.")

# Função principal
def main():
    while True:
        print("\n=== Sistema de Reservas de Cinema ===")
        print("1. Mostrar Filmes")
        print("2. Fazer Reserva")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            mostrar_filmes()
        elif escolha == "2":
            fazer_reserva()
        elif escolha == "3":
            print("Obrigado por usar o Sistema de Reservas de Cinema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Lista de filmes e horários
filmes = [
    {"titulo": "Filme A", "horarios": ["10:00", "14:30", "18:45"]},
    {"titulo": "Filme B", "horarios": ["11:15", "15:40", "20:00"]},
    {"titulo": "Filme C", "horarios": ["13:20", "17:50", "22:10"]}
]

if __name__ == "__main__":
    main()
