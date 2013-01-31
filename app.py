from flask import Flask
from flask import request
from flask import url_for
from flask import render_template
from twilio import twiml
from twilio.util import TwilioCapability
from twilio.rest import TwilioRestClient
import os
from random import choice
from local_settings import *

# SONYA_APP_SID
# BSS_SPAM_ID

# Declare and configure application
app = Flask(__name__, static_url_path='/static')
app.config['ACCOUNT_SID'] = ACCOUNT_SID
app.config['AUTH_TOKEN'] = AUTH_TOKEN
app.config['BSSSPAM_APP_SID'] = BSSSPAM_APP_SID
app.config['BSS_SPAM_ID'] = BSS_SPAM_ID


@app.route('/')
def index():
    reason = quotes()
    capability = TwilioCapability(app.config['ACCOUNT_SID'],
        app.config['AUTH_TOKEN'])
    capability.allow_client_outgoing(app.config['BSSSPAM_APP_SID'])
    token = capability.generate()
    return render_template('index.html', token=token, reason=reason)


@app.route('/sms', methods=['POST'])
def sms():
    r = twiml.Response()
    reason = quotes()
    r.sms(reason)
    return str(r)


def quotes():
    reasons = [
            'Funny quote of the hour: The quickest way to double your money is to fold it in half and put it back in your pocket.',
            'Funny quote of the hour: When Life Gives You Questions, Google has Answers',
            'Funny quote of the hour: If at first you don\'t succeed, call it version 1.0.',
            'Funny quote of the hour: Microsoft - You\'ve got questions. We\'ve got dancing paperclips.',
            'Funny quote of the hour: There are 10 types of people in the world: those who understand binary, and those who don\'t.',
            'Funny quote of the hour: I\'m not anti-social; I\'m just not user friendly',
            'Funny quote of the hour: My software never has bugs. It just develops random features.',
            'Funny quote of the hour: I would love to change the world, but they won\'t give me the source code.',
            'Funny quote of the hour: Be nice to the nerds, you will probably end up working for them.',
            'Funny quote of the hour: Artificial Intelligence is no match for Natural Stupidity.',
            'Funny quote of the hour: A computer lets you make more mistakes faster than any invention in human history - with the possible exceptions of handguns and tequila.',
            'Funny quote of the hour: In a world without fences and walls, who needs Gates and Windows?']
    return choice(reasons)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))

    if port == 5000:
        app.debug = True

    app.run(host='0.0.0.0', port=port)
