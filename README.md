# Simple-Scraper
A simple scraping program
Goes through websites one by one, downloading and formatting any & all data it finds. (Used adact.me's campaign leaderboard logs in this case)


**Example input (https://x9c98fh3ng.execute-api.eu-west-1.amazonaws.com/production/leaderboard?campaignId=3&limit=100):**

  ```[{"score":1600,"leaderboardName":"asd"},{"score":1200,"leaderboardName":"test"}]```


**Output:**
  ```
  asd:1600
  test:1200
  ```
  
 Usage:
 Change the log URL within the code, then run it.
 ```
 run - runs the scraper
 rem - removes the logs
 help, cmds, cmd, ? - lists the commands
 ```
