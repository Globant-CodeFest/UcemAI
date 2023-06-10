from flask import Flask, jsonify, request, send_from_directory
import os, json, shutil
from werkzeug.utils import secure_filename
from flask_cors import CORS
from data import obtener_columna_como_array
from alerta import diferencia_fechas
import pandas as pd


app = Flask(__name__)

CORS(app)

@app.route('/api/v1')
def hello():
    return "Hello word"

@app.route('/api/v1/obtener_columna_como_array', methods=['GET'])
def array():
    column = request.args.get('country')
    path = 'api/static/meteo2.csv'

    return jsonify(obtener_columna_como_array(path, column))



@app.route('/api/v1/alert', methods=['GET'])
def alert():
    country = request.args.get('country')
    desastre = request.args.get('disaster')

    diferencia_fechas

    return jsonify(diferencia_fechas(country, desastre))


if __name__ == '__main__':
    app.run(debug=True, port=4012)

