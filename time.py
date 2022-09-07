# import datetime
# import pytz
# from tzwhere import tzwhere

# tzwhere = tzwhere.tzwhere()
# timezone_str = tzwhere.tzNameAt(12.8819,80.0885) # Seville coordinates
# print(timezone_str)
# #> Europe/Madrid

# timezone = pytz.timezone(timezone_str)
# dt = datetime.datetime.now()
# print(timezone.utcoffset(dt))
# #> datetime.timedelta(0, 7200)



import datetime
system_time = datetime.datetime.now()

print(system_time.strftime("%H:%M:%S"))

from datetime import datetime
s1 = '10:33:26'
s2 = '11:15:49' # for example
FMT = '%H:%M:%S'
tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
print(tdelta.seconds/3600)