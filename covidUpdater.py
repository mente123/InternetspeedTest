import requests
from win10toast import ToastNotfier
import time
import json

# usinf the api we can get a response of daily covid statud of patients 

def update():
    request = requests.get('https://coronavirus-19-api.harokuapp.com/all')
    data = request.json()  # the data will be converted in to json format
    text = f'Confirmed Cases: {data["cases"]} \n Deaths : {data["deaths"]} \nRecovered : {["recovered"]}'
    
    
    while True:
        toast = ToastNotfier() # this shows a notification in our computer for some period of time(declared)
        toast.show_toast("Covid-19 Update",text,duration=20) #the notification will be stayed for 20 seconds
        time.sleep(60) #the data will be notified within every  one minute
        
update() 

