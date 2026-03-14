import requests
import pandas as pd
import matplotlib.pyplot as plt
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

#create the plot
plt.figure(figsize = (10,6))
plt.plot(formated_data["Date"], formated_data["Min_Temperature"], marker ='o', label = "Min Temp")
plt.plot(formated_data["Date"], formated_data["Max_Temperature"], marker= 'o', label ="Max Temp")



# Add labels and title
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Paris Weather - Past 7 Days')
plt.legend()

# Rotate x-axis labels for readability
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('weather_chart.png')
plt.show()
