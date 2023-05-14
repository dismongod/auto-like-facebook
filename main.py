import requests
from os import system
import sys
import time
import os
from pystyle import Colorate, Colors


def printSlow(text):
    for char in text:
        print(char, end="")
        sys.stdout.flush()
        time.sleep(.1)

printSlow("Hypre Auto Like Year 2023 .....")


os.system("clear")

print(Colorate.Horizontal(Colors.rainbow, f"""


                                  __  __  __   __     __ __ __  __  __    
                          |__|\_/|__)|__)|_   |_  /\ /  |_ |__)/  \/  \|_/
                          |  | | |   | \ |__  |  /--\\__|__|__)\__/\__/| \
                                                

                                 Facebook Auto Like Year 2023 By ` HYPRE.EXE#9999



"""))
print()
print()

target = input(Colorate.Horizontal(Colors.rainbow, "ID POST: "))

def api():
	get = {"access_token": "....."} #โทเค่นเฟส
	res = requests.post("https://az-like.com/loginWithToken_v2",headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36","cookie": "_ga=GA1.2.1718715253.1676465505; _gid=GA1.2.269098419.1676465505; az_likecom_session=eyJpdiI6IitjZ2VNZTVuWUVBM3hLZDNib2xMVXc9PSIsInZhbHVlIjoiMzFBSzVrVUtUc3lkWnYzMjVXSllqUnU2cEFaR3B5ZHhJZm5OTHducmpHcXpOUUw5TE4vMmo5MXhyeFpSazY4U2FTTTFDWEo3NFRMWGp4eW5ZNjRocDRLRUFCbzRKcFcyUGEwbXBBdVkrSmp4K1d0ZURkSVRqcS9QQWVnMk5Pem8iLCJtYWMiOiI4ZjY5ZTA5NTg4NzIwNTRlMDlkZjhkZjZhOGRmNTcyNTZmODJiNWFjOGU3ZWZkODVlZTBmODM1NGQ0ZGU5MzEyIn0%3D"},json=get)
	if res.status_code == 200:
		cookies = res.headers['set-cookie']
		req = requests.post("https://az-like.com/likes",headers={'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36","cookie": f"_ga=GA1.2.1718715253.1676465505; _gid=GA1.2.269098419.1676465505; {cookies}"},json={"fbid":f"{target}","type":"1"})
		if req.status_code == 200:
			total = req.json()['success']
			print(Colorate.Horizontal(Colors.rainbow, f"ส่งไลค์ {total} สำเร็จ !"))
		else:
			print(req.json())
	else:
			print(res.json())
			
			
api()
