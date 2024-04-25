import requests

payload = {"username": "smsboom", "password": "smsboom"}
Auth = requests.post("https://file.weycloud.online/api/auth/login", json=payload)

if Auth.status_code == 200:
    Auth = Auth.json()
    token = Auth["data"]["token"]  # 假设返回的数据结构中有"data"和"token"这样的字段
    print(token)
else:
    print(f"请求失败，状态码：{Auth.status_code}")
    exit()

json = {
    "path": "/Public_Files/SMS-boom/GETAPI.json",
    "password": "",
    "page": 1,
    "per_page": 0,
    "refresh": False
}
headers = {"Authorization":token}
reponse = requests.get("https://file.weycloud.online/p/Public_Files/SMS-boom/GETAPI.json?sign=lSeNeHETFjFK0ty0lPsGenhZ5csmDDcXwvqwhXT3ihk=:0&alist_ts=1712390744275")
print(reponse.text)