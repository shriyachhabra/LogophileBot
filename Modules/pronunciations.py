import requests
import json

def pronunciation(word):

 app_id = 'd520dc72'
 app_key = '9636a335f1d422e70aa5a9b2381f6517'

 language = 'en'
 word_id = word

 url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()

 r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
 code=r.status_code
 if(code==404):
     return "Word does not exist"
 r=r.json();
 res=r['results'][0]
 le=res['lexicalEntries'][0]
 pro=le['pronunciations'][0]
 af=pro['audioFile']
 print(af)
 return af