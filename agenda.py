import csv


def adicionar_contato(nome, telefone):
    with open('agenda.csv', 'a', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerow([nome, telefone])
    print('Contato adicionado com sucesso!')


def listar_contatos():
    with open('agenda.csv', 'r') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        for linha in leitor_csv:
            print('Nome: {}, Telefone: {}'.format(linha[0], linha[1]))


def buscar_contato(nome):
    with open('agenda.csv', 'r') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        for linha in leitor_csv:
            if linha[0] == nome:
                print('Nome: {}, Telefone: {}'.format(linha[0], linha[1]))
                return
        print('Contato não encontrado.')


def remover_contato(nome):
    contatos = []
    removido = False
    with open('agenda.csv', 'r') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        for linha in leitor_csv:
            if linha[0] != nome:
                contatos.append(linha)
            else:
                removido = True
    
    if removido:
        with open('agenda.csv', 'w', newline='') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)
            for contato in contatos:
                escritor_csv.writerow(contato)
        print('Contato removido com sucesso!')
    else:
        print('Contato não encontrado.')

# Menu principal
while True:
    print('\nMenu:')
    print('1. Adicionar Contato')
    print('2. Listar Contatos')
    print('3. Buscar Contato')
    print('4. Remover Contato')
    print('5. Sair')
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        nome = input('Digite o nome do contato: ')
        telefone = input('Digite o telefone do contato: ')
        adicionar_contato(nome, telefone)
    elif opcao == '2':
        listar_contatos()
    elif opcao == '3':
        nome = input('Digite o nome do contato que deseja buscar: ')
        buscar_contato(nome)
    elif opcao == '4':
        nome = input('Digite o nome do contato que deseja remover: ')
        remover_contato(nome)
    elif opcao == '5':
        print('Saindo...')
        break
    else:
        print('Opção inválida. Por favor, tente novamente.')
