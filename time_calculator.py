# link to replit code: https://replit.com/@MauricioFiorent/boilerplate-time-calculator#time_calculator.py

def add_time(start, duration, day=None):

    weekdays = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")

    if day != None:
        weekday_index = weekdays.index(day.lower())
        weekday = (weekdays[weekday_index]).capitalize()

    colen_index_start = start.find(":")
    colen_index_duration = duration.find(":")

    start_hour = int(start[0:colen_index_start])
    duration_hour = int(duration[0:colen_index_duration])

    start_minutes = int(start[colen_index_start+1:colen_index_start+3])
    duration_minutes = int(duration[colen_index_duration+1:colen_index_duration+3])

    if start_minutes + duration_minutes < 60:
        if start_minutes + duration_minutes < 10:
            resultant_minutes = "0" + str(start_minutes + duration_minutes)
        else:
            resultant_minutes = start_minutes + duration_minutes
        resultant_hour = start_hour + duration_hour
    else:
        if start_minutes + duration_minutes - 60 < 10:
            resultant_minutes = "0" + str(start_minutes + duration_minutes - 60)
            resultant_hour = start_hour + duration_hour + 1
        else:
            resultant_minutes = start_minutes + duration_minutes - 60
            resultant_hour = start_hour + duration_hour + 1

    hours_left = (duration_hour+duration_minutes/60)-(12 - (start_hour+start_minutes/60))

    if resultant_hour >= 12:
        AM_PM_flip_count = 1 + int(hours_left/12)
    else:
        AM_PM_flip_count = 0

    if start[colen_index_start+4:colen_index_start+6] == "AM":
        if AM_PM_flip_count % 2 == 0:
            AM_PM_FINAL = "AM"
        else:
            AM_PM_FINAL = "PM"
    else:
        if AM_PM_flip_count % 2 == 0:
            AM_PM_FINAL = "PM"
        else:
            AM_PM_FINAL = "AM"

    if start[colen_index_start+4:colen_index_start+6] == "PM":
        if hours_left >=0 and hours_left < 12:
            extra_days = 1
        elif hours_left >= 12:
            extra_days = 1 + int(hours_left/24)
        elif hours_left < 0:
            extra_days = 0

    else:
        if hours_left-12 >=0 and hours_left-12 < 24:
            extra_days = 1
        elif hours_left >= 24:
            extra_days = 1 + int(hours_left/24)
        else:
            extra_days = 0

    if resultant_hour % 12 == 0:
        print_hour = 12
    else:
        print_hour = resultant_hour % 12

    if day == None:
        if extra_days == 0:
            return (str(print_hour) + ":" + str(resultant_minutes) + " " + str(AM_PM_FINAL))
        if extra_days == 1:
            return (str(print_hour) + ":" + str(resultant_minutes) + " " + str(AM_PM_FINAL) + " (next day)")
        if extra_days > 1:
            return (str(print_hour) + ":" + str(resultant_minutes) + " " + str(AM_PM_FINAL) + " (" + str(extra_days) + " days later)")

    if day != None:
        new_weekday = weekdays[(extra_days+weekday_index)%7].capitalize()
        if extra_days == 0:
            return (str(print_hour) + ":" + str(resultant_minutes) + " " + str(AM_PM_FINAL) + ", " + str(weekday))
        if extra_days == 1:
            return (str(print_hour) + ":" + str(resultant_minutes) + " " + str(AM_PM_FINAL) + ", " + str(new_weekday) + " (next day)")
        if extra_days > 1:
            return (str(print_hour) + ":" + str(resultant_minutes) + " " + str(AM_PM_FINAL) + ", " + str(new_weekday) + " (" + str(extra_days) + " days later)")
