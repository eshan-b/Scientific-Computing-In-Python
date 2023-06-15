def add_time(start,add,day=None):
  time, period = start.split() 
  hour, minutes = map(int,time.split(':')) 
  addH, addM = map(int,add.split(':'))
  midday = ('PM','AM') 
  new_day = '' 
  later = ''

  carry, minutes = divmod(minutes + addM,60) 
  hour += carry 
  cycles, hour = divmod(hour + addH,12) 

  period = abs(midday.index(period)-(cycles % 2)) 
  passed = (period + cycles) // 2  

  if hour == 0: 
    hour = 12

  if minutes < 10: 
    minutes = f'0{minutes}'

  if day:
      week = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')
      new_day = f', {week[(week.index(day.capitalize()) + passed) % 7]}' 

  if passed == 1:
      later = ' (next day)'
  elif passed != 0:
      later = f' ({passed} days later)'

  return f'{hour}:{minutes} {midday[period]}{new_day}{later}'