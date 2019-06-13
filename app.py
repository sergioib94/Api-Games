import requests

from flask import Flask,render_template,request,redirect
app = Flask(__name__)

URL_BASEv1="https://fortnite-public-api.theapinetwork.com"
URL_BASEv2="https://fortnite-api.theapinetwork.com"

@app.route ('/',methods=['GET','POST'])
def inicio():
    return render_template("index.html")

@app.route ('/stats',methods=["GET",'POST'])
def stats():
    user = request.form.get("Usuario")
    payload = {'username' : user}
    r=requests.get(URL_BASEv1 + "/prod09/users/id", params=payload)
    if r.status_code == 200:
        doc=r.json()

app.run(debug=True)

#def stats():

#@app.route ('/store')
#@app.route ('/news_&_events')
