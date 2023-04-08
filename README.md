# PythonWeatherAPI
<img src="https://shields-io-visitor-counter.herokuapp.com/badge?page=juniorcavicchioli.DesafioTarget&color=1D70B8&logo=GitHub&logoColor=FFFFFF&style=flat-square"/>

## Sumário
- [Descrição do Projeto](#descrição-do-projeto)
- [Como funciona](#como-funciona)
- [Configuração](#configuração)
- [Dependências](#dependências)
- [Autor](#autor)
## Descrição do Projeto
Este é um simples projeto em Python que utiliza a API do OpenWeatherMap para exibir informações sobre o clima em uma cidade escolhida pelo usuário.

## Como funciona
O usuário é solicitado a inserir o nome de uma cidade e, em seguida, o programa faz uma solicitação para a API OpenWeatherMap para obter informações sobre a cidade, incluindo temperatura, descrição do tempo e umidade. O programa exibe essas informações na saída padrão.
### Exemplo de entrada
```python
Pindamonhangaba
```
### Exemplo de saída
```console
Cidade........Pindamonhangaba
Temperatura...29.14
Tempo.........few clouds
Umidade.......58
```

## Configuração
Para usar a API OpenWeatherMap, você precisa de uma chave de API válida. Você pode obter uma chave de API gratuitamente se inscrevendo no site do [OpenWeatherMap](https://home.openweathermap.org). Uma vez que você tenha uma chave de API, insira-a no arquivo config.py, que deve ser criado no diretório raiz do projeto e conter uma linha que define a chave como uma variável chamada chave_api.

## Dependências
Este programa requer o módulo requests para fazer solicitações HTTP à API OpenWeatherMap. Se você não tiver o módulo requests instalado, poderá instalá-lo usando o comando
`
pip install requests
`

## Autor
Feito por [@juniorcavicchioli](https://github.com/juniorcavicchioli?tab=repositories). Entre em contato!

LinkedIn: [Adilson Roberto Cavicchioli Junior](https://www.linkedin.com/in/adilson-roberto-cavicchioli-junior-6816b7192?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BIpMh5bVEQOi82%2FRHJ6oxkg%3D%3D) <br>
Email: [cavicchioli.adilson@gmail.com](mailto:cavicchioli.adilson@gmail.com)

Sinta-se à vontade para me contatar caso tenha dificuldade em gerar uma chave para testar o programa, para perguntas, sugestões ou colaborações em projetos futuros!
