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

***What Happens:***
***1***. *The target receives the SMS with the link.*
***2***. *When they click the link:*
***3***. *The server logs their IP address and user-agent.*
***4***. *If they allow geolocation access, the latitude and longitude are also logged.*

**Example**
`When the link is clicked:`

***Console logs:***
```yaml
Copy code
IP Address: 127.0.0.1
User Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/605.1.15
Latitude: 53.8371663
Longitude: -9.3515381
```
***Lookup the Latitude and Logitude on Google Maps for a surprise :)***

**Important Notes**
***Ethical Use:***
*Ensure the target has explicitly consented to this process.*
***Legal Compliance:***
*Verify compliance with local laws and regulations.*
***Testing:***
*Use ngrok for testing, but for production, deploy on a proper hosting service (e.g., AWS, Azure, etc.).*

***Feel Free to modify the code to your liking ifywim.***
**Happy Hacking ;)**
