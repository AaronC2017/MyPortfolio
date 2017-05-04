#importation of modules needed to scrape SkySports.com using BeautifulSoup
def part3A(favTeam):
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
  matchdate = page_soup.findAll("h3",{"class":"fixres__header1"})
  fixtureTeamLeft = page_soup.findAll("span",{"class":"matches__item-col matches__participant matches__participant--side1"})
  fixtureTeamRight = page_soup.findAll("span",{"class":"matches__item-col matches__participant matches__participant--side2"})
  time = page_soup.findAll("span",{"class":"matches__date"})
  date = page_soup.findAll("h4",{"class":"fixres__header2"})

  favTeam = favTeam.title()
  #finding the length of the longest line that being printed in the second while loop
  i = 0
  longest = -1
  while i < len(fixtureTeamLeft):
    x = fixtureTeamLeft[i].text.strip() + " vs " + fixtureTeamRight[i].text.strip() + " " + time[i].text.strip()
    if favTeam in x:
      if len(x) > int(longest):
        longest = len(x)
    i += 1
  dashes = "-" * (longest + 2)
  print longest

  #Printing todays date
  premier_date= "As of the: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
  print " " * int( (longest + 2 - len(premier_date) )/2 )  + premier_date
  #Header
  header= "Barclay's Premier League Fixtures"
  print " " * int( (longest + 2 - len(header) )/2 )  + header

  #favTeam = raw_input("Choose Team\n").title()
  print "+" + dashes + "+"

  i = 0
  while i < len(fixtureTeamLeft):
    x = fixtureTeamLeft[i].text.strip() + " vs " + fixtureTeamRight[i].text.strip() + " " + time[i].text.strip()
    if favTeam in x:
      print "| " + x + (" " * (longest - len(x) + 1)) + "|"
      print "+" + dashes + "+"
    i = i + 1
  from maincode import main
  main()
    

