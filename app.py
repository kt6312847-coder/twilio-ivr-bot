from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/voice", methods=["POST"])
def voice():
    resp = VoiceResponse()
    resp.say("مرحباً! هذا رد تلقائي من البوت. شكراً لاتصالك.", language="ar-SA")
    return Response(str(resp), mimetype='text/xml')

@app.route("/", methods=["GET"])
def home():
    return "Twilio IVR Bot is running."

if __name__ == "__main__":
    app.run(debug=True)
