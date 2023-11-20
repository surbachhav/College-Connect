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


@app.route('/table')
def table():
   mycursor.execute("SELECT * FROM Colleges")
   data = mycursor.fetchall()
   return render_template('table.html', data=data)




@app.route('/order_by_act')
def order_by_act():
   mycursor.execute("SELECT * FROM Colleges ORDER BY act_avg")
   data = mycursor.fetchall()
   return render_template('table.html', data=data)




@app.route('/order_by_sat')
def order_by_sat():
   mycursor.execute("SELECT * FROM Colleges ORDER BY sat_avg")
   data = mycursor.fetchall()
   return render_template('table.html', data=data)




@app.route('/order_by_class_size')
def order_by_class_size():
   mycursor.execute("SELECT * FROM Colleges ORDER BY enrollment")
   data = mycursor.fetchall()
   return render_template('table.html', data=data)




@app.route('/order_by_acceptance_rate')
def order_by_acceptance_rate():
   mycursor.execute("SELECT * FROM Colleges ORDER BY acceptance_rate")
   data = mycursor.fetchall()
   return render_template('table.html', data=data)




@app.route('/order_by_cost')
def order_by_cost():
   mycursor.execute("SELECT * FROM Colleges ORDER BY cost")
   data = mycursor.fetchall()
   return render_template('table.html', data=data)




@app.route('/order_by_rank')
def order_by_rank():
   mycursor.execute("SELECT * FROM Colleges ORDER BY national_rank")
   data = mycursor.fetchall()
   return render_template('table.html', data=data)




@app.route('/order_by_gpa')
def order_by_gpa():
   mycursor.execute("SELECT * FROM Colleges ORDER BY hs_gpa")
   data = mycursor.fetchall()
   return render_template('table.html', data=data)




@app.route('/save_values')
def save_values():
   data = request.get_json()
   min_value = data['min']
   max_value = data['max']
   connection = psycopg2.connect(**db_config)
   mycursor = connection.cursor()


   try:
       query = "SELECT * FROM your_table WHERE cost BETWEEN %s AND %s"
       mycursor.execute(query, (min_value, max_value))


       data = mycursor.fetchall()
       return render_template('table.html', data=data)


   except Exception as e:
       print(f"Error: {e}")


   finally:
       # Close the cursor and connection
       mycursor.close()
       connection.close()

@app.route('/check_pub')
def check_pub():
   mycursor.execute("SELECT * FROM Colleges WHERE Institutional_Control = 'public'")
   data = mycursor.fetchall()
   return render_template('table.html', data=data)


@app.route('/check_priv')
def check_priv():
   mycursor.execute("SELECT * FROM Colleges WHERE Institutional_Control = 'private'")
   data = mycursor.fetchall()
   return render_template('table.html', data=data)


@app.route('/check_prop')
def check_prop():
   mycursor.execute("SELECT * FROM Colleges WHERE Institutional_Control = 'proprietary'")
   data = mycursor.fetchall()
   return render_template('table.html', data=data)


@app.route('/mycolleges')
def colleges():
   return "<h1>View My Colleges Here!</h1>"

s = HTMLSession()
app.run(host="127.0.0.1", port=9999, debug=True, threaded=True)
