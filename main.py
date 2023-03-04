import requests

chave_api = "sua_chave_api"
cidade = input("Escolha sua cidade: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&units=metric"
resposta = requests.get(url)
dados = resposta.json()
temperatura = dados['main']['temp']
descricao_tempo = dados['weather'][0]['description']
umidade = dados['main']['humidity']

print(f"Cidade........{cidade}\n"
      f"Temperatura...{temperatura}\n"
      f"Tempo.........{descricao_tempo}\n"
      f"Umidade.......{umidade}")
