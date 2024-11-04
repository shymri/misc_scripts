"""get data from a raw json from malmobybike and convert to usable geojson format"""

import json

with open(r"/home/shannon/Documents/scripts/geojson/malmobybike_raw.json") as f:
    data = json.load(f)

new_data = {"type": "FeatureCollection",
            "features": []}

for d in data:
    name = d['name']
    lat = d['location']['lat']
    lon = d['location']['lon']
    geo = {
        "type": "Feature",
        "geometry": {
            "coordinates": [
                lon,
                lat
            ],
            "type": "Point"
        },
        "properties": {
            "_umap_options": {
                "color": "Orange",
                "iconClass": "Circle"
            },
            "name": name
        }
    }
    new_data["features"].append(geo)

file_p = r"/home/shannon/Documents/scripts/geojson/malmobybike.geojson"

with open(file_p, "w") as outf:
    json.dump(new_data, outf, indent=4)
