from flask import Flask,request
from pymessenger.bot import Bot
from Modules.wordExists import *
from Modules.meaning import *
from Modules.synonyms import *
from Modules.antonyms import *
from Modules.pronunciations import *
from Modules.facts import *
from Modules.hello import *
import os
app = Flask(__name__)

ACCESSTOKEN='EAAF5jHKhUdgBAJ2CAResm3HcnbZC2b0NclRN8K0POynZBklRg2IaieWKd7MUy0KwuRUEofBpc6nVXZBB307xnZBM8UKYUyBPLl56hjZCbupOvmt1RJmXazOXOPZC5vcOWhCOCR89fnbpT9y2beZCkuMH0yRT5dJMSGoha40Fb3RIndGgx4unGtr'
VERIFYTOKEN='aaruchinu1'
bot = Bot(ACCESSTOKEN)

@app.route('/',methods=['POST'])
def post_mssg():
    output = request.get_json()
    for event in output['entry']:
        messaging = event['messaging']
        for message in messaging:
            print(message)

            if message.get('message'):
                # Facebook Messenger ID for user so we know where to send response back to
                recipient_id = message['sender']['id']
                if message['message'].get('attachments'):
                    response_sent_nontext ="Ask me something useful dude :P"
                    send_message(recipient_id, response_sent_nontext)
                    return "non text response"
                msg = message['message'].get('text')
                handle_mssg(recipient_id,msg)
    return "message received"


@app.route('/',methods=['GET'])
def get_mssg():
    """Before allowing people to message your bot, Facebook has implemented a verify token
           that confirms all requests that your bot receives came from Facebook."""
    token_sent = request.args.get("hub.verify_token")
    return verify_fb_token(token_sent)

def handle_mssg(rec_id,msg):
    txt=msg.split(' ',1)

    response_text=''
    if(txt[0].lower() in ['hey','hi','hello','yo','ssup','yuhu']):
        response_text=start_Convo
    elif(txt[0].lower() in ['thanks','thank']):
        response_text:thanks
    elif(txt[0]=="ex?"):
        response_text=word_exists(txt[1])
    elif(txt[0]=="def?"):
        response_text=word_meaning(txt[1])
    elif(txt[0]=="syn?"):
        response_text=synonyms(txt[1])
    elif(txt[0]=="ant?"):
        response_text=antonyms(txt[1])
    elif(txt[0]=="pro?"):
        response_text=pronunciation(txt[1])
    elif(txt[0]=="fact?"):
        response_text=get_facts()
    else:
        response_text="Be Specific"
    send_message(rec_id,response_text)

    return "handled"


def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error
    if token_sent == VERIFYTOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 6000))
    app.run(host='0.0.0.0', port=port)
    app.run(debug=True)
