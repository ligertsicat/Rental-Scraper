import requests
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

import json

output = open("rentpad_list.csv", "w+")

def scrapeRentpad(city):

	payload = {
            "a":"31",
            "cityName":"Mandaluyong",
            "propertyTypeIDs":[2,3,5],
            "furnishTypeIDs":[1,2,3],
            "placeIDs":[],
            "statusTypeIDs":[],
            "amenityIDs":[],
            "longMonthRateLow":"0",
            "longMonthRateHigh":"30,000",
            "numBedroomsLow":"0",
			"numBedroomsHigh":"0",
			"itemsPerPage":"1000",
			"pageNumber":"1",
			"lengthOfStay":"",
			"ham":"ham"


	}
	r = requests.post(
			url="https://rentpad.com.ph/long-term-rentals/mandaluyong/apartment#",
			data=payload,

		)

	html = BeautifulSoup(r.text, 'html.parser')
	prices = html.find_all(itemprop="price")
	apartments = html.find_all(itemprop="name")
	links = html.find_all(itemprop="offers")

	i = 0
	for apartment in apartments:
		if apartment.string == None:
			continue
		price = prices[i].string[1:].replace(",", "")
		link = links[i].find('a').get('href')
		print(apartment.string + "," + price + "," + link)
		output.write(apartment.string+","+price+","+link+"\n")
		i+=1



scrapeRentpad("Mandaluyong")
