import utils

def get_schedule(date, pretty=True):
    # date format: string mm/dd/yyyy
    endpoint = 'http://stats.nba.com/stats/scoreboardv2' 
    payload = {
        'DayOffset': '0',
        'LeagueID': '00',
        'gameDate': date
    }
    response = utils.get_response(endpoint, payload)
    return response['GameHeader']

def get_team_schedule(team_id, season, pretty=True):
    # season format ex. 2014-15
    endpoint = 'http://stats.nba.com/stats/teamgamelog'
    payload = {
        "TeamID":team_id,
        "LeagueID":"00",
        "Season":utils.clease_season(season),
        "SeasonType":"Regular Season"
    }
    response = utils.get_response(endpoint, payload)
    return response['TeamGameLog']

def get_boxscore(game_id):
    endpoint = 'http://stats.nba.com/stats/boxscoretraditionalv2'
    payload = {
        'GameID': game_id,
        'StartPeriod': 1,
        'EndPeriod': 10,
        'StartRange': 0,
        'EndRange': 28800,
        'RangeType': 2
    }
    response = utils.get_response(endpoint, payload)
    return response['PlayerStats']

def get_player_info(player_id):
    # example james harden = 201935
    endpoint = 'http://stats.nba.com/stats/commonplayerinfo'
    payload = {
        "PlayerID":player_id,
        "LeagueID":"00"
    }
    response = utils.get_response(endpoint, payload)
    return response

def get_player_games(player_id, season):
    endpoint = 'http://stats.nba.com/stats/playergamelog'
    payload = {
        "PlayerID":player_id,
        "LeagueID":"00",
        "Season":utils.clease_season(season),
        "SeasonType":"Regular Season"
    }
    response = utils.get_response(endpoint, payload)
    return response

def get_team_info(team_id, season):
    endpoint = 'http://stats.nba.com/stats/teaminfocommon'
    payload = {
        "LeagueID":"00",
        "Season":utils.clease_season(season),
        "SeasonType":"Regular Season",
        "TeamID":team_id
    }
    response = utils.get_response(endpoint, payload)
    return response

def get_team_roster(team_id, season):
    endpoint = 'http://stats.nba.com/stats/commonteamroster'
    payload = {
        "TeamID":team_id,
        "LeagueID":"00",
        "Season":utils.clease_season(season)
    }
    response = utils.get_response(endpoint, payload)
    return response

def get_player_shot_log(player_id):
    endpoint = 'http://stats.nba.com/stats/playerdashptshotlog'
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
    response = utils.get_response(endpoint, payload)
    return response

def get_player_rebound_log(player_id):
    endpoint = 'http://stats.nba.com/stats/playerdashptreboundlogs'
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
    response = utils.get_response(endpoint, payload)
    return response

def get_all_players(season, all_time=False):
    # 0 is false 1 is true
    cur_season = 1
    if all_time:
        cur_season = 0

    endpoint = 'http://stats.nba.com/stats/commonallplayers'
    payload = {
        "LeagueID":"00",
        "Season":utils.clease_season(season),
        "IsOnlyCurrentSeason":cur_season
    }
    response = utils.get_response(endpoint, payload)
    return response
