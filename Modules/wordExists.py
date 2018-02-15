import requests
import json

def word_exists(word):
 app_id = 'd520dc72'
 app_key = '9636a335f1d422e70aa5a9b2381f6517'

 language = 'en'
 word_id = word
 url = 'https://od-api.oxforddictionaries.com:443/api/v1/inflections/' + language + '/' + word_id.lower()
 r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
 code="code {}\n".format(r.status_code)
 print(code)

 if(code=='404'):
     return "The word does not exist"

 return """Great!The word exists.
          You know the language well."""
# print("text \n" + r.text)
# print("json \n" + json.dumps(r.json()))