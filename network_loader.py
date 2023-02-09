import time
import requests
i = 0
while True:
    response = requests.get('http://localhost:5000/')
    #print(response.text)
    i += 1
    if i%10==0:
        print(i)
    time.sleep(4)