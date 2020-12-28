import requests 

url = "http://10.10.204.95:8000/api/"

for i in range(1,100, 2):
    r = requests.get(url + str(i))
    print(r.text)