from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

@app.route('/wx_anger6/')
def index():
    signature = request.args.get('signature')
    timestamp = request.args.get('timestamp')
    nonce = request.args.get('nonce')
    echostr = request.args.get('echostr')
    print('signature:%s echostr:%s nonce:%s timestamp:%s'%(signature, echostr, nonce, timestamp))
    return make_response(echostr)

