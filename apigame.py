import requests

user = input ("Nombre de usuario: " )

payload = {'username' : user}

r=requests.get('https://fortnite-public-api.theapinetwork.com/prod09/users/id', params=payload)
if r.status_code == 200:
    doc=r.json()
    ID = doc ["uid"]
    print ("uid","-", doc ["uid"])
    print ("username","-",doc ["username"])
    print ("platforms: ")
    for platforms in doc ["platforms"]:
        print ("-",platforms, end="")
        print ("")

    stats = input("¿Quiere ver las estadisticas basicas? (s/n): ")
    if stats == "S" or stats == "s":
        payload2 = {'user_id' : ID}
        r2=requests.get('https://fortnite-public-api.theapinetwork.com/prod09/users/public/br_stats_v2', params=payload2)
        if r2.status_code == 200:
            stats=r2.json()
            for dev in stats ["devices"]:
                if "keyboardmouse" in dev:
                    print ("Estadisticas en solitario: ")
                    for solo,valor in stats["data"]["keyboardmouse"]["deimos"]["solo"].items():
                        print ("*",solo,"-",valor)
                    print ("")
                    print ("Estadisticas en duos: ")
                    for duo,valor in stats["data"]["keyboardmouse"]["deimos"]["duo"].items():
                        print ("*",duo,"-",valor)
                    print ("")
                    print ("Estadisticas en Escuadron: ")
                    for squad,valor in stats["data"]["keyboardmouse"]["deimos"]["squad"].items():
                        print ("*",squad,"-",valor)
                elif "gamepad" in dev:
                    print ("Estadisticas en solitario: ")
                    for solo,valor in stats["data"]["gamepad"]["deimos"]["solo"].items():
                        print ("*",solo,"-",valor)
                    print ("")
                    print ("Estadisticas en duos: ")
                    for duo,valor in stats["data"]["gamepad"]["deimos"]["duo"].items():
                        print ("*",duo,"-",valor)
                    print ("")
                    print ("Estadisticas en Escuadron: ")
                    for squad,valor in stats["data"]["gamepad"]["deimos"]["squad"].items():
                        print ("*",squad,"-",valor)
        else:
            print ("No se encuentran datos del jugador")
