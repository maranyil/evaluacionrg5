import csv
from flask import Flask, jsonify

app = Flask(__name__, static_url_path="")


@app.route('/', methods=['GET'])
def csv_to_json():
    path = 'data/employees.csv'
    with open(path, 'r') as file:
        reader = csv.reader(file)
        the_data = list()
        for row in reader:
            the_data.append(row)
        data = [dict(zip(the_data[0], row)) for row in the_data]
        data.pop(0)
        shiny_json = jsonify(data)
        return shiny_json


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
