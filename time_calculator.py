def add_time(start, duration, weekday=None):

  #splitting strings 
  clock, time_switch = start.split()
  start_h, start_m = clock.split(":")
  dur_h, dur_m = duration.split(":")

  #explaining AM/PM
  if time_switch == 'PM':
    tot_start_h = 12 + int(start_h)
  else:
    tot_start_h = int(start_h)  

  #total minutes
  new_min = int(start_m) + int(dur_m)

  #total hours
  new_hr = int(tot_start_h) + int(dur_h)

  #minutes conversion
  if new_min > 60:
    new_min -= 60
    new_hr += 1
  else:
    new_min = new_min
    new_hr = new_hr      

  #hours conversion in days

  if new_hr >= 24:
    days = new_hr // 24
    new_hr = new_hr % 24  
    
  #am/pm condition - time switch
    if new_hr == 0:
      new_time_switch = 'AM' 
      new_hr = 12
    elif new_hr > 12:
      new_time_switch = 'PM'
      new_hr -=12
    else: 
      new_time_switch = 'AM'  
      new_hr = new_hr  

  else:
  
    days = 0

    if new_hr >= 12:
      new_time_switch = 'PM'
      new_hr -=12
      if new_hr == 0:
        new_hr = 12
    else:
      new_time_switch = 'AM'
      new_hr = new_hr    

  #days count

  if days == 0:
    screenday = ""
  elif days <= 1:
    screenday = '(next day)'
  else:
    screenday = '(' + str(days) + ' days later)'

  #week day in input 
  weekdays= ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thurstday', 'Friday', 'Saturday']

  #setting indexes for weekdays
  if weekday != None:
    if weekday.capitalize() in weekdays:
      first_idx = weekdays.index(weekday.capitalize())
      new_idx = first_idx + days

      if new_idx > 6: #more than weekdays list
        new_idx = ((new_idx + 1) % 7 ) - 1 #calculate index to be between 0 and 6
        new_day = weekdays[new_idx]
      else:
        new_day = weekdays[new_idx]
        
    #setting new_time

  if days == 0:
    if weekday != None:
      new_time = f"{new_hr}:{new_min:02} {new_time_switch}, {new_day}" #setting format for min 
    else:  
      new_time = f"{new_hr}:{new_min:02} {new_time_switch}"

  else:
    if weekday != None:
      new_time = f"{new_hr}:{new_min:02} {new_time_switch}, {new_day} {screenday}"
    else:
      new_time = f"{new_hr}:{new_min:02} {new_time_switch} {screenday}" 
      
  return new_time