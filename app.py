from flask import Flask, render_template, request, redirect, url_for
import csv
import pyodbc
import pandas as pd
import numpy as np
import os
import time
app = Flask(__name__)

server = 'mysqlserveradb.database.windows.net'
database = 'archana'
username = 'archanat'
password = 'Dheeraj92'
#driver= '{ODBC Driver 17 for SQL Server}'
driver='/usr/local/lib/libmsodbcsql.17.dylib'

@app.route('/')
def hello():
	return render_template('home.html')

#sql query 
@app.route('/five', methods=["POST","GET"])
def earthquake1():
	cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
	crsr = cnxn.cursor()
	earthquakes=[]
	quakes={'Magnitude':'Count of Earthquakes',}
 	# quakes={}
 	#for i in range(+lat1+, +lat2+):
	lat1 = request.form.get('lat1')
	lat2 = request.form.get('lat2')
	query = "SELECT * FROM v WHERE v.Latitude BETWEEN "+lat1+" AND "+lat2+" "
    #query="Select count(*) from [dbo].[all_month] where mag="+str(i)
	crsr.execute(query)
	val=crsr.fetchall()
	val=int(val[0][0])
	earthquakes.append(val)
	#quakes['Mag= '+str(i)]=val
	return render_template('five.html',data=quakes)

@app.route('/six', methods=["POST", "GET"])
def six():
	cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};PORT=1433;SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
	cursor = cnxn.cursor()
	country = request.form.get('country')
	cursor.execute("SELECT * FROM [dbo].[v] WHERE [dbo].[v].[Country] = "+country+" ")
	row = cursor.fetchall()
	count = len(row)
	return render_template('six.html', row=row, count=count)

@app.route('/seven', methods=["POST","GET"])
def part2():
	cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};PORT=1433;SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
	crsr = cnxn.cursor()
	num1 = request.form.get('num1')
	num2 = request.form.get('num2')
	row = cursor.fetchall()
	count = len(row)
	return render_template("seven.html", row=row, count=count)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)