# API de Informações de Pacotes

Esta API fornece informações sobre pacotes de software, incluindo nome, data de publicação, versão Python mais recente e downloads no último mês. Ela recupera as informações de um arquivo CSV e expõe vários endpoints para consulta e filtragem dos dados.

## Instruções de Execução

1. Instale as dependências necessárias executando o seguinte comando:
pip install flask

2. Execute o seguinte comando para iniciar o servidor:
python app.py


4. A API estará disponível em `http://localhost:5000/`.

## Endpoints

- `GET /pacotes`: Retorna informações de todos os pacotes.
- `GET /pacotes/nome`: Retorna os pacotes ordenados por nome.
- `GET /pacotes/data_publicacao`: Retorna os pacotes ordenados por data de publicação.
- `GET /pacotes/versao_python`: Retorna os pacotes ordenados por versão Python mais recente.
- `GET /pacotes/downloads_ultimo_mes`: Retorna os pacotes ordenados por downloads no último mês.
- `GET /pacotes/nome/<nome>`: Retorna os pacotes com o nome especificado.
- `GET /pacotes/versao_python/<versao_python>`: Retorna os pacotes com a versão Python especificada.

Substitua `<nome>` e `<versao_python>` pelos valores desejados ao fazer as requisições nos dois últimos endpoints.

