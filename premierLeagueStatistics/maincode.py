#importation of modules needed to scrape SkySports.com using BeautifulSoup

input_message = "Press 1 for Premier League Table. \nPress 2 for Premier League Fixtures.\nPress 3 for Stats on your Favourite Team\nPress E to exit\n"

def main():
  select = raw_input(input_message)
  #Opening up up connection, grabbing the page

  #if select != "1" or select != "2" or select != "3":
  #	select = raw_input("Press 1 for Premier League Table. \nPress 2 for Premier League Fixtures.\nPress 3 for Stats on your Favourite Team\n")

  while select != "1" and select != "2" and select != "3" and select.lower() != "e":
    print "Not a valid option."
    select = raw_input(input_message)

  if select == "1":
	  from part1 import part1
	  part1()

  elif select == "2":
	  from part2 import part2
	  part2()

  elif select == "3":
	  from part3 import part3
	  part3()

  elif select.lower() == "e":
	  print "Exiting program."	
	  exit()

if __name__ == "__main__":
  main()
    
