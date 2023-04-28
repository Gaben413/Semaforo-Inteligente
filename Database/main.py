import mysql.connector
from datetime import datetime
from datetime import timedelta
import dotenv
import os

from random import randrange #Only to insert dummy data-

dotenv.load_dotenv(dotenv.find_dotenv())
#Connect to the database
mydb = mysql.connector.connect(
    host=os.getenv('hostString'),
    user=os.getenv('userString'),
    password=os.getenv('passwordString'),
    database=os.getenv('databaseString')
)

mycursor = mydb.cursor()

data = {"counter": 7, "date_time": datetime.now()}

def INSERT_DATA(camera_ID, input_data):
    sql = "INSERT INTO Dados (Contador, Data_Tempo, Camera_ID) VALUES (%s, %s, %s)"
    data = (input_data['counter'], input_data['date_time'], camera_ID)
    mycursor.execute(sql, data)
    mydb.commit()
    print(mycursor.rowcount, "record inserted")


#INSERT_DATA(1, data)

#The time tange will be inserted as seconds at a minimum
#Example:
#FetchData(datetime.datime('2023-04-28 07:00:00'), (60*30)) 
#It will check time from 28/04/2023 07:00:00 to 28/04/2023 07:30:00
#The (60*30) will add 30 minutes. It takes a input of seconds (60 seconds is a minute)
#and then multiply by 30, making it 30 minutes
def FetchData(dataTime, timeRange, camera_id):
    #SELECT * FROM Dados WHERE (Data_Tempo BETWEEN '2010-01-30 14:15:55' AND '2010-09-29 10:15:55');
    query = "SELECT Contador FROM Dados WHERE (Data_Tempo BETWEEN %s AND %s AND Camera_ID = %s);"
    times = [dataTime, (dataTime+timedelta(0, timeRange))]
    adr = (times[0], times[1], camera_id)

    mycursor.execute(query, adr)
    results = mycursor.fetchall()
    
    total = 0

    for i in results:
        total += int(''.join(map(str, i)))
        #print(type(int(''.join(map(str, i)))))
        #print(i)

    print(f'Total of cars that have passed: {total}')

    print(f'Cars detected by camera {camera_id} that passed by between {times[0]} and {times[1]}')
    return total

    
#FetchData(datetime.fromisoformat('2023-04-28 07:00:00'), (60*30), 3)

def CompareData(camera_select_1, camera_select_2, startTime, interval):
    data_cam_1 = FetchData(startTime, interval, camera_select_1)
    data_cam_2 = FetchData(startTime, interval, camera_select_2)

    print(f'Cam 1: {data_cam_1}\nCam 2: {data_cam_2}')

    if data_cam_1 > data_cam_2:
        print('Camera 1 tem mais carros passando, entao deve ter prioridade')
    elif data_cam_1 < data_cam_2:
        print('Camera 2 tem mais carros passando, entao deve ter prioridade')
    elif data_cam_1 == data_cam_2:
        print('Ambas cameras tem a mesma quantidade de carros passando')

#CompareData(2, 3, datetime.fromisoformat('2023-04-28 07:00:00'), (60*30))

def InsertDummyData():
    for i in range(100):
        sql = 'INSERT INTO Dados (Contador, Data_Tempo, Camera_ID) VALUES (%s, %s, %s)'
        val = (randrange(50), datetime.fromisoformat('2023-04-28 07:00:00')+timedelta(0, randrange(60*60)), 3)
        mycursor.execute(sql, val)
    mydb.commit()

    print(mycursor.rowcount, "record inserted")

#print(randrange(60*60))
#InsertDummyData()
'''
mydb.commit()

print(mycursor.rowcount, "record inserted")
'''