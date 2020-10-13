import requests
import yaml

with open(r'./credentials.yaml') as file:
        parameters = yaml.load(file, Loader=yaml.FullLoader)

def getLists(id):
    url = "https://api.trello.com/1/boards/{}/lists".format(id)

    query = {
        'key': parameters['trello_key'],
        'token': parameters['trello_token'],
    }

    response = requests.request(
    "GET",
    url,
    params=query
    )
  

def createCard(issue): 
    url = "https://api.trello.com/1/cards"

    description = """ Olá professor. Por favor, verifique o tópico criado pelo aluno {}\n Link: {}\n Texto: {} """.format(issue['user_name'], issue['url'], issue['message'])

    query = {
        'key': parameters['trello_key'],
        'token': parameters['trello_token'],
        'idList': parameters['trello_list'],
        'name': 'Atividade de fórum',
        'desc': description
    }

    response = requests.request(
        "POST",
        url,
        params=query
    )


def executeIssues(issues):
    [createCard(row) for _, row in issues.iterrows()]