import amino
import os
import json
import threading
import requests
import wget
import heroku3
key="7ad5b9cf-7c8c-4ff5-a016-6186e636d3b7"
nickname="light"
app_name="accj567890"
url="https://save.thehybridklaus.repl.co"
password="Charlie123"
def restart():
    heroku_conn = heroku3.from_key(key)
    botapp= heroku_conn.apps()[app_name]
    botapp.restart()
def send(data):
    requests.post(f"{url}/save",data=data)
client=amino.Client("172D5D674D519B32F403299B33C377F402D1F5FAB1879EFC286A40C97BAD437D200A7BB8C2BD6BC27D")

def codee(link):
	d={"data":link}
	p=requests.post("http://192.46.210.24:5000/captcha",data=d)
	return p.json()["dick"]

#password=custompwd

for i in range(3):
  dev=client.devicee()
  #dev=client.device_id
  email=client.gen_email()
  print(email)
  client.request_verify_code(email = email,dev=dev)
  link=client.get_message(email)
  try: code=codee(link)
  except: pass
  
  
  try:
    client.register(email = email,password = password,nickname =nickname, verificationCode = code,deviceId=dev)
    #sub.send_message(chatId=chatId,message="Criada")
    d={}
    d["email"]=str(email)
    d["password"]=str(password)
    d["device"]=str(dev)
    t=json.dumps(d)
    data={"data":t}
    send(data)
  except Exception as l:
    print(l)
    pass


restart()
