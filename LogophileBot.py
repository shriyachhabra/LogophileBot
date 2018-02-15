from flask import Flask,request
from pymessenger.bot import Bot
import os
app = Flask(__name__)

ACCESSTOKEN='EAAF5jHKhUdgBAOjfCWUYGrAbZCoZBWPgwjudtXEZBGZAQJCoQgFfQm2Xg9ZAFamlg6YjwEH0IaaaimdW9c5AYeMCCGaGRxPquAT8GGXpJWWuxErabvde495EseEAweFoVB6LUeKzahG3SB0F5zfWEjI5ZAIGE8ZC7xOSpftsNtIZAZBwMrj5XxZC8y'
VERIFYTOKEN='aaruchinu'
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

def handle_mssg(rec_id,msg):
    txt=msg.split(' ',1)
    response_text=''
    if(txt[0]=="hey"):
        response_text="hi"
        send_message(rec_id,response_text)

    return "handled"

@app.route('/',methods=['GET'])
def get_mssg():
    """Before allowing people to message your bot, Facebook has implemented a verify token
           that confirms all requests that your bot receives came from Facebook."""
    token_sent = request.args.get("hub.verify_token")
    return verify_fb_token(token_sent)



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
