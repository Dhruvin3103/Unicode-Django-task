import requests
import json

def find(data):
    url = "https://google-search3.p.rapidapi.com/api/v1/search/q="+data

    headers = {
        "X-User-Agent": "desktop",
        "X-Proxy-Location": "IN",
        "X-RapidAPI-Key": "3fe0d6c75cmsh347351fe90238ccp1bbbabjsn18547a8da9e8",
        "X-RapidAPI-Host": "google-search3.p.rapidapi.com"
    }

    r = requests.request("GET", url, headers=headers)
    return r.json()



# l=d
# l1=d["results"]
#
# # for i in range(len(l)):
# #     print(l[i])
# #     print("\n")
# for j in range(len(l1)):
#  print(l1[j]["title"])
#  print(l1[j]['link'])
#  print(l1[j]['description'])
#  print("---------------------------------------------------------------")
#
# print('Total number of searches : '+ str(l['total']))