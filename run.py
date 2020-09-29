from flask_migrate import Migrate
from os import environ
from sys import exit

from config import config_dict
from app import create_app, db

import os, sys, time, glob
from flask import *
from BotModules import module_fakenews
import json

from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

account_sid = 'DEFAULT'
auth_token = 'DEFAULT'

get_config_mode = environ.get('APPSEED_CONFIG_MODE', 'Debug')

try:
    config_mode = config_dict[get_config_mode.capitalize()]
except KeyError:
    exit('Error: Invalid APPSEED_CONFIG_MODE environment variable entry.')

app = create_app(config_mode) 
Migrate(app, db)

@app.route("/sms", methods=['POST'])

def sms_reply():
    msg = request.form.get('Body')
    num = request.form.get('From')
    global url
    global account_sid
    global account_token
    client = Client(account_sid, auth_token)
    resp = MessagingResponse()
    while msg in ['start','Start', 'run', 'Run', 'HI', 'hi', 'Hai', 'Hello', 'hello', 'Hi']:
        message = client.messages.create(body = '''*A hackathon initiative by Assam Police to tackle fake news. Type info to show usage instructions.* ''',media_url= 'https://cdn.skillenza.com/files/325bad70-29b8-42c4-814c-637bec29f277/AssamPolice_logo.png',from_='whatsapp:+14155238886',to=num)
        return str(resp)
        return str(resp)
    while msg in ['info','INFO','Info']:
        resp.message(''' 
*ℹ️ Fake News Detection/Reporting Tool*

- [ *!help* ] Bot usage Instructions
- [ *!text* ] Checks Text News
- [ *!url* ] Check News Link 
- [ *!alerts* ] Police Fake News Alerts 
- [ *!contact* ] Contct Team

 TYPE *!help* to get usage examples and information.''')
        return str(resp)
    if '!text' in msg:
        news = msg.replace('!text ','')
        news = news.lower()
        print(news)
        final = module_fakenews.run(str(news))
        print(final)
        accuracy = final[0][1]
        print(accuracy)
        accuracy_rounded = round(accuracy, 2)
        print(accuracy_rounded) 
        if accuracy_rounded >= 0.8:
            final_result = "The information is probably true"
        elif accuracy_rounded <= 0.2:
            final_result = "The information is probably fake"
        else:
            final_result = "Need more information, Unsure" 
        contents = 'Your Query: ' + news + '\nResult: ' + final_result + '\nAccuracy: ' + str(round(accuracy_rounded*100, 2)) +'%'
        message = client.messages.create(body=contents,from_='whatsapp:+14155238886',to= num)
        return str(resp)
    elif '!contact' == msg:
        message = client.messages.create(body = 'Created by CyberBots Team @ Assam Police Hackathon',from_='whatsapp:+14155238886',to= num)
        return str(resp)
    elif '!help' in msg:
        resp.message(''' 
*ℹ️ Bot Usage Instructions & Guide*

1) Command: !help
   Description: Provides information on how to use the bot with examples.

2) Command: !text
   Description: Checks whether an whatsapp forward or online information is fake or not. The input should be in text format.
   Example: !check Virat Kohli is the captain of team india cricket team.
   Output: Sends a text response where the input information is fake or not.

3) Command: !url
   Description: Checks where an online news article is fake or not. The input should be the news article link.
   Example: !url https://www.cnn.com/2020/09/23/asia/china-india-border-troop-agreement-intl-hnk/index.html.
   Output: Sends a text response where the input information is fake or not.

4) Command: !alerts
   Description: Receive alerts directly from police authorities.
   Output: Sends important alerts from police authorities.

5) Command: !contact
   Description: Contact authorities/team to get help.
   Output: Sends contact information.

''')
        return str(resp)
    else:
       message = client.messages.create(body = 'Invalid Input, enter !help for commands',from_='whatsapp:+14155238886',to= num)
       return str(resp)

def load_token():
    try:
        with open('twilio-token.txt', 'r') as file:
            for line in file.readlines():
                line = line.replace("\n", "").replace("\r","")
                global account_sid
                global auth_token
                account_sid = line.split(" ")[0]
                auth_token = line.split(" ")[1]
    except:
    	print("exception occured")
    	exit(0)       

if __name__ == "__main__":
    load_token()
    app.run(debug=True,host='10.0.0.4',port=80, threaded=True)
