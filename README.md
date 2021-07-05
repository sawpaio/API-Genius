API-GENIUS-LUCAS-SAMPAIO
=================================

API que consome do site Genius utilizando API própria fornecida pelo site: https://docs.genius.com/#/getting-started-h1

Resposta: 10 músicas mais ouvidas do artista buscados pelo Id do artista, armazenamento do nome do artista com dados de id de transações únicos no dynamodb.

Instalação dos pacotes
--------------------
Instale os pacotes necessários com o comando:
``
$ pip install -r requirements.txt
``

Preparação
--------------------
É necessário que o usuário e desenvolvedor use um Access Token, que pode ser gerado em: https://genius.com/api-clients/new

Substitua pelo seu Access Token no campo CLIENT_ACCESS_TOKEN no arquivo app.py

Execução
--------------------
Execute a aplicação com:

``
python3 app.py
``

Teste
--------------------
Pode-se utilizar o postman para testar a aplicação, envie dois argumentos no método GET: id (do artista) e cache (True ou False) para a relação do DynamoDB e Redis.

Retorno
--------------------
O response da aplicação são as 10 músicas mais ouvidas do artista pesquisado.


