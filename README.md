<p align="center">
 <img width="200px" src="https://avatars0.githubusercontent.com/u/71754745?s=400&u=eb42f9020f213811c28ae3ef4948bf088d22890f&v=4" align="center" alt="WatABot" />
 <h2 align="center">WatABot: Whatsapp Buisness bot implementation using twilio and flask.</h2>
</p>

<p align="center">
 <a href="https://github.com/WatABot/WatABot/releases">
      <img alt="Releases" src="https://img.shields.io/github/v/release/WatABot/WatABot?include_prereleases&color=blueviolet" />
    </a>
    <a href="https://github.com/WatABot/WatABot/blob/master/LICENSE">
      <img alt="License" src="https://img.shields.io/github/license/WatABot/WatABot?color=orange" />
    </a>
 <a href="https://github.com/WatABot/WatABot/graphs/contributors">
      <img alt="Contributors" src="https://img.shields.io/badge/Contributors-4-green" />
    </a>
    <a href="https://github.com/WatABot/WatABot">
      <img src="https://img.shields.io/github/languages/count/WatABot/WatABot" />
    </a>
    <a href="https://github.com/WatABot/WatABot/network/members">
      <img alt="Forks" src="https://img.shields.io/github/forks/WatABot/WatABot?style=social" />
    </a>
    <a href="https://github.com/WatABot/WatABot/stargazers">
      <img alt="Github Stars" src="https://img.shields.io/github/stars/WatABot/WatABot?style=social" />
    </a>
  </p>
  
## Introduction

A Whatsapp buisness bot using Twillio API and flask server. The bot can include multiple python scripts/modules and generate output which can be sent via twilio API.
## Local Setup
### Requirements
- Python >=3.6;
- flask
- pandas;
- nltk;
- keras
- tensorflow
- twillo API token
## Installing and running
```bash
git clone https://github.com/WatABot/WatABot/
cd WatABot
pip3 install -r requirements.txt
python3 run.py
```

### Using Twillo Whatsapp Bot
```
Add this no to your contacts: +14155238886 
Message "  join apart-then "
Then Type "Hi"
```
``` 
ℹ️ Bot Usage Instructions & Guide

1) Command: !help
   Description: Provides information on how to use the bot with examples.

2) Command: !text
   Description: Checks whether an whatsapp forward or online information is fake or not. The input should be in text format.
   Example: !check Virat Kohli is the captain of team india cricket team.
   Output: Sends a text response where the input information is fake or not.

3) Command: !link
   Description: Checks where an online news article is fake or not. The input should be the news article link.
   Example: !link https://www.cnn.com/2020/09/23/asia/china-india-border-troop-agreement-intl-hnk/index.html.
   Output: Sends a text response where the input information is fake or not.

4) Command: !alerts
   Description: Receive alerts directly from police authorities.
   Output: Sends important alerts from police authorities.

5) Command: !contact
   Description: Contact authorities/team to get help.
   Output: Sends contact information.
```

For further documentation refer to : [Documentation!](https://github.com/WatABot/WatABot/blob/master/Assam%20Police%20Hackathon%20Documentaion.pdf)
> **_NOTE:_** 
You need to get a Twillo API token, for the whatsapp bot to work. 
Add your token in `https://github.com/WatABot/WatABot/blob/master/twilio-token.txt` file
