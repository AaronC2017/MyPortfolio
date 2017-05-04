def part1():
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


  #Opening up up connection, grabbing the page
  uClient = uReq(Table)
  pageHtml = uClient.read()
  uClient.close()
  #html parsing
  page_soup = soup(pageHtml, "html.parser")



  tableTeam = page_soup.findAll("tr",{"class":"standing-table__row"})
  #finding the length of the longest line that being printed in the second while loop
  i = 2
  l =  tableTeam[1].text.split()
  l = u" ".join(l)
  longest = len(l)
  while i < 21:
    l =  tableTeam[i].text.split()
    l = u" ".join(l)
    if(len(l) > longest):
      longest = len(l)
    i += 1
  dashes = "-" * (longest + 2)

  date = "As of: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
  #this is some mad maths but sure look b grand i.e how we centered it  
  # Variable x is the number of spaces needed on both sides of the text for the text to be centered
  # equation:
  # longest + 2 = 2x +len(date or header)
  # longest + 2 - len(date or header) = 2x
  # (longest + 2 - len(date or header))/2 = x
  print " " * int( (longest + 2 - len(date) )/2 )  + date
  #Header
  header = "Barclay's Premier League Table"
  print " " * int( (longest + 2 - len(header) )/2 )  + header
  
  print "+" + dashes + "+"

  i = 0   
  while i < 21:
    l =  tableTeam[i].text.split()     
    l = u" ".join(l)
    print "| " + l + (" " * (longest - len(l) + 1)) + "|"
    print "+" + dashes + "+"
    i = i + 1
    
  from maincode import main
  main()

