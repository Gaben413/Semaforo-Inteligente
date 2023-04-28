from database import FetchData, Insert_Data
from datetime import datetime

data = {"counter": 99, "date_time": datetime.now()}

Insert_Data(1, data)

data = {"counter": 7, "date_time": datetime.now()}
#print(FetchData(datetime.fromisoformat('2023-04-28 07:00:00'), (60*30), 3))