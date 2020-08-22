import pandas
from datetime import datetime, timedelta
from math import pi, cos
from matplotlib import pyplot

def temperature_forecast(common_min, common_max, coldest_day):
    day_1=datetime(2020, 1, 1) - timedelta(days=1) #weather for this year
    day_of_year=[]
    temperature=[] 
    amplitude = (common_max - common_min) / 2
    wavelength = 366 #days in 2020 (leap year)
    y_offset = common_max - amplitude
    x_offset = coldest_day
    for day in range(1, wavelength+1):
        day_of_year.append(day_1 + timedelta(days=day))
        daily_temp = y_offset + amplitude * -1 * cos(2*pi * 1/wavelength * day - 2*pi*x_offset/wavelength)
        daily_temp = round(daily_temp, 1)
        temperature.append(daily_temp)
    return [temperature, day_of_year]
   
def get_temperature(day, month, year):
    day_of_year = daily_weather[1].index(datetime(year, month, day))
    temperature = daily_weather[0][day_of_year]
    return temperature
  
daily_weather = temperature_forecast(6.4, 20.4, 13) 
pyplot.plot(daily_weather[1], daily_weather[0])

get_temperature(22, 8, 2020)
