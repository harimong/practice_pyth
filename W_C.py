


import requests #실시간 데이터 받아오기
import json #for API 

r=requests.get("https://api.openweathermap.org/data/2.5/weather?q=Seoul,kr&appid=84c84b95b8315afa208b27b48ca91f55")

r=json.loads(r.content.decode('utf-8').replace("'",'"')) #convert JSON to python

print(r['weather'][0]['main']) # 날씨가 뜬다. ex) haze
print(r['weather'][0]['id']) # 날씨 id가 뜬다. ex) 721

wid = r['weather'][0]['id']

if wid//100 == 8:
    if wid/100 > 8:
        GPIO.output(23, True)
    else:
        GPIO.output(24, True)
elif wid//100 == 7:
    GPIO.output(25, True)
else:
    GPIO.output(23, True)
    GPIO.output(24, True)



