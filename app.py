from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/voice", methods=['POST'])
def voice():
    response = VoiceResponse()
    response.say("مرحبًا، هذا اختبار من خدمة الرد الآلي.")
    return str(response)

