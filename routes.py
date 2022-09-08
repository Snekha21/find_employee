from flask import Flask, request, url_for, redirect, render_template
from flask import *

from datetime import datetime
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# import pandas as pd
import json 
# from Flask import request
# # from json import jsonify
# from werkzeug.utils import secure_filename
app = Flask(__name__)
# import pathlib
import haversine as hs
from haversine import Unit

subject = "Daily Report"
body = "Greetings! Here is your employee report"
sender_email = "snekhasuresh2777@gmail.com"
receiver_email = "bluesmeter@gmail.com"
password = "mstwwvcpyyjzbzbv"
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email
message.attach(MIMEText(body, "plain"))
filename="track-a-thon.pdf"
with open(filename, "rb") as attachment:
             part = MIMEBase("application", "octet-stream")
             part.set_payload(attachment.read())
             encoders.encode_base64(part)
             part.add_header(
            "Content-Disposition",
             f"attachment; filename= {filename}",
             )
             message.attach(part)
             text = message.as_string()
             context = ssl.create_default_context()
             with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
            # msg = Message('Hello', sender = 'snekhasuresh2777@gmail.com', recipients = ['bluesmeter@gmail.com'])
            # msg.body = "Hello Flask message sent from Flask-Mail"
            # mail.send(msg)
                server.sendmail(sender_email, receiver_email, text)

@app.route("/home")
def home():
    with open('datas.json') as f:
        datas = json.load(f)
        #   lst = datas.split()
        lst = datas["emp_details"]
    # for i in range(0,len(lst)):
    #     data=lst[i]
    #     data1=lst[i+1]
        # data1=lst[-1]
        # data2=lst[len(lst)-2]
        # data3=lst[len(lst)-3]
        # data4=lst[len(lst)-4]
        # data5=lst[len(lst)-5]
        # data6=lst[len(lst)-6]
        data1=lst[0]
        data2=lst[1]
        data3=lst[2]
        data4=lst[3]
        data5=lst[4]
        data6=lst[5]
        # data  = json.load(last)
        loc1=data1['co-ordinates']
        loc1=loc1.split(",")
        loc1 = (float(loc1[0]),float(loc1[1]))
        # print(loc1)
        # loc1=list(map(float, loc1))
        # loc1=(loc1.split(","))
        # last_before=lst[len(lst)-1]
        # data1  = json.load(last_before)
        loc2=data2['co-ordinates']
        loc2=loc2.split(",")
        loc2 = (float(loc2[0]),float(loc2[1]))

        loc3=data3['co-ordinates']
        loc3=loc3.split(",")
        loc3 = (float(loc3[0]),float(loc3[1]))

        loc4=data4['co-ordinates']
        loc4=loc4.split(",")
        loc4 = (float(loc4[0]),float(loc4[1]))


        loc5=data5['co-ordinates']
        loc5=loc5.split(",")
        loc5 = (float(loc5[0]),float(loc5[1]))


        loc6=data6['co-ordinates']
        loc6=loc6.split(",")
        loc6 = (float(loc6[0]),float(loc6[1]))

        region1=data2['city']
        region2=data3['city']
        region3=data4['city']
        region4=data5['city']
        region5=data6['city']
        # print(loc2)
        # loc2=loc1.split(",")
        # loc2=list(map(float, loc2))
        
        # loc2=(loc2.split(","))
        dis1 = hs.haversine(loc1,loc2)
        dis2 = hs.haversine(loc2,loc3)
        dis3 = hs.haversine(loc3,loc4)
        dis4 = hs.haversine(loc4,loc5)
        dis5 = hs.haversine(loc5,loc6)
        
        s1=time1=data1['Time']
        s2=times1=time2=data2['Time']
        s3=times2= time3=data3['Time']
        s4=times3=time4=data4['Time']
        s5=times4=time5=data5['Time']
        s6=times5=data6['Time']
        FMT = '%H:%M:%S'
        td1 = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
        tim1=(td1.seconds/3600)
        td2 = datetime.strptime(s3, FMT) - datetime.strptime(s2, FMT)
        tim2=(td2.seconds/3600)
        td3 = datetime.strptime(s4, FMT) - datetime.strptime(s3, FMT)
        tim3=(td3.seconds/3600)
        td4 = datetime.strptime(s5, FMT) - datetime.strptime(s4, FMT)
        tim4=(td4.seconds/3600)
        td5 = datetime.strptime(s6, FMT) - datetime.strptime(s5, FMT)
        tim5=(td4.seconds/3600)
        total_dis= dis1+dis2+dis3+dis4+dis5
        total_dis= int(total_dis)
        total_time=tim1+tim2+tim3+tim4+tim5
        # m_distance = hs.haversine(loc1,loc2,unit=Unit.METERS)
        # miles = hs.haversine(loc1,loc2,unit=Unit.MILES)
    # print(distance)
    # return render_template("index.html", distance = distance , start=loc1, end=loc2, miles=miles,m_distance=m_distance,)
    return render_template("index.html", 
    region1 = region1, dis1=dis1,time1=time1,times1=times1,tim1=tim1,total_dis=total_dis,
    region2 = region2, dis2=dis2,time2=time2,times2=times2,tim2=tim2,total_time=total_time,
    region3 = region3, dis3=dis3,time3=time3,times3=times3,tim3=tim3,
    region4 = region4, dis4=dis4,time4=time4,times4=times4,tim4=tim4,
    region5 = region5, dis5=dis5,time5=time5,times5=times5,tim5=tim5)

@app.route("/")
def login():
     if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('login'))
    # show the form, it wasn't submitted
     return render_template('login.html')

@app.route("/map")
def map():
     if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('map'))
    # show the form, it wasn't submitted
     return render_template('map.html')

    
# @app.route("/json")
# def myfn():
#     url = 'http://ipinfo.io/json'
#     response = request(url).json()
#     # response = urlopen(url)
#     data = json.load(response)
#     # get_details(data)
#     return data

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)
