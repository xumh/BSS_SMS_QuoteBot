'''
Configuration Settings

Includes keys for Twilio, etc.  Second stanza intended for Heroku deployment.
'''

# Uncommet to configure in file.
ACCOUNT_SID = "AC802d88dd13f2e3f8d8bc3f9b95eb9f06" 
AUTH_TOKEN = "a610e5b81d025523706a2bbc381bf5ac"
BSSSPAM_APP_SID = "AP69a2d4c9cdceee480dfa9e9230c586c5"
BSS_SPAM_ID = "+17032913341"


# Begin Heroku configuration - configured through environment variables.
import os
ACCOUNT_SID = os.environ['ACCOUNT_SID']
AUTH_TOKEN = os.environ['AUTH_TOKEN']
BSSSPAM_APP_SID = os.environ['BSSSPAM_APP_SID']
BSS_SPAM_ID = os.environ['BSS_SPAM_ID']
