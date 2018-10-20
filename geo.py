# -*- coding: utf8 -*-
import geojson
import json

def get_region(district):
    with open("mo.geojson", encoding="utf-8") as f:
        gj = geojson.load(f)
    features = gj['features']
    districts = {}
    for feature in features:
        if len(feature['geometry']['coordinates'][0][0]) != 2:
            district_geo = feature['geometry']['coordinates'][0][0]
        else:
            district_geo = feature['geometry']['coordinates'][0]

        if feature["properties"]['NAME_AO'] not in districts.keys():
            districts[feature["properties"]['NAME_AO']] = [district_geo]
        else:
            districts[feature["properties"]['NAME_AO']].append(district_geo)

    if district == "Все районы":
        return districts
    else:
        return {district:districts[district]}


if __name__ == "__main__":
    #for r in get_region():
    #    print(r) 
    d = get_region("Все районы")
    print(d)
    print("all ok")