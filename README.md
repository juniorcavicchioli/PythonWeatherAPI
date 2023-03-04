# PythonWeatherAPI
## Descrição do Projeto
Este é um simples projeto em Python que utiliza a API do OpenWeatherMap para exibir informações sobre o clima em uma cidade escolhida pelo usuário.

## Funcionalidades
O usuário informa o nome da cidade que deseja consultar e a chave da API do OpenWeatherMap. O código faz uma requisição HTTP para a API com os parâmetros informados, e a resposta é armazenada em formato JSON. A partir desses dados, são extraídas informações como a temperatura, descrição do tempo e umidade, que são exibidas na saída.

## Como utilizar
1. Você precisará de uma chave de API válida do OpenWeatherMap. Você pode obter uma chave gratuita no site do OpenWeatherMap.
2. Faça o clone do projeto em seu computador.
3. Na linha 3 do arquivo, substitua sua_chave_api pela chave de API que você obteve no [OpenWeatherMap](https://home.openweathermap.org).
4. Execute o programa digitando `python nome_do_arquivo.py` no terminal, onde `nome_do_arquivo.py` é o nome do arquivo que contém o código, no caso, o `main.py`.
5. Digite o nome da cidade que deseja consultar as informações climáticas e pressione Enter.

### Exemplo de entrada
```
Pindamonhangaba
```
### Exemplo de saída
```python
Cidade........Pindamonhangaba
Temperatura...29.14
Tempo.........few clouds
Umidade.......58
```