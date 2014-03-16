'''
Configuration Settings

Includes keys for Twilio, etc.  Second stanza intended for Heroku deployment.
'''

# Uncommet to configure in file.
ACCOUNT_SID = "AC63cd1cf15913fcef3b77d83f29b95303"
AUTH_TOKEN = "e39b5e3330543a91e0d5265c85650dd3"
BSSSPAM_APP_SID = "AP8f878da6ab66e40d36a3121d4b46aa47"
BSS_SPAM_ID = "+16175051472"


# Begin Heroku configuration - configured through environment variables.
import os
ACCOUNT_SID = os.environ['ACCOUNT_SID']
AUTH_TOKEN = os.environ['AUTH_TOKEN']
BSSSPAM_APP_SID = os.environ['BSSSPAM_APP_SID']
BSS_SPAM_ID = os.environ['BSS_SPAM_ID']
