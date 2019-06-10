import requests

user = input ("Nombre de usuario: " )

payload = {'username' : user}

r=requests.get('https://fortnite-public-api.theapinetwork.com/prod09/users/id', params=payload)
if r.status_code == 200:
    doc=r.json()

    print ("uid","-", doc ["uid"])
    print ("username","-",doc ["username"])
    print ("platforms: ")
    for platforms in doc ["platforms"]:
        print ("-",platforms, end="")
        print ("")

    stats = input("¿Quiere ver las estadisticas basicas? (s/n): ")
    ID = doc ["uid"]
    if stats == "S" or stats == "s":
        payload2 = {'user_id' : ID}
        r2=requests.get('https://fortnite-public-api.theapinetwork.com/prod09/users/public/br_stats_v2', params=payload2)
        if r2.status_code == 200:
            stats=r2.json()
            for dev in stats ["devices"]:
                if "keyboardmouse" in dev:
                    print ("")
                    print ("Estadisticas en competitivo (pc):")
                    if "comp" in stats["data"]["keyboardmouse"]:
                        for comp,valor in stats["data"]["keyboardmouse"]["comp"]["solo"].items():
                            print ("*",comp,"-",valor)
                        print ("")
                    else:
                        print ("")
                        print ("El jugador no cuenta con estadisticas en competitivo")
                        print ("")
                    print ("Estadisticas en solitario (pc): ")
                    if "deimos" in stats["data"]["keyboardmouse"]:
                        if "solo" in stats["data"]["keyboardmouse"]["deimos"]:
                            for solo,valor in stats["data"]["keyboardmouse"]["deimos"]["solo"].items():
                                print ("*",solo,"-",valor)
                                print ("")
                        else:
                            print ("")
                            print ("El jugador no cuenta con estadisticas en solitario")
                            print ("")
                    else:
                        print ("Sin datos")
                    print ("Estadisticas en duos (pc): ")
                    if "deimos" in stats["data"]["keyboardmouse"]:
                        if "duo" in stats["data"]["keyboardmouse"]["deimos"]:
                            for duo,valor in stats["data"]["keyboardmouse"]["deimos"]["duo"].items():
                                print ("*",duo,"-",valor)
                                print ("")
                        else:
                            print ("")
                            print ("El jugador no cuenta con estadisticas en duo")
                            print ("")
                    else:
                        print ("Sin datos")
                    print ("Estadisticas en Escuadron (pc): ")
                    if "deimos" in stats["data"]["keyboardmouse"]:
                        if "squad" in stats["data"]["keyboardmouse"]["deimos"]:
                            for squad,valor in stats["data"]["keyboardmouse"]["deimos"]["squad"].items():
                                print ("*",squad,"-",valor)
                                print ("")
                        else:
                            print ("")
                            print ("El jugador no cuenta con estadisticas en escuadron")
                            print ("")
                    else:
                        print ("Sin datos")
                if "gamepad" in dev:
                    print ("Estadisticas en solitario (ps4/nintendo): ")
                    if "defaultsolo" in stats["data"]["gamepad"]:
                        for solo,valor in stats["data"]["gamepad"]["defaultsolo"]["default"].items():
                            print ("*",solo,"-",valor)
                        print ("")
                    else:
                        print ("")
                        print ("El jugador no cuenta con estadisticas en solitario")
                        print ("")
                    print ("Estadisticas en duos (ps4/nintendo): ")
                    if "defaultduo" in stats["data"]["gamepad"]:
                        for duo,valor in stats["data"]["gamepad"]["defaultduo"]["default"].items():
                            print ("*",duo,"-",valor)
                        print ("")
                    else:
                        print ("")
                        print ("El jugador no cuenta con estadisticas en duo")
                        print ("")
                    print ("Estadisticas en Escuadron (ps4/nintendo): ")
                    if "defaultsquad" in stats["data"]["gamepad"]:
                        for squad,valor in stats["data"]["gamepad"]["defaultsquad"]["default"].items():
                            print ("*",squad,"-",valor)
                        print ("")
                    else:
                        print ("")
                        print ("El jugador no cuenta con estadisticas en escuadron")
else:
    print ("En estos momentos no se pueden mostrar las estadisticas, intentelo mas tarde")
