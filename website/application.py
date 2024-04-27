from flask import Flask, render_template, request, jsonify
import json
import mysql.connector
from datetime import datetime, timedelta
from flask_cors import CORS, cross_origin

application = Flask(__name__, static_url_path='/static')
CORS(application)
#app = Flask(__name__)

def db_connection():
	mydb = mysql.connector.connect( host = 'database-2.c9gkgua66wjp.us-east-1.rds.amazonaws.com',
	user = 'group9',
	port = '3306',
	database = 'group9_db',
	passwd = 'comp4442')

	# insert new database
	cur = mydb.cursor()
 
	print("successfully connect to the database")
	
	# return mydb

def tupleToJsonA(t):
	jsonList = []
	jsonList.append(t[0])
	jsonList.append(t[1][0])
	jsonList.append(t[1][1])
	jsonList.append(t[1][2])
	jsonList.append(t[1][3])
	jsonList.append(t[1][4])

	return jsonList

def driverList():
	driverList = []
	results = open("./result.txt", encoding='utf-8')
	with results as file:
		for line in file.readlines():
			line = line.strip('\n') 
			line = eval(line)
			jsonList = tupleToJsonA(line)
			driverList.append(jsonList[0])
	# print(driverList)
	return driverList

@application.route('/')
@cross_origin()
def home():
	return render_template('home.html')

@application.route('/behavior',methods = ['POST', 'GET'])
@cross_origin()
def behavior():
	jsonListsA = []
	results = open("./result.txt", encoding='utf-8')
	with results as file:
		for line in file.readlines():
			line = line.strip('\n') 
			line = eval(line)
			jsonList = tupleToJsonA(line)
			jsonListsA.append(jsonList)

	print(jsonListsA)
	print(type(jsonListsA))

	return render_template("behavior.html", result=jsonListsA)

@application.route('/diagram',methods = ['POST', 'GET'])
@cross_origin()
def diagram():
	drivers = driverList()
	driver_data = []
	result_data = []
	if request.method == 'POST':
		driverId = json.loads(request.data)["driverId"]
		totalTime = json.loads(request.data)["totalTime"]
		print("Server: received request for records of driver", driverId, "within", totalTime, "seconds")
		with open('./resultB.txt', 'r') as all_data:
			driver_data = [line.strip() for line in all_data.readlines() if line.split(",")[0] == driverId]
			if driver_data == []:
				return jsonify("No data to display")
			else:	
				first_record = driver_data[0]
				first_time = datetime.strptime(first_record.split(",")[2], "%Y-%m-%d %H:%M:%S")
				for line in driver_data:
					time = datetime.strptime(line.split(",")[2], "%Y-%m-%d %H:%M:%S")
					if time - first_time <= timedelta(seconds=totalTime):
						result_data.append(line)
		
		print(result_data)
		return jsonify(result_data)

	return render_template("diagram.html", drivers = drivers)


if __name__ == '__main__':
	application.run(port=3000, debug=True)




