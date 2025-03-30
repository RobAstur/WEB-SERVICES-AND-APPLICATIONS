
#Import the modules
import requests
import json

#Url for the API
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

# Function to get all data from the API
def getALL():
    response = requests.get(url)
    return response.json()

#open file and convert data into jason
if __name__ == "__main__":
    with open ("cso.json", "wt") as fp:
        print(json.dumps(getALL()), file = fp)
