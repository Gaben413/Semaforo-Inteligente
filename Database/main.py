import mysql.connector
from datetime import datetime
import dotenv
import os

dotenv.load_dotenv(dotenv.find_dotenv())
#Connect to the database
mydb = mysql.connector.connect(
    host=os.getenv('hostString'),
    user=os.getenv('userString'),
    password=os.getenv('passwordString'),
    database=os.getenv('databaseString')
)

mycursor = mydb.cursor()

'''
#Dictionary example
dct = [
    {"Name": 'Gary', "Age": 10},
    {"Name": 'Tommy', "Age": 25},
    {"Name": 'Tony', "Age": 45},
    {"Name": 'Tery', "Age": 15},
    {"Name": 'Kory', "Age": 14},
    {"Name": 'Tory', "Age": 35},
    {"Name": 'Bubba', "Age": 75},
    {"Name": 'Ben', "Age": 45},
]

#Insert example
sql = "INSERT INTO test (testName, testAge) VALUES (%s, %s)"
val = []
for row in dct:
    val.append((
        row['Name'],
        row['Age']
    ))

mycursor.executemany(sql,val)
'''

data = {"counter": 7, "date_time": datetime.now()}

def INSERT_DATA(camera_ID, input_data):
    sql1 = "INSERT INTO Dados (Contador, Data_Tempo) VALUES (%s, %s)"
    data1 = (input_data['counter'], input_data['date_time'])
    mycursor.execute(sql1, data1)

    sql_check = "SELECT COUNT(*) FROM Dados"
    mycursor.execute(sql_check)

    counter = mycursor.fetchone()
    counterInt = int(counter[0])

    sql2 = "INSERT INTO possui VALUES (%s, %s)"
    data2 = (camera_ID, counterInt)
    mycursor.execute(sql2, data2)

INSERT_DATA(2, data)

mydb.commit()

print(mycursor.rowcount, "record inserted")