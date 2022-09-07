# import re
import json
# import urllib.request as urllib2
from urllib.request import urlopen
import haversine as hs
from haversine import Unit
import datetime
# from apscheduler.schedulers.background import BackgroundScheduler as scheduler

def myfn():
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data = json.load(response)
    get_details(data)
    return data


def distance_calc(data,data1):
    # data=lst[-1]
    # data1=lst[len(lst)-2]
    # data  = json.load(last)
    loc1=data['co-ordinates']
    loc1=loc1.split(",")
    loc1 = (float(loc1[0]),float(loc1[1]))
    print(loc1)
    # loc1=list(map(float, loc1))
    # loc1=(loc1.split(","))
    # last_before=lst[len(lst)-1]
    # data1  = json.load(last_before)
    loc2=data1['co-ordinates']
    loc2=loc2.split(",")
    loc2 = (float(loc2[0]),float(loc2[1]))
    print(loc2)
    # loc2=loc1.split(",")
    # loc2=list(map(float, loc2))
    
    # loc2=(loc2.split(","))
    distance = hs.haversine(loc1,loc2)
    m_distance = hs.haversine(loc1,loc2,unit=Unit.METERS)
    miles = hs.haversine(loc1,loc2,unit=Unit.MILES)
    print(distance)

def get_details(data):
    ip=data['ip']
    org=data['org']
    city = data['city']
    country=data['country']
    region=data['region']
    loc=data['loc']
    new_data={"ip": ip,
              "city":city,
              "country":country,
              "region":region,
              "co-ordinates":loc
              }
    with open("datas.json",'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
      
        system_time = datetime.datetime.now()
        time=system_time.strftime("%H:%M:%S")
        new_data.update({"Time": time})
        # Join new_data with file_data inside emp_details
        file_data["emp_details"].append(new_data)
    
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

    # with open('datas.json') as f:
    #     datas = json.load(f)
    #     #   lst = datas.split()
    #     lst = datas["emp_details"]
    # data=lst[len(lst)-1]
    # data1=lst[len(lst)-2]

    # print(lst[1])
    # distance_calc(data,data1)
    # return(lst)

myfn()
# sch = scheduler()
# sch.add_job(myfn, 'interval', seconds=5)
# sch.start()
# lst[len(lst)-1],lst[len(lst)-2]

