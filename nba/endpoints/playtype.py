from nba import utils

'''
available methods
    player_transition_data
    player_cut_data
    player_pr_ball_handler_data
    player_handoff_data
    player_isolation_data
    player_misc_data
    player_post_up_data
    player_pr_roll_data
    player_spotup_data
TODO
    player_screen_data
    player_rebound_data
    team_transition_data
    team_cut_data
    team_pr_ball_handler_data
    team_handoff_data
    team_isolation_data
    team_misc_data
    team_screen_data
    team_post_up_data
    team_rebound_data
    team_pr_roll_data
    team_spotup_data

'''

def player_transition_data():
    """
    returns synergy transition data for all players this season
    returns:
        players (list): transition data for all players

    each player is a dict with the following available keys
    ["PlayerIDSID","PlayerFirstName","PlayerLastName","PlayerNumber","P",
    "TeamIDSID","TeamName","TeamNameAbbreviation","TeamShortName","GP","Poss",
    "Time","Points","FGA","FGM","PPP","WorsePPP","BetterPPP","PossG","PPG",
    "FGAG","FGMG","FGmG","FGm","FG","aFG","FT","TO","SF","PlusOne","Score"]

    """
    endpoint = 'http://stats.nba.com/js/data/playtype/player_Transition.js'
    response = utils.get_response(endpoint, None)
    return response['Offensive']


def player_cut_data():
    """
    returns synergy cut data for all players this season
    returns:
        players (list): cut data for all players

    each player is a dict with the following available keys
    ["PlayerIDSID","PlayerFirstName","PlayerLastName","PlayerNumber","P",
    "TeamIDSID","TeamName","TeamNameAbbreviation","TeamShortName","GP","Poss",
    "Time","Points","FGA","FGM","PPP","WorsePPP","BetterPPP","PossG","PPG",
    "FGAG","FGMG","FGmG","FGm","FG","aFG","FT","TO","SF","PlusOne","Score"]

    """
    endpoint = 'http://stats.nba.com/js/data/playtype/player_Cut.js'
    response = utils.get_response(endpoint, None)
    return response['Offensive']


def player_handoff_data():
    """
    returns synergy handler data for all players this season
    returns:
        players (list): handler data for all players

    each player is a dict with the following available keys
    ["GP","Poss","Time","Points","FGA","FGM","PPP","WorsePPP","BetterPPP",
    "PlayerIDSID","PlayerFirstName","PlayerLastName","PlayerNumber","P",
    "TeamIDSID","TeamName","TeamNameAbbreviation","TeamShortName","PossG",
    "PPG","FGAG","FGMG","FGmG","FGm","FG","aFG","FT","TO","SF","PlusOne",
    "Score"]

    """
    endpoint = 'http://stats.nba.com/js/data/playtype/player_Handoff.js'
    response = utils.get_response(endpoint, None)
    return response['Offensive']


def player_pnr_handler_data():
    """
    returns synergy PnR ball handler data for all players this season
    returns:
        players (list): data for all players

    each player is a dict with the following available keys
    ["PlayerIDSID","PlayerFirstName","PlayerLastName","PlayerNumber","P",
    "TeamIDSID","TeamName","TeamNameAbbreviation","TeamShortName","GP","Poss",
    "Time","Points","FGA","FGM","PPP","WorsePPP","BetterPPP","PossG","PPG",
    "FGAG","FGMG","FGmG","FGm","FG","aFG","FT","TO","SF","PlusOne","Score"]

    """
    endpoint = 'http://stats.nba.com/js/data/playtype/player_PRBallHandler.js'
    response = utils.get_response(endpoint, None)
    return response['Offensive']


def player_isolation_data():
    """
    returns synergy isolation data for all players this season
    returns:
        players (list): isolation data for all players

    each player is a dict with the following available keys
    ["GP","Poss","Time","Points","FGA","FGM","PPP","WorsePPP","BetterPPP",
    "PlayerIDSID","PlayerFirstName","PlayerLastName","PlayerNumber","P",
    "TeamIDSID","TeamName","TeamNameAbbreviation","TeamShortName","PossG",
    "PPG","FGAG","FGMG","FGmG","FGm","FG","aFG","FT","TO","SF","PlusOne",
    "Score"]

    """
    endpoint = 'http://stats.nba.com/js/data/playtype/player_Isolation.js'
    response = utils.get_response(endpoint, None)
    return response['Offensive']


def player_misc_data():
    """
    returns synergy misc data for all players this season
    returns:
        players (list): misc data for all players

    each player is a dict with the following available keys
    ["PlayerFirstName","PlayerLastName","PlayerNumber","P","TeamIDSID",
    "TeamName","TeamNameAbbreviation","TeamShortName","GP","Poss","Time",
    "Points","FGA","FGM","PPP","WorsePPP","BetterPPP","PlayerIDSID","PossG",
    "PPG","FGAG","FGMG","FGmG","FGm","FG","aFG","FT","TO","SF","PlusOne",
    "Score"]

    """
    endpoint = 'http://stats.nba.com/js/data/playtype/player_Misc.js'
    response = utils.get_response(endpoint, None)
    return response['Offensive']


def player_postup_data():
    """
    returns synergy postup data for all players this season
    returns:
        players (list): postup data for all players

    each player is a dict with the following available keys
    ["PlayerIDSID","PlayerFirstName","PlayerLastName","PlayerNumber","P",
    "TeamIDSID","TeamName","TeamNameAbbreviation","TeamShortName","GP","Poss",
    "Time","Points","FGA","FGM","PPP","WorsePPP","BetterPPP","PossG","PPG",
    "FGAG","FGMG","FGmG","FGm","FG","aFG","FT","TO","SF","PlusOne","Score"]

    """
    endpoint = 'http://stats.nba.com/js/data/playtype/player_Postup.js'
    response = utils.get_response(endpoint, None)
    return response['Offensive']


def player_pnr_roll_data():
    """
    returns synergy PnR roll data for all players this season
    returns:
        players (list): PnR roll data for all players

    each player is a dict with the following available keys
    ["PlayerIDSID","PlayerFirstName","PlayerLastName","PlayerNumber","P",
    "TeamIDSID","TeamName","TeamNameAbbreviation","TeamShortName","GP","Poss",
    "Time","Points","FGA","FGM","PPP","WorsePPP","BetterPPP","PossG","PPG",
    "FGAG","FGMG","FGmG","FGm","FG","aFG","FT","TO","SF","PlusOne","Score"]

    """
    endpoint = 'http://stats.nba.com/js/data/playtype/player_PRRollMan.js'
    response = utils.get_response(endpoint, None)
    return response['Offensive']

def player_spotup_data():
    """
    returns synergy spotup data for all players this season
    returns:
        players (list): spotup data for all players

    each player is a dict with the following available keys
    ["PlayerFirstName","PlayerLastName","PlayerNumber","P","TeamIDSID",
    "TeamName","TeamNameAbbreviation","TeamShortName","GP","Poss","Time",
    "Points","FGA","FGM","PPP","WorsePPP","BetterPPP","PlayerIDSID","PossG",
    "PPG","FGAG","FGMG","FGmG","FGm","FG","aFG","FT","TO","SF","PlusOne",
    "Score"]

    """
    endpoint = 'http://stats.nba.com/js/data/playtype/player_Spotup.js'
    response = utils.get_response(endpoint, None)
    return response['Offensive']