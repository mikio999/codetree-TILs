class Forecast:
  def __init__(self, day, date, weather) :
    self.day = day
    self.date = date
    self.weather = weather

n = int(input())
weather_list = []
for _ in range(n):
  date, day, weather = tuple(input().split())
  weather_list.append(Forecast(day, date, weather))

rain_list = []
for i in range(n):
  if weather_list[i].weather == 'Rain':
    rain_list.append(weather_list[i])

target = 0
for j in range(1,len(rain_list)):
  if int(rain_list[target].date[0:4]) > int(rain_list[j].date[0:4]) :
    target = j
  elif int(rain_list[target].date[0:4]) == int(rain_list[j].date[0:4]) :
    if int(rain_list[target].date[5:7]) == int(rain_list[j].date[5:7]) :
      if int(rain_list[target].date[8:10]) > int(rain_list[j].date[8:10]) :
        target = j
    elif int(rain_list[target].date[5:7]) > int(rain_list[j].date[5:7]) :
      target = j

print(rain_list[target].date, rain_list[target].day, rain_list[target].weather)