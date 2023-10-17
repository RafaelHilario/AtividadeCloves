import requests

def obter_previsao_tempo(cidade, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric"
    resposta = requests.get(url)
    dados = resposta.json()

    if resposta.status_code == 200:
        clima = dados["weather"][0]["description"]
        temperatura = dados["main"]["temp"]
        umidade = dados["main"]["humidity"]
        vento = dados["wind"]["speed"]
        return f"Condição: {clima}\nTemperatura: {temperatura}°C\nUmidade: {umidade}%\nVelocidade do Vento: {vento} m/s"
    else:
        return "Cidade não encontrada ou erro na obtenção dos dados."

def main():
    cidade = input("Digite o nome da cidade para consultar a previsão do tempo: ")
    api_key = "SUA_CHAVE_DE_API_DO_OPENWEATHERMAP"  # Substitua pelo seu próprio OpenWeatherMap API Key
    previsao = obter_previsao_tempo(cidade, api_key)
    print(previsao)

if __name__ == "__main__":
    main()
