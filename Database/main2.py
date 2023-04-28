from main import FetchData, INSERT_DATA
from datetime import datetime

data = {"counter": 77, "date_time": datetime.now()}

INSERT_DATA(1, data)

data = {"counter": 7, "date_time": datetime.now()}
#print(FetchData(datetime.fromisoformat('2023-04-28 07:00:00'), (60*30), 3))