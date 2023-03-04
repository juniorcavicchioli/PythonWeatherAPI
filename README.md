# PythonWeatherAPI
## Descrição do Projeto
Este é um simples projeto em Python que utiliza a API do OpenWeatherMap para exibir informações sobre o clima em uma cidade escolhida pelo usuário.

## Como funciona
O usuário é solicitado a inserir o nome de uma cidade e, em seguida, o programa faz uma solicitação para a API OpenWeatherMap para obter informações sobre a cidade, incluindo temperatura, descrição do tempo e umidade. O programa exibe essas informações na saída padrão.

## Configuração
Para usar a API OpenWeatherMap, você precisa de uma chave de API válida. Você pode obter uma chave de API gratuitamente se inscrevendo no site do [OpenWeatherMap](https://home.openweathermap.org). Uma vez que você tenha uma chave de API, insira-a no arquivo config.py, que deve ser criado no diretório raiz do projeto e conter uma linha que define a chave como uma variável chamada chave_api.

## Dependências
Este programa requer o módulo requests para fazer solicitações HTTP à API OpenWeatherMap. Se você não tiver o módulo requests instalado, poderá instalá-lo usando o comando
`
pip install requests
`
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