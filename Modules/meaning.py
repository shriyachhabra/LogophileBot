
import requests
import json

def word_meaning(word):
    app_id = 'd520dc72'
    app_key = '9636a335f1d422e70aa5a9b2381f6517'

    language = 'en'
    word_id = word

    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()

    r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

    code=r.status_code
    r=r.json()
    results=r['results'][0]
    le=results['lexicalEntries'][0]
    entries=le['entries'][0]
    senses=entries['senses'][0]
    definition=senses['definitions']
    if(code==404):
        return "The word does not exist"
    return definition
# print(definition)