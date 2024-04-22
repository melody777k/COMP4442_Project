from flask import Flask, render_template, request
import mysql.connector

application = Flask(__name__, static_url_path='/static')
#app = Flask(__name__)

@application.route('/')
def home():
	return render_template('home.html')

@application.route('/summary',methods = ['POST', 'GET'])
def summary():
	# if request.method == 'POST':
	# 	Name = request.form['Name']
	# 	ID = request.form['ID']
	# 	Department = request.form['Department']
	# 	Email = request.form['Email']

	# 	mydb = db_connection()
	# 	cur = mydb.cursor()
	# 	info = "insert into Students values('{}','{}','{}','{}')".format(Name, ID, Department, Email)
	# 	cur.execute(info)

	# 	mydb.commit()
	# 	msg = "Record successfully added"

	# 	mydb.close()
		return render_template("summary.html")

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
	application.run(port=5000, debug = True)




