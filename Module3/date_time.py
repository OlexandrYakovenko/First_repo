import datetime  as dt
from datetime import datetime as dtdt
#basics
# print("\nDate and time now")
# x = dtdt.now()
# print(x)

# print("Another day")
# x = dtdt(2020, 5, 17,14,32,12)
# print(x)

# print("One field")
# x = dtdt.now()
# print(type(x))
# year = type(x.strftime("%Y"))
# print("year:", year)
# month = x.strftime("%m")
# print("month:", month)
# day = x.strftime("%d")
# print("day:", day)
# time = x.strftime("%H:%M:%S")
# print("time:", time)
# date_time = x.strftime("%m/%d/%Y, %H:%M:%S")
# print("date and time:",date_time)
# # https://www.w3schools.com/python/python_datetime.asp

# print("\nConverting a String to a datetime object:" )
# datetime_str = '10/19/22 13:55:26'
# datetime_object = dtdt.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
# print(type(datetime_object))
# print(datetime_object)  # printed in default format

# print("\nConverting String to datetime.date() object")
# date_str = '10/19/22 13:55:26'
# date_object = dtdt.strptime(date_str, '%m/%d/%y %H:%M:%S').date()
# print(type(date_object))
# print(date_object)  # printed in default format

# print("\nConverting String to datetime.time() object")
# time_str = '13::55::26'
# time_object = dtdt.strptime(time_str, '%H::%M::%S').time()
# print(type(time_object))
# print(time_object)

# print( "\nFormatting output another way:")
# print( " -Local to ISO 8601:")
# print(dtdt.now().isoformat())
# print( " -UTC to ISO 8601:") 
# print(dtdt.utcnow().isoformat())#DEPRECATED
# print(dtdt.now(dt.UTC))
# print( " -Local to ISO 8601 without microsecond:")
# print(dtdt.now().replace(microsecond=0).isoformat())
# print( " -UTC to ISO 8601 with TimeZone information (Python 3):")
# print(dtdt.now(tz=dt.timezone.utc).isoformat())
# print( " -UTC to ISO 8601 with Local TimeZone information without microsecond (Python 3):")
# print(dtdt.now().astimezone().replace(microsecond=0).isoformat())
# print( " -Local to ISO 8601 with TimeZone information (Python 3):")
# print(dtdt.now().astimezone().isoformat())
