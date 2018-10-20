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

url = "https://manaleks.azurewebsites.net/#home"


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        district = request.form['district']

        if district == "":
            return render_template('sorry.html')
            
        # yandex_dat = yandex_data.super_run(phrases=phrases, cities=cities)
        # data = {"yandex_data":yandex_dat}

        #with open("log.txt", "a") as f:
        #    f.write("\n" + "Request yandex answer: " + str(data) + "\n" + "###" * 50 + "\n")

        #dataj = json.dumps(data, "utf-8")

        #return render_template('main.html', result_yandex=dataj)

        region = geo.get_region(district)
        districts.remove(district)
        districts.insert(0, district)
        return render_template('main.html', districts=districts, regions=region)

    return render_template('main.html', districts=districts)

@app.route('/<distr>', methods=['GET', 'POST'])
def distr(distr):
    if request.method == 'POST':
        district = request.form['district']

        if district == "":
            return render_template('sorry.html')
            
        # yandex_dat = yandex_data.super_run(phrases=phrases, cities=cities)
        # data = {"yandex_data":yandex_dat}

        #with open("log.txt", "a") as f:
        #    f.write("\n" + "Request yandex answer: " + str(data) + "\n" + "###" * 50 + "\n")

        #dataj = json.dumps(data, "utf-8")

        #return render_template('main.html', result_yandex=dataj)

        region = geo.get_region(district)
        districts.remove(district)
        districts.insert(0, district)
        return render_template('main.html', districts=districts, regions=region)

    return render_template('main.html', districts=distr)

@app.route('/1/1')
def hello():
    return redirect(url, code=302)

if __name__ == "__main__":
    app.run(debug=True)