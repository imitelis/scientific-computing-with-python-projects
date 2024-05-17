def add_time(start, end, day= None):
  new_time = ''
  start_splt = start.split(' ')
  start_time = start_splt[0].split(':')
  start_hour = int(start_time[0])
  start_minute = int(start_time[1])
  start_jour = start_splt[1]
  end_splt = end.split(' ')
  end_time = end_splt[0].split(':')
  end_hour = int(end_time[0])
  end_minute = int(end_time[1])

  if start_jour == 'PM':
    start_hour = int(start_hour + 12)
  else:
    start_hour = int(start_hour)
  
  start_minutes = int(start_minute + (60 * start_hour))
  end_minutes = int(end_minute + (60 * end_hour))
  total_minutes = int(start_minutes + end_minutes)
  added_minutes = total_minutes % 60
  added_hours = int(total_minutes / 60)
  number_of_days = int(added_hours / 24)
  number_of_hours = added_hours % 24  

  if len(str(added_minutes)) == 2:
    new_time = str(added_minutes)
  elif len(str(added_minutes)) == 1:
    new_time = "0" + str(added_minutes)

  new_hour = number_of_hours % 12
  if int(number_of_hours / 12) == 0:
    new_jour = 'AM'
    if new_hour == 0:
      new_hour = '12'
  else:
    new_jour = 'PM'
    if new_hour == 0:
      new_hour = '12'
  
  new_time = str(new_hour) + ':' + new_time + ' ' + new_jour

  if not day == None:
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    ite = 0

    while True:
      if day.lower() == days[ite].lower():
        break
      ite = ite + 1
    newday = days[((ite + (number_of_days % 7)) % 7)]
    new_time = new_time + ', ' + newday


  if number_of_days == 1:
    new_time = new_time + ' (next day)'
  elif number_of_days > 1:
    new_time = new_time + ' (' + str(number_of_days) + ' days later)'
  return new_time