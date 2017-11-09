#### Premier League New-Winner Python Script

Python script that scrapes English Premier League match data for two seasons using Beautiful Soup and determines a new winner based on a very simple algorithm (explained below).

Our champion basically becomes the team that beat the reigning champion. For example:

> Current champion at the start of gameweek 1 is Chelsea

> Chelsea gets beaten (for the first time this season) by West Ham in gameweek 14

> New champion is West Ham 

> If West Ham remain unbeaten till the end of the season (gameweek 38), they are the eventual champions

> Carry this champion into next season and continue
