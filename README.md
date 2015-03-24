# NBapi
python wrapper for the undocumented/unofficial NBA stats api

`endpoints.py` contains methods to call the api along with documentation
## Use
The NBA stats api is unofficial and undocumented so these endpoints may break or return unexpected data at any time. Please rate limit all requests. Please be smart when using this wrapper, do not try to copy every stat the NBA has ever collected.

## implemented endpoints

```
http://stats.nba.com/stats/scoreboardv2
http://stats.nba.com/stats/teamgamelog
http://stats.nba.com/stats/boxscoretraditionalv2
http://stats.nba.com/stats/commonplayerinfo
http://stats.nba.com/stats/playergamelog
http://stats.nba.com/stats/teaminfocommon
http://stats.nba.com/stats/commonteamroster
http://stats.nba.com/stats/playerdashptshotlog
http://stats.nba.com/stats/playerdashptreboundlogs
http://stats.nba.com/stats/commonallplayers
http://stats.nba.com/stats/leagueleaders
http://stats.nba.com/stats/boxscoreplayertrackv2
http://stats.nba.com/stats/playbyplayv2
http://stats.nba.com/stats/shotchartdetail
http://stats.nba.com/stats/leaguedashplayerstats
http://stats.nba.com/stats/leaguedashteamstats

#sportsvu team endpoints
http://stats.nba.com/js/data/sportvu/{season}/drivesTeamData.json
http://stats.nba.com/js/data/sportvu/{season}/defenseTeamData.json
http://stats.nba.com/js/data/sportvu/{season}/catchShootTeamData.json
http://stats.nba.com/js/data/sportvu/{season}/speedTeamData.json
http://stats.nba.com/js/data/sportvu/{season}/shootingTeamData.json
http://stats.nba.com/js/data/sportvu/{season}/reboundingTeamData.json
http://stats.nba.com/js/data/sportvu/{season}/pullUpShootTeamData.json
http://stats.nba.com/js/data/sportvu/{season}/touchesTeamData.json
http://stats.nba.com/js/data/sportvu/{season}/passingTeamData.json

#sportsvu player endpoints
http://stats.nba.com/js/data/sportvu/{season}/drivesData.json
http://stats.nba.com/js/data/sportvu/{season}/defenseData.json
http://stats.nba.com/js/data/sportvu/{season}/catchShootData.json
http://stats.nba.com/js/data/sportvu/{season}/speedData.json
http://stats.nba.com/js/data/sportvu/{season}/shootingData.json
http://stats.nba.com/js/data/sportvu/{season}/reboundingData.json
http://stats.nba.com/js/data/sportvu/{season}/pullUpShootData.json
http://stats.nba.com/js/data/sportvu/{season}/touchesData.json
http://stats.nba.com/js/data/sportvu/{season}/passingData.json

#synergy player endpoints
http://stats.nba.com/js/data/playtype/player_Transition.js
http://stats.nba.com/js/data/playtype/player_Cut.js
http://stats.nba.com/js/data/playtype/player_PRBallHandler.js
http://stats.nba.com/js/data/playtype/player_Handoff.js
http://stats.nba.com/js/data/playtype/player_Isolation.js
http://stats.nba.com/js/data/playtype/player_Misc.js
http://stats.nba.com/js/data/playtype/player_Postup.js
http://stats.nba.com/js/data/playtype/player_PRRollMan.js
http://stats.nba.com/js/data/playtype/player_Spotup.js
```

## Contributing
Feel free to help implement and document the unimplented endpoints, look at endpoints.py to see how the methods and docs are set up. If you have a suggestion to improve the wrapper or documentation please let me know.

## unimplemented endpoints
```
http://stats.nba.com/stats/locations_getmoments
http://stats.nba.com/stats/videodetails
http://stats.nba.com/stats/leaguedashplayerclutch
http://stats.nba.com/stats/leaguedashplayershotlocations
http://stats.nba.com/stats/leaguedashteamclutch
http://stats.nba.com/stats/leaguedashteamshotlocations
http://stats.nba.com/stats/playervsplayer
http://stats.nba.com/stats/teamvsplayer

http://stats.nba.com/js/data/playtype/Screen.js
http://stats.nba.com/js/data/playtype/Rebound.js

http://stats.nba.com/js/data/playtype/team_Transition.js
http://stats.nba.com/js/data/playtype/team_Cut.js
http://stats.nba.com/js/data/playtype/team_PRBallHandler.js
http://stats.nba.com/js/data/playtype/team_Handoff.js
http://stats.nba.com/js/data/playtype/team_Isolation.js
http://stats.nba.com/js/data/playtype/team_Misc.js
http://stats.nba.com/js/data/playtype/Screen.js
http://stats.nba.com/js/data/playtype/team_Postup.js
http://stats.nba.com/js/data/playtype/Rebound.js
http://stats.nba.com/js/data/playtype/team_PRRollMan.js
http://stats.nba.com/js/data/playtype/team_Spotup.js)
```