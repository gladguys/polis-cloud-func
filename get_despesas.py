import requests
import json
import google.cloud

from firebase_admin import credentials, firestore

def getDespesas(db,id):
    receive = requests.get(f'https://dadosabertos.camara.leg.br/api/v2/deputados/{id}/despesas?ordem=ASC&ordenarPor=ano')
    despesas = receive.json()['dados']
    for d in despesas:
        if d['dataDocumento'] == '2020-02-13':
            d['politico_id'] = id
            db.collection('despesas').add(d)
    
    # save despesas in loop


def hello_world(request):
    # Add a new document
    db = firestore.Client()
    politicos = db.collection('politicos').stream()
    
    for p in politicos:
        getDespesas(db,p.to_dict()['id'])
     
    return 'end ok'
    

