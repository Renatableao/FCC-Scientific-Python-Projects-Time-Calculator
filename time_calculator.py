def add_time(start, duration, weekday=""):
  new_time = ""
  weekday_list = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]


  # get time and AM-PM
  start_list = start.split(" ")
  # calculate duration in minutes
  duration_list = duration.split(":")
  duration_min = (int(duration_list[0]) * 60) + int(duration_list[1])

  # calculate start in minutes
  hour_min = start_list[0].split(":")
  minutes = (int(hour_min[0]) * 60) + int(hour_min[1])

  # get total in minutes
  total = minutes + duration_min

  # calculate number of days and total minutes after 24h
  days_passed = int(total / 1440)

  min_after = total - (days_passed * 1440)

  # get final hour
  hour_result = str(int(min_after/60))
  min_result = str("{:02d}".format(total%60))
  
  if start_list[1] =='AM':
    
    if total < 720:

      if weekday != "": 
        weekday = ", " + (weekday.lower()).capitalize()
        
      new_time =  hour_result + ':' + min_result + " AM" + weekday

    if total >= 720 and total < 1440:

      if weekday != "": 
        weekday = ", " + (weekday.lower()).capitalize()
        
      new_time = str((int(hour_result) - 12)) + ':' + min_result  + " PM" + weekday

    if total >= 1440 and total < 2880:
  
      total = min_after
     
      days_text = " (next day)"

      if weekday != "": 
        weekday = ", " +  (weekday_list[ (weekday_list.index(weekday.lower()) + 1)  % 7]).capitalize()

      if total < 720:
        
        new_time = hour_result + ':' + min_result + " AM" + weekday + days_text

      if total >= 720 and total < 1440:
        new_time = str((int(hour_result) - 12)) + ':' + min_result + " PM" + weekday + days_text
      
    if total >= 2880:

      total = min_after
      days_text =  " (" + str(days_passed) + " days later)"

      if total < 720:

        if weekday != "": 
          weekday = ", " +  (weekday_list[ (weekday_list.index(weekday.lower()) + days_passed)  % 7]).capitalize()
        
        new_time = hour_result + ':' + min_result + " AM" + weekday + days_text

      if total >= 720 and total < 1440:

        if weekday != "": 
          weekday = ", " +  (weekday_list[ (weekday_list.index(weekday.lower()) + days_passed)  % 7]).capitalize()
        
        new_time = str((int(hour_result) - 12)) + ':' + min_result + " PM" + week_result + days_text

      
  if start_list[1] =='PM':
    
    if total < 720:
      
      if weekday != "": 
        weekday = ", " + (weekday.lower()).capitalize()
        
      new_time = hour_result + ':' + min_result + " PM" + weekday

    if total >= 720 and total < 1440: 

      if weekday != "": 
        weekday = ", " +  (weekday_list[ (weekday_list.index(weekday.lower()) + 1)  % 7]).capitalize()
        
      new_time = str((int(hour_result) - 12)) + ':' + min_result + " AM" + weekday  + " (next day)"

    if total >= 1440 and total < 2880:

      total = min_after

      if total < 720:
        
        if weekday != "": 
          weekday = ", " + (weekday_list[ (weekday_list.index(weekday.lower()) + 1)  % 7]).capitalize()
        
        new_time = hour_result + ':' + min_result + " PM" +  weekday + " (next day)"

      if total >= 720 and total < 1440:
        
        if weekday != "": 
          weekday = ", " +  (weekday_list[ (weekday_list.index(weekday.lower()) + days_passed + 1)  % 7]).capitalize()
        
        new_time = str((int(hour_result) - 12)) + ':' + min_result + " AM" +  weekday + " (" + str(days_passed + 1) + " days later)"

    if total >= 2880:

      total = min_after
      
     

      if total < 720:

        if weekday != "": 
          weekday = ", " +  (weekday_list[ (weekday_list.index(weekday.lower()) + days_passed)  % 7]).capitalize()
        
        new_time = hour_result + ':' + min_result + " PM" +  weekday + " (" + str(days_passed) + " days later)"

      if total >= 720 and total < 1440:

        if weekday != "": 
          weekday = ", " +  (weekday_list[ (weekday_list.index(weekday.lower()) + days_passed + 1)  % 7]).capitalize()
        
        new_time = str((int(hour_result) - 12)) + ':' + min_result + " AM" +  weekday + " (" + str(days_passed + 1) + " days later)"


  return new_time.replace("0:", "12:")