


def part2():
	#importation of modules needed to scrape SkySports.com using BeautifulSoup
	import bs4
	import urllib2
	from urllib2 import urlopen as uReq
	from bs4 import BeautifulSoup as soup
	import datetime

	#Link for premier league table
	Table = "http://www.skysports.com/premier-league-table"
	#Link for fixtures
	Fixtures = "http://www.skysports.com/premier-league-fixtures"

	uClient = uReq(Fixtures)
	pageHtml = uClient.read()
	uClient.close()
	#html parsing
	page_soup = soup(pageHtml, "html.parser")
	#Printing todays date
	print "As of: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
	#Header
	print "Barclay's Premier League Fixtures  \n"
	matchdate = page_soup.findAll("h3",{"class":"fixres__header1"})
	fixtureTeamLeft = page_soup.findAll("span",{"class":"matches__item-col matches__participant matches__participant--side1"})
	fixtureTeamRight = page_soup.findAll("span",{"class":"matches__item-col matches__participant matches__participant--side2"})
	time = page_soup.findAll("span",{"class":"matches__date"})
	date = page_soup.findAll("h4",{"class":"fixres__header2"})
	i = 0
	while i < len(fixtureTeamLeft):
	  print "\n",fixtureTeamLeft[i].text.strip(), "vs", fixtureTeamRight[i].text.strip(), time[i].text.strip()
	  i = i + 1
