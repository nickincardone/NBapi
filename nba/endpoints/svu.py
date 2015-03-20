from nba import utils

'''
available methods
    team_drive_data
    team_defense_data
    team_catch_shoot_data
    team_catch_shoot_data
    team_speed_data
    team_shooting_data
    team_rebounding_data
    team_pull_up_data
    team_touches_data
    team_passing_data

    player_drive_data
    player_defense_data
    player_catch_shoot_data
    player_catch_shoot_data
    player_speed_data
    player_shooting_data
    player_rebounding_data
    player_pull_up_data
    player_touches_data
    player_passing_data

'''

# TODO verify all these, coded on a plane

def team_drive_data(season):
    """
    returns sportsvu driving data for all teams
    args:
        season
    returns:
        teams (list): driving data for all teams

    each team is a dict with the following available keys
    ["TEAM_ID","TEAM_CITY","TEAM_NAME","TEAM_ABBREVIATION","TEAM_CODE","GP",
    "MIN","DVS","DPP","DTP","FG_PCT","PTS_48","DPP_TOT","DVS_TOT"]

    """
    endpoint = 'http://stats.nba.com/js/data/sportvu/%s/drivesTeamData.json' % util.season_to_int(season)
    response = utils.get_response(endpoint, None)
    return response['TeamTrackingDrivesStats']


def team_defense_data(season):
    """
    returns sportsvu defense data for all teams
    args:
        season
    returns:
        teams (list): defense data for all teams

    each team is a dict with the following available keys
    ["TEAM_ID","TEAM_CITY","TEAM_NAME","TEAM_ABBREVIATION","TEAM_CODE","GP",
    "MIN","BLK","STL","FGM_DEFEND_RIM","FGA_DEFEND_RIM","FGP_DEFEND_RIM",
    "BLK_TOT"]

    """
    endpoint = 'http://stats.nba.com/js/data/sportvu/%s/defenseTeamData.json' % util.season_to_int(season)
    response = utils.get_response(endpoint, None)
    return response['TeamTrackingDefenseStats']


def team_catch_shoot_data(season):
    """
    returns sportsvu catch and shoot data for all teams
    args:
        season
    returns:
        teams (list): catch and shoot data for all teams

    each team is a dict with the following available keys
    ["TEAM_ID","TEAM_CITY","TEAM_NAME","TEAM_ABBREVIATION","TEAM_CODE","GP",
    "MIN","PTS","FGM","FGA","FG_PCT","FG3M","FG3A","FG3_PCT","EFG_PCT",
    "PTS_TOT"]

    """
    endpoint = 'http://stats.nba.com/js/data/sportvu/%s/catchShootTeamData.json' % util.season_to_int(season)
    response = utils.get_response(endpoint, None)
    return response['TeamTrackingCatchShootStats']


def team_speed_data(season):
    """
    returns sportsvu speed data for all teams
    args:
        season
    returns:
        teams (list): speed data for all teams

    each team is a dict with the following available keys
    ["TEAM_ID","TEAM_CITY","TEAM_NAME","TEAM_ABBREVIATION","TEAM_CODE","GP",
    "MIN","DIST","AV_SPD","DIST_PG","DIST_48","DIST_OFF","DIST_DEF",
    "AV_SPD_OFF","AV_SPD_DEF"]

    """
    endpoint = 'http://stats.nba.com/js/data/sportvu/%s/speedTeamData.json' % util.season_to_int(season)
    response = utils.get_response(endpoint, None)
    return response['TeamTrackingSpeedStats']


def team_shooting_data(season):
    """
    returns sportsvu shooting data for all teams
    args:
        season
    returns:
        teams (list): shooting data for all teams

    each team is a dict with the following available keys
    ["TEAM_ID","TEAM_CITY","TEAM_NAME","TEAM_ABBREVIATION","TEAM_CODE","GP",
    "MIN","PTS","PTS_DRIVE","FGP_DRIVE","PTS_CLOSE","FGP_CLOSE",
    "PTS_CATCH_SHOOT","FGP_CATCH_SHOOT","PTS_PULL_UP","FGP_PULL_UP",
    "FGA_DRIVE","FGA_CLOSE","FGA_CATCH_SHOOT","FGA_PULL_UP","EFG_PCT",
    "CFGM","CFGA","CFGP","UFGM","UFGA","UFGP","CFG3M","CFG3A","CFG3P",
    "UFG3M","UFG3A","UFG3P"]

    """
    endpoint = 'http://stats.nba.com/js/data/sportvu/%s/shootingTeamData.json' % util.season_to_int(season)
    response = utils.get_response(endpoint, None)
    return response['TeamTrackingShootingEfficiencyStats']


def team_rebounding_data(season):
    """
    returns sportsvu rebounding data for all teams
    args:
        season
    returns:
        teams (list): rebounding data for all teams

    each team is a dict with the following available keys
    ["TEAM_ID","TEAM_CITY","TEAM_NAME","TEAM_ABBREVIATION","TEAM_CODE","GP",
    "MIN","REB","REB_CHANCE","REB_COL_PCT","REB_CONTESTED","REB_UNCONTESTED",
    "REB_UNCONTESTED_PCT","REB_TOT","OREB","OREB_CHANCE","OREB_COL_PCT",
    "OREB_CONTESTED","OREB_UNCONTESTED","OREB_UNCONTESTED_PCT","DREB",
    "DREB_CHANCE","DREB_COL_PCT","DREB_CONTESTED","DREB_UNCONTESTED",
    "DREB_UNCONTESTED_PCT"]

    """
    endpoint = 'http://stats.nba.com/js/data/sportvu/%s/reboundingTeamData.json' % util.season_to_int(season)
    response = utils.get_response(endpoint, None)
    return response['TeamTrackingReboundingStats']


def team_pull_up_data(season):
    """
    returns sportsvu pull up shooting data for all teams
    args:
        season
    returns:
        teams (list): pull up shooting data for all teams

    each team is a dict with the following available keys
    ["TEAM_ID","TEAM_CITY","TEAM_NAME","TEAM_ABBREVIATION","TEAM_CODE","GP",
    "MIN","PTS","FGM","FGA","FG_PCT","FG3M","FG3A","FG3_PCT","EFG_PCT",
    "PTS_TOT"]

    """
    endpoint = 'http://stats.nba.com/js/data/sportvu/%s/pullUpShootTeamData.json' % util.season_to_int(season)
    response = utils.get_response(endpoint, None)
    return response['TeamTrackingPullUpShootStats']


def team_touches_data(season):
    """
    returns sportsvu touches data for all teams
    args:
        season
    returns:
        teams (list): touches data for all teams

    each team is a dict with the following available keys
    ["TEAM_ID","TEAM_CITY","TEAM_NAME","TEAM_ABBREVIATION","TEAM_CODE","GP",
    "MIN","TCH","FC_TCH","TOP","CL_TCH","EL_TCH","PTS","PTS_TCH","PTS_HCCT",
    "TCH_TOT"]

    """
    endpoint = 'http://stats.nba.com/js/data/sportvu/%s/touchesTeamData.json' % util.season_to_int(season)
    response = utils.get_response(endpoint, None)
    return response['TeamTrackingTouchesStats']


def team_passing_data(season):
    """
    returns sportsvu passing data for all teams
    args:
        season
    returns:
        teams (list): passing data for all teams

    each team is a dict with the following available keys
    ["TEAM_ID","TEAM_CITY","TEAM_NAME","TEAM_ABBREVIATION","TEAM_CODE","GP",
    "MIN","PASS","AST","AST_FT","AST_SEC","AST_POT","PTS_CRT","PTS_CRT_48",
    "AST_TOT"]

    """
    endpoint = 'http://stats.nba.com/js/data/sportvu/%s/passingTeamData.json' % util.season_to_int(season)
    response = utils.get_response(endpoint, None)
    return response['TeamTrackingPassingStats']


def player_drive_data(season):
    """
    returns sportsvu driving data for all players
    args:
        season
    returns:
        players (list): driving data for all players

    each player is a dict with the following available keys
    ["PLAYER_ID","PLAYER","FIRST_NAME","LAST_NAME","TEAM_ABBREVIATION","GP",
    "MIN","DVS","DPP","DTP","FG_PCT","PTS_48","DPP_TOT","DVS_TOT"]

    """
    endpoint = 'http://stats.nba.com/js/data/sportvu/%s/drivesData.json' % util.season_to_int(season)
    response = utils.get_response(endpoint, None)
    return response['PlayerTrackingDrivesStats']


def player_defense_data(season):
    """
    returns sportsvu defense data for all players
    args:
        season
    returns:
        players (list): defense data for all players

    each player is a dict with the following available keys
    ["PLAYER_ID","PLAYER","FIRST_NAME","LAST_NAME","TEAM_ABBREVIATION","GP",
    "MIN","BLK","STL","FGM_DEFEND_RIM","FGA_DEFEND_RIM","FGP_DEFEND_RIM",
    "BLK_TOT"]

    """
    endpoint = 'http://stats.nba.com/js/data/sportvu/%s/defenseData.json' % util.season_to_int(season)
    response = utils.get_response(endpoint, None)
    return response['PlayerTrackingDefenseStats']


def player_catch_shoot_data(season):
    """
    returns sportsvu catch and shoot data for all players
    args:
        season
    returns:
        players (list): catch and shoot data for all players

    each player is a dict with the following available keys
    ["PLAYER_ID","PLAYER","FIRST_NAME","LAST_NAME","TEAM_ABBREVIATION","GP",
    "MIN","PTS","FGM","FGA","FG_PCT","FG3M","FG3A","FG3_PCT","EFG_PCT",
    "PTS_TOT"]

    """
    endpoint = 'http://stats.nba.com/js/data/sportvu/%s/catchShootData.json' % util.season_to_int(season)
    response = utils.get_response(endpoint, None)
    return response['PlayerTrackingCatchShootStats']


def player_speed_data(season):
    """
    returns sportsvu speed data for all players
    args:
        season
    returns:
        players (list): speed data for all players

    each player is a dict with the following available keys
    ["PLAYER_ID","PLAYER","FIRST_NAME","LAST_NAME","TEAM_ABBREVIATION","GP",
    "MIN","DIST","AV_SPD","DIST_PG","DIST_48","DIST_OFF","DIST_DEF",
    "AV_SPD_OFF","AV_SPD_DEF"]

    """
    endpoint = 'http://stats.nba.com/js/data/sportvu/%s/speedData.json' % util.season_to_int(season)
    response = utils.get_response(endpoint, None)
    return response['PlayerTrackingSpeedStats']


def player_shooting_data(season):
    """
    returns sportsvu shooting data for all players
    args:
        season
    returns:
        players (list): shooting data for all players

    each player is a dict with the following available keys
    ["PLAYER_ID","PLAYER","FIRST_NAME","LAST_NAME","TEAM_ABBREVIATION","GP",
    "MIN","PTS","PTS_DRIVE","FGP_DRIVE","PTS_CLOSE","FGP_CLOSE",
    "PTS_CATCH_SHOOT","FGP_CATCH_SHOOT","PTS_PULL_UP","FGP_PULL_UP",
    "FGA_DRIVE","FGA_CLOSE","FGA_CATCH_SHOOT","FGA_PULL_UP","EFG_PCT","CFGM",
    "CFGA","CFGP","UFGM","UFGA","UFGP","CFG3M","CFG3A","CFG3P","UFG3M",
    "UFG3A","UFG3P"]

    """
    endpoint = 'http://stats.nba.com/js/data/sportvu/%s/shootingData.json' % util.season_to_int(season)
    response = utils.get_response(endpoint, None)
    return response['PlayerTrackingShootingEfficiencyStats']


def player_rebounding_data(season):
    """
    returns sportsvu rebounding data for all players
    args:
        season
    returns:
        players (list): rebounding data for all players

    each player is a dict with the following available keys
    ["PLAYER_ID","PLAYER","FIRST_NAME","LAST_NAME","TEAM_ABBREVIATION","GP",
    "MIN","REB","REB_CHANCE","REB_COL_PCT","REB_CONTESTED","REB_UNCONTESTED",
    "REB_UNCONTESTED_PCT","REB_TOT","OREB","OREB_CHANCE","OREB_COL_PCT",
    "OREB_CONTESTED","OREB_UNCONTESTED","OREB_UNCONTESTED_PCT","DREB",
    "DREB_CHANCE","DREB_COL_PCT","DREB_CONTESTED","DREB_UNCONTESTED",
    "DREB_UNCONTESTED_PCT"]

    """
    endpoint = 'http://stats.nba.com/js/data/sportvu/%s/reboundingData.json' % util.season_to_int(season)
    response = utils.get_response(endpoint, None)
    return response['PlayerTrackingReboundingStats']


def player_pull_up_data(season):
    """
    returns sportsvu pull up shooting data for all players
    args:
        season
    returns:
        players (list): pull up shooting data for all players

    each player is a dict with the following available keys
    ["PLAYER_ID","PLAYER","FIRST_NAME","LAST_NAME","TEAM_ABBREVIATION","GP",
    "MIN","PTS","FGM","FGA","FG_PCT","FG3M","FG3A","FG3_PCT","EFG_PCT",
    "PTS_TOT"]

    """
    endpoint = 'http://stats.nba.com/js/data/sportvu/%s/pullUpShootData.json' % util.season_to_int(season)
    response = utils.get_response(endpoint, None)
    return response['PlayerTrackingPullUpShootStats']


def player_touches_data(season):
    """
    returns sportsvu touches data for all players
    args:
        season
    returns:
        players (list): touches data for all players

    each player is a dict with the following available keys
    ["PLAYER_ID","PLAYER","FIRST_NAME","LAST_NAME","TEAM_ABBREVIATION","GP",
    "MIN","TCH","FC_TCH","TOP","CL_TCH","EL_TCH","PTS","PTS_TCH","PTS_HCCT",
    "TCH_TOT"]

    """
    endpoint = 'http://stats.nba.com/js/data/sportvu/%s/touchesData.json' % util.season_to_int(season)
    response = utils.get_response(endpoint, None)
    return response['PlayerTrackingTouchesStats']


def player_passing_data(season):
    """
    returns sportsvu passing data for all players
    args:
        season
    returns:
        players (list): passing data for all players

    each player is a dict with the following available keys
    ["PLAYER_ID","PLAYER","FIRST_NAME","LAST_NAME","TEAM_ABBREVIATION","GP",
    "MIN","PASS","AST","AST_FT","AST_SEC","AST_POT","PTS_CRT","PTS_CRT_48",
    "AST_TOT"]

    """
    endpoint = 'http://stats.nba.com/js/data/sportvu/%s/passingData.json' % util.season_to_int(season)
    response = utils.get_response(endpoint, None)
    return response['PlayerTrackingPassingStats']

