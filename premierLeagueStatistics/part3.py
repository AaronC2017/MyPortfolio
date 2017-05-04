def part3():
  #importation of modules needed to scrape SkySports.com using BeautifulSoup
  import bs4
  import urllib2
  from urllib2 import urlopen as uReq
  from bs4 import BeautifulSoup as soup
  import datetime
  from part3A import part3A

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
  #Printing todays date
  #Table Header
  #chelsea =  tableTeam[1].text.split( )


  dic={}
  #this creats the dictionary
  i=1
  while i < len(tableTeam):
    parse= tableTeam[i].text.lower().split()
    if len(parse) == 10:
      club=" ".join(parse[1:2])
      tableRow=parse[2:]
    elif len(parse) == 11:
      club=" ".join(parse[1:3])
      tableRow=parse[3:]
    elif len(parse) == 12:
      club=" ".join(parse[1:4])
      tableRow=parse[4:]
    if club not in dic:
      dic[club]=tableRow
      #return "Team name entered is incorrect"
    i=i+1


  #this keeps asking until the team entered is in the dictionary
  input_message= "What is your favourite team? (or type E to exit)\n"
  favTeam = raw_input(input_message).lower()
  while favTeam not in dic and favTeam != "e":
    print "Team name entered is incorrect"
    favTeam = raw_input(input_message).lower()

  if favTeam == "e":
    exit()

  # if its in the dictionary its 1st print out your favourate team full details then asks you for the stats of the team and calulates it
  if favTeam in dic: # unneeded
    x=dic[favTeam]
    top=tableTeam[0].text.split()
    print "-".join(top[1:-2])
    print favTeam.upper(),"  ".join(dic[favTeam])
    input_message = "\nType in yes/no if you would you like to know the statistics for " + favTeam.title() +"?" +"\n"
    stats=raw_input(input_message).lower()
    while stats != "yes" and stats != "y" and stats != "no" and stats != "n":
      print "Not a valid option."
      stats=raw_input(input_message).lower()
    if stats== "yes" or stats == "y":
      pts_per_game= float(x[7])/float(x[0])
      goals_per_game= float(x[4])/float(x[0])
      goalsCon_per_game= float(x[5])/float(x[0])
      print "\n" + favTeam.upper()
      print "Points per Game: " , round(pts_per_game, 2)
      print "Goals Scored per Game: " , round(goals_per_game, 2)
      print "Goals Conceded per Game: " , round(goalsCon_per_game, 2)
    elif stats =="no" or stats == "n":
      print "That's ok. Feel free to run the program again."
      print "Exiting program."	
      exit()


    #ask for your teams remaining fixtures and loads up part3A 
    input_message = "Would you like " + favTeam.title() + "'s remaining fixtures? (y for yes, n for no)\n"
    question=raw_input(input_message).lower()
    while question != "yes" and question != "y" and question != "no" and question != "n":
      print "Not a valid option."
      question=raw_input(input_message).lower()

    if question=="yes" or question=="y":
      part3A(favTeam)
    else: # question=="no" or question=="n"
      exit()
