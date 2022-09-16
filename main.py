


from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

from flask_cors import CORS

import finance as my
import json


app = Flask(__name__)


CORS(app)



app.route('/')
def index():
    return '';

@app.route('/api/<ticker>', methods=['GET'])
def get_stock(ticker):
    stock = my.Stock(ticker)
    return stock.toJson()


app.run()
