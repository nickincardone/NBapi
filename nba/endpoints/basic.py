from nba import utils

'''
available methods
    schedule_from_date
    standings_from_date
    team_leaders_from_date
    team_game_log
    play_by_play
    boxscore
    player_tracking_from_game
    all_players_stats
    all_teams_stats
    player_game_shot_chart
    player_info
    player_game_log
    league_leaders
    league_lineups
    team_info
    team_roster
    team_coaching_staff
    player_shot_log
    player_rebound_log
    all_players
'''


def schedule_from_date(date):
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


def standings_from_date(date):
    """
    return the standing on a given date
    args:
        date (string): format=mm/dd/yyyy
    returns:
        standings (dict) keys are 'EAST', and 'WEST'
            values are teams

    teams (list): games that happen that day

    each team is a dict with the following available keys
    ["TEAM_ID","LEAGUE_ID","SEASON_ID","STANDINGSDATE","CONFERENCE","TEAM",
    "G","W","L","W_PCT","HOME_RECORD","ROAD_RECORD"]

    """
    endpoint = 'http://stats.nba.com/stats/scoreboardv2'
    payload = {
        'DayOffset': '0',
        'LeagueID': '00',
        'gameDate': date
    }
    response = utils.get_response(endpoint, payload)
    return {
        'EAST': response['EastConfStandingsByDay'],
        'WEST': response['WestConfStandingsByDay']
    }


def team_leaders_from_date(date):
    """
    return statistical leaders for teams that play on given date
    args:
        date (string): format=mm/dd/yyyy
    returns:
        teams (list): teams that played on the given date and their statistical
            leaders

    each team is a dict with the following available keys
    ["GAME_ID","TEAM_ID","TEAM_CITY","TEAM_NICKNAME","TEAM_ABBREVIATION",
    "PTS_PLAYER_ID","PTS_PLAYER_NAME","PTS","REB_PLAYER_ID","REB_PLAYER_NAME",
    "REB","AST_PLAYER_ID","AST_PLAYER_NAME","AST"]

    """
    endpoint = 'http://stats.nba.com/stats/scoreboardv2'
    payload = {
        'DayOffset': '0',
        'LeagueID': '00',
        'gameDate': date
    }
    response = utils.get_response(endpoint, payload)
    return response['TeamLeaders']


def team_game_log(team_id, season):
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


def play_by_play(game_id):
    """
    return play by play data for a given game
    args:
        game_id (int)
    returns:
        plays (list)

    each player is a dict with the following available keys
    ["GAME_ID","EVENTNUM","EVENTMSGTYPE","EVENTMSGACTIONTYPE","PERIOD",
    "WCTIMESTRING","PCTIMESTRING","HOMEDESCRIPTION","NEUTRALDESCRIPTION",
    "VISITORDESCRIPTION","SCORE","SCOREMARGIN","PERSON1TYPE","PLAYER1_ID",
    "PLAYER1_NAME","PLAYER1_TEAM_ID","PLAYER1_TEAM_CITY",
    "PLAYER1_TEAM_NICKNAME","PLAYER1_TEAM_ABBREVIATION","PERSON2TYPE",
    "PLAYER2_ID","PLAYER2_NAME","PLAYER2_TEAM_ID","PLAYER2_TEAM_CITY",
    "PLAYER2_TEAM_NICKNAME","PLAYER2_TEAM_ABBREVIATION","PERSON3TYPE",
    "PLAYER3_ID","PLAYER3_NAME","PLAYER3_TEAM_ID","PLAYER3_TEAM_CITY",
    "PLAYER3_TEAM_NICKNAME","PLAYER3_TEAM_ABBREVIATION"]

    """
    endpoint = 'http://stats.nba.com/stats/playbyplayv2'
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


def boxscore(game_id):
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
        "GameID": game_id
        "StartPeriod": 1,
        "EndPeriod": 10
        }
    response = utils.get_response(endpoint, payload)
    return response['PlayByPlay']


def player_tracking_from_game(game_id):
    """
    return player tracking information for a given game
    args:
        game_id (int)
    returns:
        players (list): players that played in given game and their 
            tracking information

    each player is a dict with the following available keys
    ["GAME_ID","TEAM_ID","TEAM_ABBREVIATION","TEAM_CITY","PLAYER_ID",
    "PLAYER_NAME","START_POSITION","COMMENT","MIN","SPD","DIST","ORBC",
    "DRBC","RBC","TCHS","SAST","FTAST","PASS","AST","CFGM","CFGA",
    "CFG_PCT","UFGM","UFGA","UFG_PCT","FG_PCT","DFGM","DFGA","DFG_PCT"]

    """
    endpoint = 'http://stats.nba.com/stats/boxscoreplayertrackv2'
    payload = {
        'GameID': game_id,
    }
    response = utils.get_response(endpoint, payload)
    return response['PlayerTrack']


def all_players_stats(season):
    # TODO all users to specify what type of stats
    """
    return basic stats for all players in a season
    args:
        season: format ex: '1999-00', also accepts 1999 or 99
    returns:
        players (list): players and their stats for the season

    each player is a dict with the following available keys
    ["PLAYER_ID","PLAYER_NAME","TEAM_ID","TEAM_ABBREVIATION","GP","W","L",
    "W_PCT","MIN","FGM","FGA","FG_PCT","FG3M","FG3A","FG3_PCT","FTM","FTA",
    "FT_PCT","OREB","DREB","REB","AST","TOV","STL","BLK","BLKA","PF","PFD",
    "PTS","PLUS_MINUS","DD2","TD3","CFID","CFPARAMS"]

    """
    endpoint = 'http://stats.nba.com/stats/leaguedashplayerstats'
    payload = {
        "MeasureType":"Base",
        "PerMode":"PerGame",
        "PlusMinus":"N",
        "PaceAdjust":"N",
        "Rank":"N",
        "LeagueID":"00",
        "Season":utils.cleanse_season(season),
        "SeasonType":"Regular Season",
        "Outcome": None,
        "Location": None,
        "Month":0,
        "SeasonSegment": None,
        "DateFrom": None,
        "DateTo": None,
        "OpponentTeamID":0,
        "VsConference": None,
        "VsDivision": None,
        "GameSegment": None,
        "Period":0,
        "LastNGames":0,
        "GameScope": None,
        "PlayerExperience": None,
        "PlayerPosition": None,
        "StarterBench": None
    }
    response = utils.get_response(endpoint, payload)
    # TODO get corrent name
    return response['LeagueDashPlayerStats']


def all_teams_stats(season): 
    # TODO all users to specify what type of stats
    """
    return basic stats for all teams in a season
    args:
        season: format ex: '1999-00', also accepts 1999 or 99
    returns:
        teams (list): teams and their stats for the season

    each team is a dict with the following available keys
    ["TEAM_ID","TEAM_NAME","GP","W","L","W_PCT","MIN","FGM","FGA","FG_PCT",
    "FG3M","FG3A","FG3_PCT","FTM","FTA","FT_PCT","OREB","DREB","REB","AST",
    "TOV","STL","BLK","BLKA","PF","PFD","PTS","PLUS_MINUS","CFID","CFPARAMS"]

    """
    endpoint = 'http://stats.nba.com/stats/leaguedashteamstats'
    payload = {
        "MeasureType":"Base",
        "PerMode":"PerGame",
        "PlusMinus":"N",
        "PaceAdjust":"N",
        "Rank":"N",
        "LeagueID":"00",
        "Season":utils.cleanse_season(season),
        "SeasonType":"Regular Season",
        "Outcome": None,
        "Location": None,
        "Month":0,
        "SeasonSegment": None,
        "DateFrom": None,
        "DateTo": None,
        "OpponentTeamID":0,
        "VsConference": None,
        "VsDivision": None,
        "GameSegment": None,
        "Period":0,
        "LastNGames":0,
        "GameScope": None,
        "PlayerExperience": None,
        "PlayerPosition": None,
        "StarterBench": None
    }
    response = utils.get_response(endpoint, payload)
    return response['LeagueDashTeamStats']


def player_game_shot_chart(game_id, team_id, player_id):
    # TODO check to make sure correct 
    """
    return player tracking information for a given game
    args:
        game_id (int)
        #TODO get team_id from player_id
        team_id (int)
        player_id (int)
    returns:
        shots (list): shots a player attempted during a game

    each player is a dict with the following available keys
    ["GRID_TYPE","GAME_ID","GAME_EVENT_ID","PLAYER_ID","PLAYER_NAME","TEAM_ID",
    "TEAM_NAME","PERIOD","MINUTES_REMAINING","SECONDS_REMAINING","EVENT_TYPE",
    "ACTION_TYPE","SHOT_TYPE","SHOT_ZONE_BASIC","SHOT_ZONE_AREA",
    "SHOT_ZONE_RANGE","SHOT_DISTANCE","LOC_X","LOC_Y","SHOT_ATTEMPTED_FLAG",
    "SHOT_MADE_FLAG"]

    """
    endpoint = 'http://stats.nba.com/stats/shotchartdetail'
    payload = {
        "LeagueID": "00",
        #see if need season or can get from game_id
        "Season": "2014-15",
        "SeasonType": "Regular Season",
        "TeamID": team_id,
        "PlayerID": player_id,
        "GameID": game_id,
        "Outcome": None,
        "Location": None,
        "Month": 0,
        "SeasonSegment": None,
        "DateFrom": None,
        "DateTo": None,
        "OpponentTeamID": 0,
        "VsConference": None,
        "VsDivision": None,
        "Position": None,
        "RookieYear": None,
        "GameSegment": None,
        "Period": 0,
        "LastNGames": 0,
        "ClutchTime": None,
        "AheadBehind": None,
        "PointDiff": None,
        "RangeType": 2,
        "StartPeriod": 1,
        "EndPeriod": 10,
        "StartRange": 0,
        "EndRange": 28800,
        "ContextFilter": "",
        "ContextMeasure": "FGA"
    }
    response = utils.get_response(endpoint, payload)
    return response['Shot_Chart_Detail']


def player_info(player_id):
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


def player_game_log(player_id, season):
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


def league_leaders(season):
    # TODO document
    endpoint = 'http://stats.nba.com/stats/leagueleaders'
    payload = {
        "LeagueID": "00",
        "PerMode": "PerGame",
        "StatCategory": "PTS",
        "Season": util.cleanse_season(season),
        "SeasonType": "Regular Season",
        "Scope": "S"
    }
    response = utils.get_response(endpoint, payload)
    return response['LeagueLeaders']


def league_lineups(season):
    """
    return lineups that have played in given season
    args:
        season: format ex: '1999-00', also accepts 1999 or 99
    returns:
        lineups (list): lineups that have played in the season

    each lineup is a dict with the following available keys
    ["GROUP_SET","GROUP_ID","GROUP_NAME","TEAM_ID","TEAM_ABBREVIATION","GP",
    "W","L","W_PCT","MIN","FGM","FGA","FG_PCT","FG3M","FG3A","FG3_PCT","FTM",
    "FTA","FT_PCT","OREB","DREB","REB","AST","TOV","STL","BLK","BLKA","PF",
    "PFD","PTS","PLUS_MINUS"]

    """
    endpoint = 'http://stats.nba.com/stats/leaguedashlineups'
    payload = {
        "MeasureType": "Base",
        "PerMode": "PerGame",
        "PlusMinus": "N",
        "PaceAdjust": "N",
        "Rank": "N",
        "LeagueID": "00",
        "Season": util.cleanse_season(season),
        "SeasonType": "Regular Season",
        "Outcome": None,
        "Location": None,
        "Month": 0,
        "SeasonSegment": None,
        "DateFrom": None,
        "DateTo": None,
        "OpponentTeamID": 0,
        "VsConference": None,
        "VsDivision": None,
        "GameSegment": None,
        "Period": 0,
        "LastNGames": 0,
        "GroupQuantity": 5
    }
    response = utils.get_response(endpoint, payload)
    return response['Lineups']


def team_info(team_id, season):
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


def team_roster(team_id, season):
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


def team_coaching_staff(team_id, season):
    """
    return a given team's coaching staff
    args:
        team_id (int)
        season: format ex: '1999-00', also accepts 1999 or 99
    returns:
        coaches (list): 

    each coach is a dict with the following available keys
    ["TEAM_ID","SEASON","COACH_ID","FIRST_NAME","LAST_NAME","COACH_NAME",
    "COACH_CODE","IS_ASSISTANT","COACH_TYPE","SCHOOL","SORT_SEQUENCE"]

    """
    endpoint = 'http://stats.nba.com/stats/commonteamroster'
    payload = {
        "TeamID": team_id,
        "LeagueID": "00",
        "Season": utils.cleanse_season(season)
    }
    response = utils.get_response(endpoint, payload)
    return response['CommonTeamRoster']


def player_shot_log(player_id):
    # TODO expand possible args
    """
    return shots player has taken
    args:
        player_id (int)
    returns:
        shots (list): shots a player has taken

    each shot is a dict with the following available keys
    ["GAME_ID","MATCHUP","LOCATION","W","FINAL_MARGIN","SHOT_NUMBER",
    "PERIOD","GAME_CLOCK","SHOT_CLOCK","DRIBBLES","TOUCH_TIME","SHOT_DIST",
    "PTS_TYPE","SHOT_RESULT","CLOSEST_DEFENDER",
    "CLOSEST_DEFENDER_PLAYER_ID","CLOSE_DEF_DIST","FGM","PTS"]

    """
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
    return response['PtShotLog']


def player_rebound_log(player_id):
    # TODO allow extra args
    """
    return rebounds player has grabbed
    args:
        player_id (int)
    returns:
        rebounds (list): rebounds a player has grabbed

    each rebound is a dict with the following available keys
    ["GAME_ID","MATCHUP","LOCATION","W","FINAL_MARGIN","REB_NUMBER",
    "PERIOD","GAME_CLOCK","REB_TYPE","CONTESTED","NUM_CONTESTED",
    "REB_DIST","SHOOTER","SHOOTER_PLAYER_ID","SHOT_TYPE","SHOT_DIST",
    "OREB","DREB","REB"]

    """
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
    return response['PtRebLog']


def all_players(season, all_time=False):
    """
    return all players
    args:
        season: format ex: '1999-00', also accepts 1999 or 99
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
