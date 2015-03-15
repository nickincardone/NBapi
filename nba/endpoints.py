import requests
nba_api = 'http://stats.nba.com/stats/'
schedule_endpoint = nba_api+'scoreboardv2'
boxscore_endpoint = nba_api+'boxscoretraditionalv2'
team_schedule_endpoint = nba_api+'teamgamelog'
player_info = nba_api+'commonplayerinfo'
player_game_log = nba_api+'playergamelog'
team_info = nba_api+'teaminfocommon'
all_players = nba_api+'commonallplayers'
team_roster = nba_api+'commonteamroster'
player_shot_log = nba_api+'playerdashptshotlog'
player_rebound_log = nba_api='playerdashptreboundlogs'

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
http://stats.nba.com/feeds/RotoWirePlayers-583598/team_id.json
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

def get_player_info(player_id):
    # example james harden = 201935
    payload = {
        "PlayerID":player_id,
        "LeagueID":"00"
    }
    r = requests.get(player_info, params=payload)
    return r.json()

def get_player_games(player_id, season):
    payload = {
        "PlayerID":player_id,
        "LeagueID":"00",
        "Season":season,
        "SeasonType":"Regular Season"
    }
    r = requests.get(player_game_log, params=payload)
    return r.json()

def get_team_info(team_id, season):
    payload = {"LeagueID":"00","Season":season,"SeasonType":"Regular Season","TeamID":team_id}
    r = requests.get(team_info, params=payload)
    return r.json()

def get_team_roster(team_id, season):
    payload = {"TeamID":team_id,"LeagueID":"00","Season":season}
    r = requests.get(team_roster, params=payload)
    return r.json()

def get_player_shot_log(player_id):
    payload = {
        "LeagueID":"00",
        "Season":"2014-15",
        "SeasonType":"Regular Season",
        "PlayerID":player_id,
        "TeamID":0,
        "Outcome":'null',
        "Location":'null',
        "Month":0,
        "SeasonSegment":'null',
        "DateFrom":'null',
        "DateTo":'null',
        "OpponentTeamID":0,
        "VsConference":'null',
        "VsDivision":'null',
        "GameSegment":'null',
        "Period":0,
        "LastNGames":0
    }
    r = requests.get(player_shot_log, params=payload)
    return r.json()

def get_player_rebound_log(player_id):
    payload = {
        "LeagueID":"00",
        "Season":"2014-15",
        "SeasonType":"Regular Season",
        "PlayerID":player_id,
        "TeamID":0,
        "Outcome":'null',
        "Location":'null',
        "Month":0,
        "SeasonSegment":'null',
        "DateFrom":'null',
        "DateTo":'null',
        "OpponentTeamID":0,
        "VsConference":'null',
        "VsDivision":'null',
        "GameSegment":'null',
        "Period":0,
        "LastNGames":0
    }
    r = requests.get(player_rebound_log, params=payload)
    return r.json()

def get_all_players(season, all_time=False):
    # 0 is false 1 is true
    cur_season = 1
    if all_time:
        cur_season = 0

    payload = {"LeagueID":"00","Season":season,"IsOnlyCurrentSeason":cur_season}
    r = requests.get(all_players, params=payload)
    return r.json()