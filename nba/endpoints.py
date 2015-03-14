import requests
nba_api = 'http://stats.nba.com/stats/'
schedule_endpoint = nba_api+'scoreboardv2'
boxscore_endpoint = nba_api+'boxscoretraditionalv2'
team_schedule_endpoint = nba_api+'teamgamelog'

#known enpoints
'''
http://stats.nba.com/stats/playerprofile
http://stats.nba.com/stats/commonplayerinfo
http://stats.nba.com/stats/commonallplayers
http://stats.nba.com/stats/teamdashboardbygeneralsplits
http://stats.nba.com/stats/playerdashboardbygeneralsplits
http://stats.nba.com/stats/shotchartdetail
http://stats.nba.com/stats/scoreboard/
http://stats.nba.com/stats/playbyplay
http://stats.nba.com/stats/boxscorescoring
http://stats.nba.com/stats/boxscoreusage
http://stats.nba.com/stats/boxscoremisc
http://stats.nba.com/stats/boxscoreadvanced
http://stats.nba.com/stats/boxscorefourfactors
'''

def get_schedule(date):
    # date format: string mm/dd/yyyy
    payload = {
        'DayOffset': '0',
        'LeagueID': '00',
        'gameDate': date
    }
    r = requests.get(schedule_endpoint, params=payload)
    return r.json()

def get_team_schedule(team_id, season):
    # season format ex. 2014-15
    payload = {
        "TeamID":team_id,
        "LeagueID":"00",
        "Season":season,
        "SeasonType":"Regular Season"
    }
    r = requests.get(team_schedule_endpoint, params=payload)
    return r.json()

def get_boxscore(game_id):
    payload = {
        'GameID': game_id,
        'StartPeriod': 1,
        'EndPeriod': 10,
        'StartRange': 0,
        'EndRange': 28800,
        'RangeType': 2
    }
    r = requests.get(boxscore_endpoint, params=payload)
    return r.json()