import requests
import json
from pygame import mixer
import time


ex_cases =0 
url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/cases_by_country.php"

headers = {
    'x-rapidapi-host': "coronavirus-monitor.p.rapidapi.com",
    'x-rapidapi-key': "8a3ae81699msh6204970706adaa4p17beeejsnf1c146a32d1d"
    }

response = requests.request("GET", url, headers=headers)
countries = json.loads(response.text)['countries_stat']

for i in range(10):
	print(str(i+1)+ ":" + countries[i]['country_name'].replace(',',''))

country = int(input("\033[1;32;40m Enter the number of the country you wish to monitor \n"))

while True:
	response = requests.request("GET", url, headers=headers)
	confirmedCases = int(json.loads(response.text)['countries_stat'][country-1]['active_cases'].replace(',',''))
	print( "\033[1;37;40m Current confirmed Cases: " + "\033[1;31;40m" + str(confirmedCases))
	
	if(confirmedCases > ex_cases):
		ex_cases = confirmedCases
		mixer.init()
		mixer.music.load('suffer.mp3')
		mixer.music.play()
		time.sleep(5)
	time.sleep(10)