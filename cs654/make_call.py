# Download the library from twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
# Get these credentials from http://twilio.com/user/account
account_sid = "AC77709cad71509b163f6f3ec522c8c7da"
auth_token = "c858b7751cc0d1260efbe9153ef5f8b4"
client = TwilioRestClient(account_sid, auth_token)
# Make the call
call = client.calls.create(to="919559753562", # Any phone number
from_="7045869183", # Must be a valid Twilio number
url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
print call.sid
