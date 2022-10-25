days_of_week = [
  'Sunday',
  'Monday',
  'Tuesday',
  'Wednesday',
  'Thursday',
  'Friday',
  'Saturday'
]

def add_time(start, duration, *args):

  [h, T] = start.split(" ")
  [sh, sm] = h.split(":")
  [dh, dm] = duration.split(":")
  

  total_minutos = int(sm) + int(dm)
  total_horas = int(sh) + int(dh)
  future_days = 0
  
  if total_minutos >= 60:
    total_minutos -= 60
    total_horas += 1
  if total_minutos < 10:
      total_minutos = f"{total_minutos}".zfill(2)

      
  if total_horas >= 12:
    t, r = divmod(total_horas, 12)
    total_horas = r if r else total_horas
    if total_horas > 12:
      total_horas = total_horas - ((t-1) * 12)

    if t > 0:
      if T == "PM":
        future_days = ((t-1) // 2) + 1
      else:
        future_days = t // 2

    if t > 0 and t %  2 != 0:
      T = "AM" if T == "PM" else "PM"
  

  new_time = str(total_horas) + ":"
  new_time += str(total_minutos) + f" {T}"

  if args:
    day = args[0].title()
    if future_days > 0:
      index = days_of_week.index(day)
      index += future_days % 7
      if index > 6:
        index = index - 7
      day = days_of_week[index]
    
      
    new_time += f", {day}"

  if future_days == 1:
    new_time += f" (next day)"
  elif future_days > 1:
    new_time += f" ({future_days} days later)"


  return new_time
