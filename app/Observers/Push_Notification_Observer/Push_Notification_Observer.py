from app.Observers.Observer import observer
import requests
from exponent_server_sdk import (
    DeviceNotRegisteredError,
    PushClient,
    PushMessage,
    PushServerError,
    PushTicketError,
)
from requests.exceptions import ConnectionError, HTTPError
import firebase_admin
from firebase_admin import credentials
import os
from firebase_admin import db

class Push_Notification_Observer(observer):
    
    def __init__(self):
        pass
    
    def update(self,dictionary):
        print("OK I AM READY TO SEND")
        try:
            dirname = os.path.dirname(__file__)
            filename = os.path.join(dirname, 'firekey.json')
            
            cred = credentials.Certificate(filename)
            if not firebase_admin._apps:
                firebase_admin.initialize_app(cred,{
                    'databaseURL' : 'https://greenbay-app-default-rtdb.firebaseio.com/'
                })

            result=db.reference('Users/').get()
            print(result.keys())

            for token in result.keys():
                try:
                    pushid="ExponentPushToken["+token+"]"
                    response=requests.post(
                        url="https://exp.host/--/api/v2/push/send",
                        data = {"to":pushid,"title":dictionary['Title'],"body":dictionary['Description']}
                    )
                    print(response)
                except:
                    continue

            
        
        except Exception as ex:
            print(ex)
        