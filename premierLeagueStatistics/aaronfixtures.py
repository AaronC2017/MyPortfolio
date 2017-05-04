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

selection = raw_input("Press 1 for Premier League Table. \nPress 2 for Premier League Fixtures.\n Press 3 for Stats on your favourite Team")
#Opening up up connection, grabbing the page
if selection == "1":
	uClient = uReq(Table)
	pageHtml = uClient.read()
	uClient.close()
	#html parsing
	page_soup = soup(pageHtml, "html.parser")
	tableTeam = page_soup.findAll("tr",{"class":"standing-table__row"})
	#Printing todays date
	print "As of: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
	#Header
	print "Barclay's Premier League Table  \n"
	#Loop through each team. Remove unicode and information not needed from list.
	
	#Table Header
	x =  tableTeam[0].text.split( )
	print u"  ".join(x[0:-2])
	#Actual Table loop. 20 Teams.
	i = 1
	while i < 21:
		l =  tableTeam[i].text.split( )
		print u" ".join(l)
		i = i + 1

elif selection == "2":
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
	currdate = 0
	while i < len(fixtureTeamLeft):
		print fixtureTeamLeft[i].text.strip(), "vs", fixtureTeamRight[i].text.strip(), time[i].text.strip()
		i = i + 1

elif selection == "3":
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
		print fixtureTeamLeft[i].text.strip(), "vs", fixtureTeamRight[i].text.strip(), time[i].text.strip()
		i = i + 1
	
	
	

