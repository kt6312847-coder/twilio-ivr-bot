from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/voice", methods=["GET", "POST"])
def voice():
    if request.method == "GET":
        return "✅ Twilio bot is running. Send a POST request to use it."

    # POST: handle Twilio call
    response = VoiceResponse()
    response.say("مرحبًا! هذا رد تجريبي من روبوت الرد الآلي. شكرًا لاتصالك.", language="ar-SA")
    return Response(str(response), mimetype="application/xml")

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")



