#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action")= "employee.age":
            result = req.get("result")
            parameters = result.get("parameters")
                var1 = parameters.get("employees")
                age = {'Sophie Quinn':41, 'Diane Russell':49, 'Ruth Cornish':37, 'Ella  Payne':33, 'Julia Nash':27, 'Lisa Miller':32, 'Liam Allan':59, 'Carl Baker':30,'Ava Vance':38}
            speech = "The age of " + var1 + " is " + str(age[var1]
    
            print("Response:")
            print(speech)

            return {
            "speech": speech,
            "displayText": speech,
               #"data": {},
            # "contextOut": [],
            "source": "apiai-denali"
            }
    elif req.get("result").get("action") = "employee.stats":
            result = req.get("result")
            parameters = result.get("parameters")
                var1 = parameters.get("stats")
                var2 = {'Min':27, 'Max':59, 'Mean':38.4}
            speech = "The answer for " + var1 + " is " + str(var2[var1])
            
            print("Response:")
            print(speech)

            return {
            "speech": speech,
            "displayText": speech,
            #"data": {},
            # "contextOut": [],
            "source": "apiai-denali"
            }
        
        else:
             return{}

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')
