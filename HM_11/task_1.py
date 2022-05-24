import requests , json
r = requests.get("https://www.mobile.bg/pcgi/mobile.cgi")

with open('mobile.txt', 'w', encoding='utf-8') as json_file:
    mobile = json.dump(dict(r.headers), json_file)

mobile_data = open('mobile.txt', encoding='utf-8')

details = json.load(mobile_data)

print(details["Date"]),
print(details["Content-Type"])
print(details["Connection"])
