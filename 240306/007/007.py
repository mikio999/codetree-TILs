class Mission:
  def __init__(self, code, location, time):
    self.code = code
    self.location = location
    self.time = time

secret_code, meeting_location, appointment_time = tuple(input().split())
kwargs = (secret_code, meeting_location, int(appointment_time))

mission = Mission(*kwargs)
print('secret code :', mission.code)
print('meeting point :', mission.location)
print('time :', mission.time)