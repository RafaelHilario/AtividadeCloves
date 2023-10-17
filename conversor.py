
taxas_fixas = {
    'USD': 1.18,   # Dólar Americano
    'GBP': 0.87,   # Libra Esterlina
    'JPY': 133.15, # Iene Japonês
    'EUR': 1.0,    # Euro (taxa base)
}

def converter_moeda(valor, moeda_origem, moeda_destino, taxas):
    if moeda_origem == moeda_destino:
        return valor
    
    if moeda_origem not in taxas or moeda_destino not in taxas:
        return "Moeda não suportada."
    
    valor_em_euro = valor / taxas[moeda_origem]
    valor_convertido = valor_em_euro * taxas[moeda_destino]
    return valor_convertido

def main():
    print("Bem-vindo ao Conversor de Moedas!")
    moeda_origem = input("Digite a moeda de origem (por exemplo, USD, EUR, GBP, JPY): ").upper()
    moeda_destino = input("Digite a moeda de destino (por exemplo, USD, EUR, GBP, JPY): ").upper()
    valor = float(input("Digite o valor que deseja converter: "))

    resultado = converter_moeda(valor, moeda_origem, moeda_destino, taxas_fixas)
    print("{:.2f} {} é equivalente a {:.2f} {}.".format(valor, moeda_origem, resultado, moeda_destino))

if __name__ == "__main__":
    main()
