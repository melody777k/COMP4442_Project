from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime, timedelta

application = Flask(__name__, static_url_path='/static')
#app = Flask(__name__)

def db_connection():
	# mydb = mysql.connector.connect( host = 'database-2.c9gkgua66wjp.us-east-1.rds.amazonaws.com',
	# user = 'group9',
	# port = '3306',
	# database = 'group9_db',
	# passwd = 'comp4442')

	# insert new database
	# cur = mydb.cursor()
	# cur.execute("select * from Students")
 
	print("successfully connect to the database")
	
	# return mydb

def tupleToJson(t):
	jsonList = []
	jsonList.append(t[0])
	jsonList.append(t[1][0])
	jsonList.append(t[1][1])
	jsonList.append(t[1][2])
	jsonList.append(t[1][3])
	jsonList.append(t[1][4])

	return jsonList

@application.route('/')
def home():
	return render_template('home.html')

@application.route('/behavior',methods = ['POST', 'GET'])
def behavior():
	jsonLists = []
	results = open("../result.txt", encoding='utf-8')
	with results as file:
		for line in file.readlines():
			line = line.strip('\n') 
			line = eval(line)
			jsonList = tupleToJson(line)
			jsonLists.append(jsonList)

	# print(jsonLists)
	# print(type(jsonLists))

	return render_template("behavior.html", result=jsonLists)

@application.route('/diagram/<driver_id>/<int:total_time>')
def diagram(driver_id, total_time):
	print("##############")
	print("Server: received request for records of driver", driver_id, "within", total_time, "seconds")
	print("##############")
	driver_data = []
	result_data = []
	with open('../b.txt', 'r') as all_data:
		driver_data = [line.strip() for line in all_data.readlines() if line.split(",")[0] == driver_id]
		first_record = driver_data[0]
		first_time = datetime.strptime(first_record.split(",")[2], "%Y-%m-%d %H:%M:%S")
		for line in driver_data:
			time = datetime.strptime(line.split(",")[2], "%Y-%m-%d %H:%M:%S")
			if time - first_time <= timedelta(seconds=total_time):
				result_data.append(line)
	return jsonify(result_data)


if __name__ == '__main__':
	application.run(port=3000, debug=True)




