import mysql.connector

user="root"
password=""
database="peoples_voice_new"
port=3306
def select(q):
	con=mysql.connector.connect(user=user,password=password,host="localhost",database=database,port=port)
	cur=con.cursor(dictionary=True)
	cur.execute(q)
	result=cur.fetchall()			
	cur.close()
	con.close()
	return result

def insert(q):
	con=mysql.connector.connect(user=user,password=password,host="localhost",database=database,port=port)
	cur=con.cursor(dictionary=True)
	cur.execute(q)
	con.commit()
	result=cur.lastrowid
	cur.close()
	con.close()
	return result

def update(q):
	con=mysql.connector.connect(user=user,password=password,host="localhost",database=database,port=port)
	cur=con.cursor(dictionary=True)
	cur.execute(q)
	con.commit()
	result=cur.rowcount
	cur.close()
	con.close()

def delete(q):
	con=mysql.connector.connect(user=user,password=password,host="localhost",database=database,port=port)
	cur=con.cursor(dictionary=True)
	cur.execute(q)
	con.commit()
	result=cur.rowcount
	cur.close()
	con.close()