import utils

'''
available methods
    team_drive_data
    team_defense_data
    team_catch_shoot_data
    team_catch_shoot_data
    team_speed_data
    team_shooting_data
    team_rebounding_data


'''

def team_drive_data(season):
    """
    returns sportsvu driving data for all teams
    args:
        season
    returns:
        teams (list): driving data for all teams

    each game is a dict with the following available keys
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

    each game is a dict with the following available keys
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

    each game is a dict with the following available keys
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

    each game is a dict with the following available keys
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

    each game is a dict with the following available keys
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


def team_pull_up_data(season):
    """
    returns sportsvu pull up shooting data for all teams
    args:
        season
    returns:
        teams (list): pull up shooting data for all teams

    each game is a dict with the following available keys
    ["TEAM_ID","TEAM_CITY","TEAM_NAME","TEAM_ABBREVIATION","TEAM_CODE","GP",
    "MIN","PTS","FGM","FGA","FG_PCT","FG3M","FG3A","FG3_PCT","EFG_PCT",
    "PTS_TOT"]

    """
    endpoint = 'http://stats.nba.com/js/data/sportvu/%s/pullUpShootTeamData.json' % util.season_to_int(season)
    response = utils.get_response(endpoint, None)
    return response['TeamTrackingReboundingStats']


def team_defense_data(season):
    """
    returns sportsvu defense data for all teams
    args:
        season
    returns:
        teams (list): defense data for all teams

    each game is a dict with the following available keys
    ["TEAM_ID","TEAM_CITY","TEAM_NAME","TEAM_ABBREVIATION","TEAM_CODE","GP",
    "MIN","BLK","STL","FGM_DEFEND_RIM","FGA_DEFEND_RIM","FGP_DEFEND_RIM",
    "BLK_TOT"]

    """
    endpoint = 'http://stats.nba.com/js/data/sportvu/%s/defenseTeamData.json' % util.season_to_int(season)
    response = utils.get_response(endpoint, None)
    return response['TeamTrackingDefenseStats']

def team_defense_data(season):
    """
    returns sportsvu defense data for all teams
    args:
        season
    returns:
        teams (list): defense data for all teams

    each game is a dict with the following available keys
    ["TEAM_ID","TEAM_CITY","TEAM_NAME","TEAM_ABBREVIATION","TEAM_CODE","GP",
    "MIN","BLK","STL","FGM_DEFEND_RIM","FGA_DEFEND_RIM","FGP_DEFEND_RIM",
    "BLK_TOT"]

    """
    endpoint = 'http://stats.nba.com/js/data/sportvu/%s/defenseTeamData.json' % util.season_to_int(season)
    response = utils.get_response(endpoint, None)
    return response['TeamTrackingDefenseStats']

def team_defense_data(season):
    """
    returns sportsvu defense data for all teams
    args:
        season
    returns:
        teams (list): defense data for all teams

    each game is a dict with the following available keys
    ["TEAM_ID","TEAM_CITY","TEAM_NAME","TEAM_ABBREVIATION","TEAM_CODE","GP",
    "MIN","BLK","STL","FGM_DEFEND_RIM","FGA_DEFEND_RIM","FGP_DEFEND_RIM",
    "BLK_TOT"]

    """
    endpoint = 'http://stats.nba.com/js/data/sportvu/%s/defenseTeamData.json' % util.season_to_int(season)
    response = utils.get_response(endpoint, None)
    return response['TeamTrackingDefenseStats']