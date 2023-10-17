def calcular_imc(peso, altura):
    try:
        altura_metros = altura / 100 
        imc = peso / (altura_metros ** 2)
        return imc
    except ZeroDivisionError:
        return "Erro: Altura não pode ser zero."

def interpretar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade grau 1"
    elif 35 <= imc < 39.9:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"


def main():
    print("Calculadora de Índice de Massa Corporal (IMC)")
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em centímetros: "))
    
    imc = calcular_imc(peso, altura)
    status_imc = interpretar_imc(imc)
    
    print(f"Seu IMC é: {imc:.2f}")
    print(f"Status IMC: {status_imc}")

if __name__ == "__main__":
    main()
