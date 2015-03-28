
import requests
import sys
from bs4 import BeautifulSoup
import string
import re

#set the chamption of season 2011-12

currChamp = 'Manchester City'

#loop twice
for guy in range (0, 2):

    #links for season 12-13 and 13-14
    r = ("http://www.soccerstats.com/table.asp?league=england_2013&tid=a", "http://www.soccerstats.com/table.asp?league=england_2014&tid=a")

    rurl = requests.get(r[guy])

    soup = BeautifulSoup(rurl.content)

    #declare empty lists where the team names and scores will be stored
    #note that these lists become empty for the new season
    home = []
    away = []
    score = []

    #Get all the tr's for each table and store them in rows
    for i in range (0, 38):

        #Find table with ID = statnowidth and width = 100% specifically (there's two tables with the same ID)
        #Each table = 1 gameweek
        Table = soup.findAll('table', {"class" : "statnowidth", "width" : "100%"})[i]

        #starting the loop from 1 excludes the Round number
        for j in range (1, 11):

            rows = Table.findAll('tr')[j]

            #this would give find the first instance of the current champions' game in this gameweek

            #these searchrows correspond to Home team, Away team and Score respectively for each row in the table
            searchrow = rows.findAll('td')[1]
            searchrow1 = rows.findAll('td')[-2]
            searchrow2 = rows.findAll('td')[-1]

            #converting to string and cleaning it up to make it easily searchable
            homestr = str(searchrow)
            awaystr = str(searchrow1)
            scorestr = str(searchrow2)

            homestr = re.sub('<[^<]+?>', '', homestr)
            awaystr = re.sub('<[^<]+?>', '', awaystr)
            scorestr = re.sub('<[^<]+?>', '', scorestr)

            homestr = homestr.replace('\xc2\xa0', '')
            awaystr = awaystr.replace('\xc2\xa0', '')
            scorestr = scorestr.replace('\n', '')

            #add team name/score to respective lists
            home.append(homestr)
            away.append(awaystr)
            score.append(scorestr)

    #game 0 would be between home[0] and away[0] and the score would be score[0]
    #so, we can iterate through the size of any (they're all the same) 
    for x in range (0, 380):
    #380 games in 2 years + this implementation = inefficient program

        #if current champion is involved in this match
        if (home[x] == currChamp or away[x] == currChamp):

            #current score format is '1 - 0'
            #this splits on whitespace and stores all in a set
            indscores = score[x].split()

            #assign home/away score
            homeScore = indscores[0]
            awayScore = indscores[2]

            #depending on who wins, new champions!
            if (homeScore > awayScore):
                currChamp = home[x]

            elif (awayScore > homeScore):
                currChamp = away[x]

            #if draw, nobody cares so do nothing
  
    #print final champions (at the end of each year)

    print currChamp





