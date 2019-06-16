import os,requests

from flask import Flask,render_template,request,redirect,abort
app = Flask(__name__)

URL_BASEv2="https://fortnite-api.theapinetwork.com"
URL_BASEv1="https://fortnite-public-api.theapinetwork.com"

key = os.environ['keyapi']

@app.route ('/',methods=['GET','POST'])
def inicio():
    return render_template("index.html")

@app.route ('/stats',methods=['GET','POST'])
def user():
    user = request.form.get("usuario")
    if user != "":
        payload = {'username' : user}
        r=requests.get(URL_BASEv1 + "/prod09/users/id", params=payload)
        if r.status_code == 200:
            datos=r.json()
            ID = datos["uid"]
            if ID != "":
                payload = {'user_id' : ID}
                r2=requests.get(URL_BASEv1 + "/prod09/users/public/br_stats_v2", params=payload)
                if r.status_code == 200:
                    stats=r.json()
                    for dev in stats["device"]:
                        if "keyboardmouse" in dev:
                            for datos in stats["keyboardmouse"]["deimos"]:
                                return render_template("stats.html", datos=datos)
                        if "gamepad" in dev:
                            for datos in stats["gamepad"]["deimos"]:
                                return render_templat("stats.html", datos=datos)
                        else:
                            Error="No se encuentran datos del jugador"
                            return render_templat("stats.html", datos=error)

@app.route ('/store',methods=['GET'])
def items():
    headers = {'Authorization' : key}
    r=requests.request('GET',URL_BASEv2 + "/items/list", headers=headers)
    if r.status_code == 200:
        doc=r.json()
        items = []
        for item in doc["data"]:
            items.append(item["item"])
        return render_template("store.html", items=items)

@app.route('/news&events',methods=['GET','POST'])
def news():
    headers = {'Authorization' : key}
    r=requests.request('GET',URL_BASEv2 + "/br_motd/get", headers=headers)
    if r.status_code == 200:
        doc=r.json()
        news = []
        for new in doc["data"]:
            news.append(new)
        return render_template("news.html", news=news)

    #headers = {'Authorization' : key}
    #r=requests.request('GET',URL_BASEv2 + "/stw_motd/get", headers=headers)
    #if r.status_code == 200:
    #    doc=r.json()
    #    events = []
    #    for i in doc["data"]:
    #        events.append(i)
    #    return render_template("news.html", events=events)
app.run(debug=True)
