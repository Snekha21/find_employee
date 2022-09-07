from urllib.request import urlopen
import json 

url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)


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
        # Join new_data with file_data inside emp_details
        file_data["emp_details"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

    with open('datas.json') as f:
        datas = json.load(f)
        #   lst = datas.split()
        lst = datas["emp_details"]
    data=lst[len(lst)-1]
    data1=lst[len(lst)-2]

    print(lst[1])
    # distance_calc(data,data1)
    return(lst)

get_details(data)