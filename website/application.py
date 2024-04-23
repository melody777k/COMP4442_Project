from flask import Flask, render_template, request
import mysql.connector
import json

application = Flask(__name__, static_url_path='/static')
#app = Flask(__name__)

@application.route('/')
def home():
	return render_template('home.html')

@application.route('/behavior',methods = ['POST', 'GET'])
def behavior():
	jsonLists = []
	results = open("../result.txt", encoding='utf-8')
	with results as f:
		for line in f.readlines():
			line = line.strip('\n') 
			line = eval(line)
			jsonList = tupleToJson(line)
			jsonLists.append(jsonList)

	# print(jsonLists)
	# print(type(jsonLists))

	return render_template("behavior.html", result=jsonLists)

def tupleToJson(t):
	jsonList = []
	jsonList.append(t[0])
	jsonList.append(t[1][0])
	jsonList.append(t[1][1])
	jsonList.append(t[1][2])
	jsonList.append(t[1][3])
	jsonList.append(t[1][4])

	return jsonList

# def db_connection():
# 	mydb = mysql.connector.connect( host = 'database-1.cti2wk8aib5l.us-east-1.rds.amazonaws.com',
# 	user = 'admin',
# 	port = '3306',
# 	database = 'lab4',
# 	passwd = '12345678')

# 	print("successfully connect to the database")
	
# 	return mydb

@application.route('/diagram')
def diagram():
	# mydb = db_connection()

	# cur = mydb.cursor()
	# cur.execute("select * from Students")

	# myresult = cur.fetchall()
	# for result in myresult:
	# 	print(result)

	return render_template("diagram.html")

if __name__ == '__main__':
	application.run(port=5000, debug=True)




