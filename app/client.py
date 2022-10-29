import time

import requests

# response = requests.get("http://127.0.0.1:5000/test?param=value", json= {"key": "value"}, headers={"token": "aaa"})

# response = requests.post("http://127.0.0.1:5000/advs/", json={"title": "test_title 55555 ", "desc": "description", "owner":"user1"},
#                       headers={"token": "aaa"})

# response = requests.patch("http://127.0.0.1:5000/advs/2", json={"title": "edit_title 55555", "desc": "edit description", "owner":"user1"},
#                         headers={"token": "aaa"})

#double trouble
# response = requests.post("http://127.0.0.1:5000/advs/",
#                          json={"title": "test_title",  "owner": "user1"},
#                          headers={"token": "aaa"})

# response = requests.get("http://127.0.0.1:5000/advs/2")

#response = requests.delete("http://127.0.0.1:5000/advs/3")

response = requests.post("http://127.0.0.1:5000/mass_mail/",
                         json={"sender": "mass_sender@aa.aa",  "msg": "Mass message",},)

print(response.status_code)
print(response.text)
#print(response.json())

first_id = response.json()[0][0]

status = ""

while status != "SUCCESS":
    time.sleep(0.5)
    response = requests.get(f"http://127.0.0.1:5000/mass_mail/{first_id}",)

    #print(response.status_code)
    #print(response.text)
    data = response.json()
    status = data["status"]
    result = data["result"]

    print(status, result)

