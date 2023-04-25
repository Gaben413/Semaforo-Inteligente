import mysql.connector

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


def INSERT_DATA():
    pass

mydb.commit()

print(mycursor.rowcount, "record inserted")