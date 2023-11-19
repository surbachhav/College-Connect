from flask import Flask, request, render_template

import psycopg2
from requests_html import HTMLSession
from requests_html import AsyncHTMLSession


conn = psycopg2.connect("dbname=postgres user=postgres password=postgres")
mycursor = conn.cursor()
app = Flask(__name__)


db_config = {
   'host': 'postgres',
   'user': 'postgres',
   'password': 'postgres',
   'database': 'colleges'
}


@app.route('/')
def test():
   return render_template('index.html')

s = HTMLSession()
app.run(host="127.0.0.1", port=9999, debug=True, threaded=True)
