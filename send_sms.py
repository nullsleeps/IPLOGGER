from twilio.rest import Client

# Twilio credentials
account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hi! Check me out broski: http://your-ngrok-url.ngrok.io/track",
    from_='+1234567890',  # Your Twilio phone number
    to='+14155552671'  # Target phone number
)

print(f"Hac message sent :) : {message.sid}")
