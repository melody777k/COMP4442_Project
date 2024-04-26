from flask import Flask, render_template, request
import json
import mysql.connector

application = Flask(__name__, static_url_path='/static')
#app = Flask(__name__)

def db_connection():
	mydb = mysql.connector.connect( host = 'database-2.c9gkgua66wjp.us-east-1.rds.amazonaws.com',
	user = 'group9',
	port = '3306',
	database = 'group9_db',
	passwd = 'comp4442')

	# insert new database
	cur = mydb.cursor()
	# cur.execute("select * from Students")
 
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

# def tupleToJsonB(t):
# 	jsonListB = []

# 	return jsonListB

@application.route('/')
def home():
	return render_template('home.html')

@application.route('/behavior',methods = ['POST', 'GET'])
def behavior():
	jsonListsA = []
	results = open("../result.txt", encoding='utf-8')
	with results as file:
		for line in file.readlines():
			line = line.strip('\n') 
			line = eval(line)
			jsonList = tupleToJsonA(line)
			jsonListsA.append(jsonList)

	# print(jsonLists)
	# print(type(jsonLists))

	return render_template("behavior.html", result=jsonListsA)

@application.route('/diagram')
def diagram():
	# jsonListsB = []
	# results = open("../b.txt", encoding='utf-8')
	# with results as file:
	# 	for line in file.readlines():
	# 		line = line.strip('\n') 
	# 		line = line.split(",")
	# 		print(line)
	# 		jsonList = line
	# 		jsonListsB.append(jsonList)
	# mydb = db_connection()

	# cur = mydb.cursor()
	# cur.execute("select * from Students")

	# myresult = cur.fetchall()
	# for result in myresult:
	# 	print(result)

	return render_template("diagram.html")
	# return render_template("diagram.html", result = jsonListsB)

if __name__ == '__main__':
	application.run(port=3000, debug=True)




