# -*- coding: utf8 -*-
from flask import Flask, request, render_template, redirect
try:
  import simplejson as json
except:
  import json
  
#import yandex_data
import geo

districts = ["Все районы","Восточный", "Западный","Зеленоградский","Новомосковский","Северный","Северо-Восточный","Северо-Западный", "Троицкий","Центральный","Юго-Восточный","Юго-Западный","Южный"]                    
 
app = Flask(__name__)

url = "https://cityportrait.azurewebsites.net/"


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        district = request.form['district']
        return redirect(url+district, code=302)
    distr = "Все районы"
    region = geo.get_region(distr)
    districts.remove(distr)
    districts.insert(0, distr)
    return render_template('main.html', districts=districts, regions=region)

@app.route('/<distr>', methods=['GET', 'POST'])
def distr(distr):
    if request.method == 'POST':
        district = request.form['district']
        return redirect(url+district, code=302)
        # yandex_dat = yandex_data.super_run(phrases=phrases, cities=cities)
        # data = {"yandex_data":yandex_dat}

        #with open("log.txt", "a") as f:
        #    f.write("\n" + "Request yandex answer: " + str(data) + "\n" + "###" * 50 + "\n")

        #dataj = json.dumps(data, "utf-8")

        #return render_template('main.html', result_yandex=dataj)
        
    if distr in districts:
        region = geo.get_region(distr)
        districts.remove(distr)
        districts.insert(0, distr)
        return render_template('main.html', districts=districts, regions=region)
    else:
        return render_template('main.html', districts=districts)

if __name__ == "__main__":
    app.run(debug=True)