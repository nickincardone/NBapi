import utils

'''
TODO unimplemented endpoints
league lineups
    http://stats.nba.com/stats/leaguedashlineups

'''


def get_schedule_from_date(date):
    """
    return games that happen on given date
    args:
        date (string): format=mm/dd/yyyy
    returns:
        games (list): games that happen that day

    each game is a dict with the following available keys
    ["GAME_DATE_EST","GAME_SEQUENCE","GAME_ID","GAME_STATUS_ID",
    "GAME_STATUS_TEXT","GAMECODE","HOME_TEAM_ID","VISITOR_TEAM_ID",
    "SEASON","LIVE_PERIOD","LIVE_PC_TIME",
    "NATL_TV_BROADCASTER_ABBREVIATION","LIVE_PERIOD_TIME_BCAST",
    "WH_STATUS"]

    """
    endpoint = 'http://stats.nba.com/stats/scoreboardv2'
    payload = {
        'DayOffset': '0',
        'LeagueID': '00',
        'gameDate': date
    }
    response = utils.get_response(endpoint, payload)
    return response['GameHeader']


def get_team_game_log(team_id, season):
    """
    return games that a team has already played in given season
    args:
        team_id (int)
        season: format ex: '1999-00', also accepts 1999 or 99
    returns:
        games (list): games a team has played in given season

    each game is a dict with the following available keys
    ["TEAM_ID","GAME_ID","GAME_DATE","MATCHUP","WL","MIN",
    "FGM","FGA","FG_PCT","FG3M","FG3A","FG3_PCT","FTM",
    "FTA","FT_PCT","OREB","DREB","REB","AST","STL","BLK",
    "TOV","PF","PTS"]

    """
    endpoint = 'http://stats.nba.com/stats/teamgamelog'
    payload = {
        "TeamID": team_id,
        "LeagueID": "00",
        "Season": utils.cleanse_season(season),
        "SeasonType": "Regular Season"
    }
    response = utils.get_response(endpoint, payload)
    return response['TeamGameLog']


def get_boxscore(game_id):
    """
    return boxscore for a given game
    args:
        game_id (int)
    returns:
        players (list): players that played in given game and their stats

    each player is a dict with the following available keys
    ["GAME_ID","TEAM_ID","TEAM_ABBREVIATION","TEAM_CITY","PLAYER_ID",
    "PLAYER_NAME","START_POSITION","COMMENT","MIN","FGM","FGA","FG_PCT",
    "FG3M","FG3A","FG3_PCT","FTM","FTA","FT_PCT","OREB","DREB","REB",
    "AST","STL","BLK","TO","PF","PTS","PLUS_MINUS"]

    """
    endpoint = 'http://stats.nba.com/stats/boxscoretraditionalv2'
    payload = {
        'GameID': game_id,
        'StartPeriod': 1,
        'EndPeriod': 10,
        'StartRange': 0,
        'EndRange': 28800,
        'RangeType': 0
    }
    response = utils.get_response(endpoint, payload)
    return response['PlayerStats']


def get_player_info(player_id):
    """
    return a players information
    args:
        player_id (int)
    returns:
        info (dict)

    info is a dict with the following available keys
    ["PERSON_ID","FIRST_NAME","LAST_NAME","DISPLAY_FIRST_LAST",
    "DISPLAY_LAST_COMMA_FIRST","DISPLAY_FI_LAST","BIRTHDATE","SCHOOL",
    "COUNTRY","LAST_AFFILIATION","HEIGHT","WEIGHT","SEASON_EXP","JERSEY",
    "POSITION","ROSTERSTATUS","TEAM_ID","TEAM_NAME","TEAM_ABBREVIATION",
    "TEAM_CODE","TEAM_CITY","PLAYERCODE","FROM_YEAR","TO_YEAR",
    "DLEAGUE_FLAG"]

    """
    endpoint = 'http://stats.nba.com/stats/commonplayerinfo'
    payload = {
        "PlayerID": player_id,
        "LeagueID": "00"
    }
    response = utils.get_response(endpoint, payload)
    return response['CommonPlayerInfo']


def get_player_games(player_id, season):
    """
    return games that a player has already played in given season
    args:
        player_id (int)
        season: format ex: '1999-00', also accepts 1999 or 99
    returns:
        games (list): games a player has played in given season

    each game is a dict with the following available keys
    ["SEASON_ID","PLAYER_ID","GAME_ID","GAME_DATE","MATCHUP","WL","MIN",
    "FGM","FGA","FG_PCT","FG3M","FG3A","FG3_PCT","FTM","FTA","FT_PCT",
    "OREB","DREB","REB","AST","STL","BLK","TOV","PF","PTS","PLUS_MINUS",
    "VIDEO_AVAILABLE"]

    """
    endpoint = 'http://stats.nba.com/stats/playergamelog'
    payload = {
        "PlayerID": player_id,
        "LeagueID": "00",
        "Season": utils.cleanse_season(season),
        "SeasonType": "Regular Season"
    }
    response = utils.get_response(endpoint, payload)
    return response['PlayerGameLog']


def get_team_info(team_id, season):
    """
    return a team's information
    args:
        team_id (int)
        season: format ex: '1999-00', also accepts 1999 or 99
    returns:
        info (dict)

    info is a dict with the following available keys
    ["TEAM_ID","SEASON_YEAR","TEAM_CITY","TEAM_NAME","TEAM_ABBREVIATION",
    "TEAM_CONFERENCE","TEAM_DIVISION","TEAM_CODE","W","L","PCT",
    "CONF_RANK","DIV_RANK","MIN_YEAR","MAX_YEAR"]

    """
    endpoint = 'http://stats.nba.com/stats/teaminfocommon'
    payload = {
        "LeagueID": "00",
        "Season": utils.cleanse_season(season),
        "SeasonType": "Regular Season",
        "TeamID": team_id
    }
    response = utils.get_response(endpoint, payload)
    return response['TeamInfoCommon']


def get_team_roster(team_id, season):
    """
    return players on a team (only current players if this season)
    args:
        team_id (int)
        season: format ex: '1999-00', also accepts 1999 or 99
    returns:
        players (list): players on roster

    each player is a dict with the following available keys
    ["TeamID","SEASON","LeagueID","PLAYER","NUM","POSITION","HEIGHT",
    "WEIGHT","BIRTH_DATE","AGE","EXP","SCHOOL","PLAYER_ID"]

    """
    endpoint = 'http://stats.nba.com/stats/commonteamroster'
    payload = {
        "TeamID": team_id,
        "LeagueID": "00",
        "Season": utils.cleanse_season(season)
    }
    response = utils.get_response(endpoint, payload)
    return response['CommonTeamRoster']


def get_player_shot_log(player_id):
    # TODO: document
    endpoint = 'http://stats.nba.com/stats/playerdashptshotlog'
    payload = {
        "LeagueID": "00",
        "Season": "2014-15",
        "SeasonType": "Regular Season",
        "PlayerID": player_id,
        "TeamID": 0,
        "Outcome": 'null',
        "Location": 'null',
        "Month": 0,
        "SeasonSegment": 'null',
        "DateFrom": 'null',
        "DateTo": 'null',
        "OpponentTeamID": 0,
        "VsConference": 'null',
        "VsDivision": 'null',
        "GameSegment": 'null',
        "Period": 0,
        "LastNGames": 0
    }
    response = utils.get_response(endpoint, payload)
    return response


def get_player_rebound_log(player_id):
    # TODO: document
    endpoint = 'http://stats.nba.com/stats/playerdashptreboundlogs'
    payload = {
        "LeagueID": "00",
        "Season": "2014-15",
        "SeasonType": "Regular Season",
        "PlayerID": player_id,
        "TeamID": 0,
        "Outcome": 'null',
        "Location": 'null',
        "Month": 0,
        "SeasonSegment": 'null',
        "DateFrom": 'null',
        "DateTo": 'null',
        "OpponentTeamID": 0,
        "VsConference": 'null',
        "VsDivision": 'null',
        "GameSegment": 'null',
        "Period": 0,
        "LastNGames": 0
    }
    response = utils.get_response(endpoint, payload)
    return response


def get_all_players(season, all_time=False):
    """
    return boxscore for a given game
    args:
        game_id (int)
    returns:
        players (list)

    each player is a dict with the following available keys
    ["PERSON_ID","DISPLAY_LAST_COMMA_FIRST","ROSTERSTATUS","FROM_YEAR",
    "TO_YEAR","PLAYERCODE"]

    """

    # IsOnlyCurrentSeason: 0 is false 1 is true
    cur_season = 1
    if all_time:
        cur_season = 0

    endpoint = 'http://stats.nba.com/stats/commonallplayers'
    payload = {
        "LeagueID": "00",
        "Season": utils.cleanse_season(season),
        "IsOnlyCurrentSeason": cur_season
    }
    response = utils.get_response(endpoint, payload)
    return response['CommonAllPlayers']
