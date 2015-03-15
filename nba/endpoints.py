import utils

# TODO break these out in a more oo way
nba_api = 'http://stats.nba.com/stats/'
schedule = nba_api+'scoreboardv2' 
boxscore = nba_api+'boxscoretraditionalv2'
team_schedule = nba_api+'teamgamelog'
player_info = nba_api+'commonplayerinfo'
player_game_log = nba_api+'playergamelog'
team_info = nba_api+'teaminfocommon'
all_players = nba_api+'commonallplayers'
team_rosteresponse = nba_api+'commonteamroster'
player_shot_log = nba_api+'playerdashptshotlog'
player_rebound_log = nba_api+'playerdashptreboundlogs'

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
    schedule = []
    payload = {
        'DayOffset': '0',
        'LeagueID': '00',
        'gameDate': date
    }
    response = utils.get_response(schedule, payload)
    games = response['GameHeader']
    for game in games:
        cur_game = {
            'id':game['GAME_ID'],
            'home_team':game['HOME_TEAM_ID'],
            'away_team':game['VISITOR_TEAM_ID'],
            'season':game['SEASON'],
            'status':game['GAME_STATUS_TEXT'],
            'date':game['GAME_DATE_EST']
        }
        schedule.append(cur_game)
    return schedule

def get_team_schedule(team_id, season):
    # season format ex. 2014-15
    payload = {
        "TeamID":team_id,
        "LeagueID":"00",
        "Season":utils.clease_season(season),
        "SeasonType":"Regular Season"
    }
    response = utils.get_response(team_schedule, payload)
    return response

def get_boxscore(game_id):
    payload = {
        'GameID': game_id,
        'StartPeriod': 1,
        'EndPeriod': 10,
        'StartRange': 0,
        'EndRange': 28800,
        'RangeType': 2
    }
    response = utils.get_response(boxscore, payload)
    return response

def get_player_info(player_id):
    # example james harden = 201935
    payload = {
        "PlayerID":player_id,
        "LeagueID":"00"
    }
    response = utils.get_response(player_info, payload)
    return response

def get_player_games(player_id, season):
    payload = {
        "PlayerID":player_id,
        "LeagueID":"00",
        "Season":utils.clease_season(season),
        "SeasonType":"Regular Season"
    }
    response = utils.get_response(player_game_log, payload)
    return response

def get_team_info(team_id, season):
    payload = {
        "LeagueID":"00",
        "Season":utils.clease_season(season),
        "SeasonType":"Regular Season",
        "TeamID":team_id
    }
    response = utils.get_response(team_info, payload)
    return response

def get_team_roster(team_id, season):
    payload = {
        "TeamID":team_id,
        "LeagueID":"00",
        "Season":utils.clease_season(season)
    }
    response = utils.get_response(team_roster, payload)
    return response

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
    response = utils.get_response(player_shot_log, payload)
    return response

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
    response = utils.get_response(player_rebound_log, payload)
    return response

def get_all_players(season, all_time=False):
    # 0 is false 1 is true
    cur_season = 1
    if all_time:
        cur_season = 0

    payload = {
        "LeagueID":"00",
        "Season":utils.clease_season(season),
        "IsOnlyCurrentSeason":cur_season
    }
    response = utils.get_response(all_players, payload)
    return response
