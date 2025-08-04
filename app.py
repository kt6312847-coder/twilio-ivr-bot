from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/voice", methods=['POST'])
def voice():
    resp = VoiceResponse()
    resp.say("مرحبًا بك عند طه. شكرًا لاتصالك.", language="ar-XA", voice="Polly.Zeina")
    return Response(str(resp), mimetype='text/xml')

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=10000)

