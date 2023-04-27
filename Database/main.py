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
    sql = "INSERT INTO Dados (Contador, Data_Tempo, Camera_ID) VALUES (%s, %s, %s)"
    data = (input_data['counter'], input_data['date_time'], camera_ID)
    mycursor.execute(sql, data)

INSERT_DATA(1, data)

def FetchDate(dataTime, timeRange):
    #SELECT * FROM Dados WHERE (Data_Tempo BETWEEN '2010-01-30 14:15:55' AND '2010-09-29 10:15:55');
    pass

mydb.commit()

print(mycursor.rowcount, "record inserted")