import requests
from bs4 import BeautifulSoup
import json

#request myinstants
r = requests.get('http://www.myinstants.com/search/?name=que+delicia')
soup = BeautifulSoup(r.text, 'html.parser')
buttonList = [];
#each button
for link in soup.find_all("div", class_="instant"):
    #name
    buttonName = link.a.text
    #parse song url
    buttonUrl = link.find("div", class_="small-button")
    s = buttonUrl['onclick']
    buttonUrl = s.partition("('")[-1].rpartition("')")[0]

    button = {
        "name": buttonName,
        "url": buttonUrl
    }
    buttonList.append(button)

#show
print( json.dumps(buttonList) )
