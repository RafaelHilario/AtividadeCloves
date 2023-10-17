
def calcular_nota(media):
    if media >= 90:
        return 'A'
    elif media >= 80:
        return 'B'
    elif media >= 70:
        return 'C'
    elif media >= 60:
        return 'D'
    else:
        return 'F'

num_notas = int(input("Quantas notas você quer inserir? "))

soma_notas = 0

for i in range(num_notas):
    nota = float(input("Digite a nota {}: ".format(i + 1)))
    soma_notas += nota

media = soma_notas / num_notas

nota_correspondente = calcular_nota(media)

print("Média: {:.2f}".format(media))
print("Nota correspondente: {}".format(nota_correspondente))
