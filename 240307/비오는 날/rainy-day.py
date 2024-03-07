class Forecast:
  def __init__(self, date, day, weather) :
    self.date = date
    self.day = day
    self.weather = weather

n = int(input())
weather_list = []
rain_list = []

answer = Forecast('2100-99-99','','')
for i in range(n):
  date, day, weather = tuple(input().split())
  weather_list.append(Forecast(date,day, weather))

  if weather_list[i].weather == 'Rain':
    if answer.date >= weather_list[i].date:
      answer = Forecast(date,day,weather)

print(answer.date, answer.day, answer.weather)