import requests
url="https://icanhazdadjoke.com/"
response=requests.get(url,headers={"Accept":"application/json"})
#------------------------------------------------+
#text/html---we'll get html files                |
#text/plain---we'll get text files		 |
#application/json---we'll get json file format   |
#------------------------------------------------+
print(response.text)
