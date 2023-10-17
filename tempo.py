import requests
from bs4 import BeautifulSoup

def obter_previsao_tempo(cidade):
    url = f"https://www.weather-forecast.com/locations/{cidade}/forecasts/latest"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        soup = BeautifulSoup(resposta.content, "html.parser")
        previsao = soup.find("span", class_="phrase").text
        return previsao.strip()
    else:
        return "Não foi possível obter a previsão do tempo para esta cidade."

def main():
    cidade = input("Digite o nome da cidade para consultar a previsão do tempo: ")
    previsao = obter_previsao_tempo(cidade)
    print(f"Previsão do Tempo para {cidade}: {previsao}")

if __name__ == "__main__":
    main()
