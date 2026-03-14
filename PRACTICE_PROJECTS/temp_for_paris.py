import requests
import pandas as pd
from datetime import datetime, timedelta
today = datetime.now()
end_date = today

# to get the one week earlier date and time 
start_date = today - timedelta(days=7)

# api would expect the date format (YYY-MM-DD)

start_date = start_date.strftime("%Y-%m-%d")
end_date = end_date.strftime("%Y-%m-%d")

# we would use the api 

api_url = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(api_url) # response 200 = ok, connection successfull

# now we would get data in the form of the json

data = response.json()



daily_data = data["daily"]
print(daily_data)

# now i am going to format the data in the daily_data

formated_data = pd.DataFrame(
    {
        "Date" : daily_data["time"],
        "Min_Temperature" : daily_data["temperature_2m_min"],
        "Max_Temperature" : daily_data["temperature_2m_max"]
    }
)

print(formated_data)
