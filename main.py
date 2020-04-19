# -*- coding: UTF-8 -*-
import flask
import json
import csv
import pandas as pd
import codecs
import os
app = flask.Flask(__name__, template_folder='templates')


def read_csv():
    csv_rows = []
    with open("data.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        title = reader.fieldnames
        for row in reader:
            csv_rows.extend([{title[i]: row[title[i]] for i in range(len(title))}])
        return csv_rows


def write_json(data, json_file):
    with open(json_file, "w") as f:
        f.write(json.dumps(data))


def read_born():
    born = []
    city = {}
    num = []
    with open("people.json", "r") as data:
        file = json.load(data)
        for line in file:
            if line["出生地"][:2] not in born:
                if line["出生地"] == "":
                    continue
                born.append(line["出生地"][:2])
                city[line["出生地"][:2]] = 1
            else:
                city[line["出生地"][:2]] += 1
    for keys in city.keys():
        num.append(city[keys])
    # _csv = pd.DataFrame({'place': born, 'num': num}).to_csv("back.csv", index=False, sep=',')
    print(city)


def read_back():
    back = []
    list = {}
    num = []
    with open("people.json", "r") as data:
        file = json.load(data)
        for line in file:
            d = line["专业背景"]
            if d not in back:
                if d == "":
                    continue
                back.append(d)
                list[d] = 1
            else:
                list[d] += 1
    for keys in list.keys():
        num.append(list[keys])
    _csv = pd.DataFrame({'back': back, 'num': num}).to_csv("back.csv", index=False, sep=',')

# data = read_csv()
# write_json(data, "people.json")
# born_city = read_born()
# read_back()


@app.route('/', methods=['GET', 'POST'])
def index0():
    return flask.render_template("index.html")


@app.route()


if __name__ == '__main__':
    app.run()
