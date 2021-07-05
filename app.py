### Lucas Sampaio de Melo
## 07/05/2021
# Confitec Test

from flask import Flask, request
import json
import requests
import boto3   
import uuid

dynamodb = boto3.resource('dynamodb')
dynamodbTable = dynamodb.Table('artist_transactions')
app = Flask('API - Genius')
id_transaction = str(uuid.uuid4())
URL = 'https://api.genius.com/artists/{}/songs?sort=popularity&per_page=10'
CLIENT_ACCESS_TOKEN = 'PREENCHA AQUI'
HEADER = {
    'Authorization': f'Bearer {CLIENT_ACCESS_TOKEN}',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/17.0',
    'Accept': 'application/json',
}

@app.route('/', methods=['GET'])
def get_top_ten_songs():
    '''
    Usa a API do Genius para listar as 10 músicas mais ouvidas do artista pelo seu ID.
    '''
    id_artist = request.args.get('id')
    cache = request.args.get('cache')
    #Verifica se o id fornecido no endpoint é inválido.
    if not id_artist:
        return 'id inválido.', 400

    id_artist = id_artist.strip()

    try:
        #Preenche a URL com o id do artista que foi verificado na API do Genius.
        url = URL.format(id_artist)    
        
        #Faz a requisição pela URL montada.
        answer = requests.get(url, headers=HEADER, timeout=5.0)
        if answer.status_code != 200:
            raise Exception

        #Retorna o JSON resposta com as 10 músicas mais populares como resposta da API.
        data = json.loads(answer.text)
        artist = data['response']['songs']
        artist = (artist[0]['primary_artist']['name'])
        if cache == 'False':
            try:
                dynamodbTable.put_item(
                {
                    'id_transaction': '{}'.format(id_transaction),
                    'artist': '{}'.format(artist)
                }
                )   
            except Exception as error:
                print('Ocorreu um erro ao adicionar ao Dynamodb.')
                pass
        else:
            'TODO: verifica se já existe disponível em Cache.'
        return data, 200

    
    except Exception as error:
        return f'Ocorreu um erro ao puxar os dados.{error}', 500

if __name__ == "__main__":
    app.run(host='localhost', port='8088')    