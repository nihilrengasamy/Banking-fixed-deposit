import urllib.request
import json

from flask import * 
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('bankingui.html')

@app.route("/success", methods=['GET','POST'])
def home2():
    if request.method == 'POST':

        data = {
            "Inputs": {
                "data":
                [
                    {
                        "Cloumn2":"request.form['x']",
                        "age" : int(request.form['a']),
                        "job" : "request.form['b']",
                        "marital": "request.form['c']",
                        "education": "request.form['d']",
                        "default": "request.form['e']",
                        "housing":"request.form['f']",
                        "loan":"request.form['g']",
                        "contact":"request.form['h']",
                        "month":"request.form['i']",
                        "duration":int(request.form['j']),
                        "campaign":int(request.form['k']),
                        "pdays":int(request.form['l']),
                        "previous":int(request.form['m']),
                        "poutcome":"request.form['n']",
                        "emp.var.rate":float(request.form['o']),
                        "cons.price.idx":float(request.form['p']),
                        "cons.conf.idx":float(request.form['q']),
                        "euribor3m":float(request.form['r']),
                        "nr.employed":float(request.form['s'])
                    },
                ]
            },
            "GlobalParameters": {
                "method": "predict"
            }
        }

        body = str.encode(json.dumps(data))

        url = 'http://ff32e937-0995-4958-a89b-d373e8248865.westus2.azurecontainer.io/score'
        
        api_key = '' # Replace this with the API key for the web service
        
        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

        req = urllib.request.Request(url, body, headers)

        try:
            response = urllib.request.urlopen(req)

            result = response.read()
            
            print(result)
        
        except urllib.error.HTTPError as error:
        
            print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
            print(error.info())
            print(json.loads(error.read().decode("utf8", 'ignore')))

    return render_template('success.html', data = result)

if __name__ == '__main__':
    app.run(debug = True)