import requests
import urllib.parse

geocode_url = "https://graphhopper.com/api/1/geocode?"
route_url = "https://graphhopper.com/api/1/route?"
idioma = "es"
key = "d16ba5f4-0aa9-4fe5-8db1-df69ad0d97f8"      # Reemplace con su API key de Graphhopper


def geocoding(location, key):
    while location == "":
        location = input("Ingrese nuevamente la ubicación: ")
    geocode_url = "https://graphhopper.com/api/1/geocode?"
    url = geocode_url + urllib.parse.urlencode({"q": location, "limit": "1", "key": key})

    replydata = requests.get(url)
    json_data = replydata.json()
    json_status = replydata.status_code

    if json_status == 200 and len(json_data["hits"]) != 0:
        lat = json_data["hits"][0]["point"]["lat"]
        lng = json_data["hits"][0]["point"]["lng"]
        name = json_data["hits"][0]["name"]
        value = json_data["hits"][0]["osm_value"]

        if "country" in json_data["hits"][0]:
            country = json_data["hits"][0]["country"]
        else:
            country = ""

        if "state" in json_data["hits"][0]:
            state = json_data["hits"][0]["state"]
        else:
            state = ""

        if len(state) != 0 and len(country) != 0:
            new_loc = name + ", " + state + ", " + country
        elif len(state) != 0:
            new_loc = name + ", " + state
        elif len(country) != 0:
            new_loc = name + ", " + country
        else:
            new_loc = name

        print("URL de la API de Geocodificación para " + new_loc + " (Tipo de ubicación: " + value + ")\n" + url)
    else:
        if json_status == 200:
            print("No se encontraron resultados para: " + location)
            json_status = 404
        else:
            print("Error de geocodificación (código " + str(json_status) + "). Revise la API key.")
        lat = "null"
        lng = "null"
        new_loc = location
    return json_status, lat, lng, new_loc


while True:
    loc1 = input("Ubicación de partida (s/salir para terminar): ")
    if loc1.strip().lower() == "salir" or loc1.strip().lower() == "s":
        break
    orig = geocoding(loc1, key)

    loc2 = input("Destino (s/salir para terminar): ")
    if loc2.strip().lower() == "salir" or loc2.strip().lower() == "s":
        break
    dest = geocoding(loc2, key)

    print("=================================================")
    if orig[0] == 200 and dest[0] == 200:
        op = "&point=" + str(orig[1]) + "%2C" + str(orig[2])
        dp = "&point=" + str(dest[1]) + "%2C" + str(dest[2])
        paths_url = route_url + urllib.parse.urlencode({"key": key, "locale": idioma}) + op + dp
        replydata = requests.get(paths_url)
        paths_status = replydata.status_code
        paths_data = replydata.json()
        print("Estado de la API de Rutas: " + str(paths_status) + "\nURL de la API de Rutas:\n" + paths_url)

        print("=================================================")
        print("Indicaciones desde " + orig[3] + " hasta " + dest[3])
        print("=================================================")
        if paths_status == 200:
            miles = (paths_data["paths"][0]["distance"]) / 1000 / 1.61
            km = (paths_data["paths"][0]["distance"]) / 1000
            sec = int(paths_data["paths"][0]["time"] / 1000 % 60)
            min = int(paths_data["paths"][0]["time"] / 1000 / 60 % 60)
            hr = int(paths_data["paths"][0]["time"] / 1000 / 60 / 60)
            print("Distancia recorrida: {0:.2f} millas / {1:.2f} km".format(miles, km))
            print("Duración del viaje: {0:02d}:{1:02d}:{2:02d}".format(hr, min, sec))
            print("=================================================")
            for each in range(len(paths_data["paths"][0]["instructions"])):
                path = paths_data["paths"][0]["instructions"][each]["text"]
                distance = paths_data["paths"][0]["instructions"][each]["distance"]
                print("{0} ( {1:.2f} km / {2:.2f} millas )".format(path, distance / 1000, distance / 1000 / 1.61))
            print("=============================================")
        else:
            print("Error al obtener la ruta: " + str(paths_data.get("message", "sin detalle")))
    else:
        print("No se pudo calcular la ruta: revise las ubicaciones ingresadas.")

print("Programa finalizado. ¡Hasta luego!")