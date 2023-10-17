import random

palavras = ['abacaxi', 'programar', 'java', 'mesa', 'computador', 'tecnologia']

def escolher_palavra(lista_palavras):
    return random.choice(lista_palavras)

def jogar_forca(palavra):
    palavra_escondida = ['_'] * len(palavra)
    tentativas = 6
    letras_usadas = []

    while '_' in palavra_escondida and tentativas > 0:
        letra = input('\nDigite uma letra: ').lower()

        if letra in letras_usadas:
            print('Você já tentou essa letra.')
        else:
            letras_usadas.append(letra)
            if letra in palavra:
                print('Letra correta!')
                for i in range(len(palavra)):
                    if palavra[i] == letra:
                        palavra_escondida[i] = letra
            else:
                print('Letra incorreta. Você tem {} tentativas restantes.'.format(tentativas - 1))
                tentativas -= 1
        
        print('Palavra: ' + ' '.join(palavra_escondida))
        print('Letras usadas: ' + ', '.join(letras_usadas))

    if '_' not in palavra_escondida:
        print('\nParabéns! Você ganhou! A palavra é: ' + palavra)
    else:
        print('\nGame over! Você perdeu. A palavra era: ' + palavra)

if __name__ == "__main__":
    palavra_selecionada = escolher_palavra(palavras)
    print('Bem-vindo ao Jogo da Forca!')
    print('Adivinhe a palavra: ')
    jogar_forca(palavra_selecionada)
