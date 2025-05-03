import requests
import json

url = "http://scorestream.com/api?request="

# test widget: 4939
# my widget: 50251

jsonData = {
    "method": 'games.search',
    "params": {
        "state": 'TX',
        "afterDateTime": '2022-09-09 05:00:00',
        "beforeDateTime": '2022-09-10 05:00:00',
        "sportNames": ['football'],
        "squadIds": [1010],
        "aboveConfidenceGrade": 30,
        "count": 2000,
        "apiKey": 'e68c9cdb-2dce-4f67-992b-0140d2d96d4c'}
}
response = requests.get(url+json.dumps(jsonData))
games = json.loads(response.text)

ids = games["result"]["gameIds"]
# print(ids)

for i in [0, len(ids)-1]:
    print(f"ID:{ids[i]}")
    print("Time:"+games["result"]["collections"]
          ["gameCollection"]["list"][i]["startDateTime"])
    print("---")
