from nba import utils

'''
for player defensive endpoints the rowset name is 'Deffensive'*

available methods
    {team/player}_transition_off
    team_transition_def
    {team/player}_cut_off
    team_cut_def
    {team/player}_pnr_ball_handler_{off/def}
    {team/player}_handoff_{off/def}
    {team/player}_isolation_{off/def}
    {team/player}_misc_off
    team_misc_def
    {team/player}_postup_{off/def}
    {team/player}_pnr_roll_{off/def}
    {team/player}_spotup_{off/def}
    {team/player}_screen_{off/def}

'''

def player_transition_off():
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


def player_cut_off():
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


def player_handoff_off():
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


def player_pnr_handler_off():
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


def player_isolation_off():
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


def player_misc_off():
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


def player_postup_off():
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


def player_pnr_roll_off():
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


def player_spotup_off():
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


def player_off_rebound():
    """
    returns synergy off rebound data for all players this season
    returns:
        players (list): off rebound data for all players

    each player is a dict with the following available keys
    ["GP","Poss","Time","PlayerIDSID","PlayerFirstName","PlayerLastName",
    "PlayerNumber","P","TeamIDSID","TeamName","TeamNameAbbreviation",
    "TeamShortName","Points","FGA","FGM","PPP","WorsePPP","BetterPPP",
    "PossG","PPG","FGAG","FGMG","FGmG","FGm","FG","aFG","FT","TO","SF",
    "PlusOne","Score"]

    """
    endpoint = 'http://stats.nba.com/js/data/playtype/player_OffRebound.js'
    response = utils.get_response(endpoint, None)
    return response['Offensive']


def player_screen_off():
    """
    returns synergy off screen data for all players this season
    returns:
        players (list): all qualified player's off screen stats

    each player is a dict with the following available keys
    ["PlayerIDSID","PlayerFirstName","PlayerLastName","PlayerNumber","P",
    "TeamIDSID","TeamName","TeamNameAbbreviation","TeamShortName","GP","Poss",
    "Time","Points","FGA","FGM","PPP","WorsePPP","BetterPPP","PossG","PPG",
    "FGAG","FGMG","FGmG","FGm","FG","aFG","FT","TO","SF","PlusOne","Score"]

    """
    endpoint = 'http://stats.nba.com/js/data/playtype/player_OffScreen.js'
    response = utils.get_response(endpoint, None)
    return response['Offensive']


def player_handoff_def():
    """
    returns synergy handoff data for all players this season
    returns:
        players (list): handoff data for all players

    each player is a dict with the following available keys
    ["PlayerIDSID","PlayerFirstName","PlayerLastName","PlayerNumber","P",
    "TeamIDSID","TeamName","TeamNameAbbreviation","TeamShortName","GP","Poss",
    "Time","Points","FGA","FGM","PPP","WorsePPP","BetterPPP","PossG","PPG",
    "FGAG","FGMG","FGmG","FGm","FG","aFG","FT","TO","SF","PlusOne","Score"]

    """
    endpoint = 'http://stats.nba.com/js/data/playtype/player_Handoff.js'
    response = utils.get_response(endpoint, None)
    return response['Deffensive']


def player_pnr_handler_def():
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
    return response['Deffensive']


def player_isolation_def():
    """
    returns synergy isolation data for all players this season
    returns:
        players (list): isolation data for all players

    each player is a dict with the following available keys
    ["PlayerIDSID","PlayerFirstName","PlayerLastName","PlayerNumber","P",
    "TeamIDSID","TeamName","TeamNameAbbreviation","TeamShortName","GP","Poss",
    "Time","Points","FGA","FGM","PPP","WorsePPP","BetterPPP","PossG","PPG",
    "FGAG","FGMG","FGmG","FGm","FG","aFG","FT","TO","SF","PlusOne","Score"]

    """
    endpoint = 'http://stats.nba.com/js/data/playtype/player_Isolation.js'
    response = utils.get_response(endpoint, None)
    return response['Deffensive']


def player_postup_def():
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
    # yes there is a typo in the endpoint
    return response['Deffensive']


def player_pnr_roll_def():
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
    return response['Deffensive']


def player_spotup_def():
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
    return response['Deffensive']


def player_screen_def():
    """
    returns synergy off screen defense data for all players this season
    returns:
        players (list): all qualified player's off screen defense stats

    each player is a dict with the following available keys
    ["PlayerIDSID","PlayerFirstName","PlayerLastName","PlayerNumber","P",
    "TeamIDSID","TeamName","TeamNameAbbreviation","TeamShortName","GP","Poss",
    "Time","Points","FGA","FGM","PPP","WorsePPP","BetterPPP","PossG","PPG",
    "FGAG","FGMG","FGmG","FGm","FG","aFG","FT","TO","SF","PlusOne","Score"]

    """
    endpoint = 'http://stats.nba.com/js/data/playtype/player_OffScreen.js'
    response = utils.get_response(endpoint, None)
    # yes there is a typo in the endpoint
    return response['Deffensive']


def team_transition_off():
    """
    returns synergy transition data for all teams this season
    returns:
        teams (list): transition data for all teams

    each team is a dict with the following available keys
    ["TeamIDSID","TeamName","TeamNameAbbreviation","TeamShortName","GP","Poss",
    "Time","Points","FGA","FGM","PPP","WorsePPP","BetterPPP","PossG","PPG",
    "FGAG","FGMG","FGmG","FGm","FG","aFG","FT","TO","SF","PlusOne","Score"]

    """
    endpoint = 'http://stats.nba.com/js/data/playtype/team_Transition.js'
    response = utils.get_response(endpoint, None)
    return response['Offensive']


def team_cut_off():
    """
    returns synergy cut data for all teams this season
    returns:
        teams (list): cut data for all teams

    each team is a dict with the following available keys
    ["TeamIDSID","TeamName","TeamNameAbbreviation","TeamShortName","GP","Poss",
    "Time","Points","FGA","FGM","PPP","WorsePPP","BetterPPP","PossG","PPG",
    "FGAG","FGMG","FGmG","FGm","FG","aFG","FT","TO","SF","PlusOne","Score"]

    """
    endpoint = 'http://stats.nba.com/js/data/playtype/team_Cut.js'
    response = utils.get_response(endpoint, None)
    return response['Offensive']


def team_handoff_off():
    """
    returns synergy handler data for all teams this season
    returns:
        teams (list): handler data for all teams

    each team is a dict with the following available keys
    ["TeamIDSID","TeamName","TeamNameAbbreviation","TeamShortName","GP","Poss",
    "Time","Points","FGA","FGM","PPP","WorsePPP","BetterPPP","PossG","PPG",
    "FGAG","FGMG","FGmG","FGm","FG","aFG","FT","TO","SF","PlusOne","Score"]

    """
    endpoint = 'http://stats.nba.com/js/data/playtype/team_Handoff.js'
    response = utils.get_response(endpoint, None)
    return response['Offensive']


def team_pnr_handler_off():
    """
    returns synergy PnR ball handler data for all teams this season
    returns:
        teams (list): data for all teams

    each team is a dict with the following available keys
    ["TeamIDSID","TeamName","TeamNameAbbreviation","TeamShortName","GP","Poss",
    "Time","Points","FGA","FGM","PPP","WorsePPP","BetterPPP","PossG","PPG",
    "FGAG","FGMG","FGmG","FGm","FG","aFG","FT","TO","SF","PlusOne","Score"]

    """
    endpoint = 'http://stats.nba.com/js/data/playtype/team_PRBallHandler.js'
    response = utils.get_response(endpoint, None)
    return response['Offensive']


def team_isolation_off():
    """
    returns synergy isolation data for all teams this season
    returns:
        teams (list): isolation data for all teams

    each team is a dict with the following available keys
    ["TeamIDSID","TeamName","TeamNameAbbreviation","TeamShortName","GP","Poss",
    "Time","Points","FGA","FGM","PPP","WorsePPP","BetterPPP","PossG","PPG",
    "FGAG","FGMG","FGmG","FGm","FG","aFG","FT","TO","SF","PlusOne","Score"]

    """
    endpoint = 'http://stats.nba.com/js/data/playtype/team_Isolation.js'
    response = utils.get_response(endpoint, None)
    return response['Offensive']


def team_misc_off():
    """
    returns synergy misc data for all teams this season
    returns:
        teams (list): misc data for all teams

    each team is a dict with the following available keys
    ["TeamIDSID","TeamName","TeamNameAbbreviation","TeamShortName","GP","Poss",
    "Time","Points","FGA","FGM","PPP","WorsePPP","BetterPPP","PossG","PPG",
    "FGAG","FGMG","FGmG","FGm","FG","aFG","FT","TO","SF","PlusOne","Score"]

    """
    endpoint = 'http://stats.nba.com/js/data/playtype/team_Misc.js'
    response = utils.get_response(endpoint, None)
    return response['Offensive']


def team_postup_off():
    """
    returns synergy postup data for all teams this season
    returns:
        teams (list): postup data for all teams

    each team is a dict with the following available keys
    ["TeamIDSID","TeamName","TeamNameAbbreviation","TeamShortName","GP","Poss",
    "Time","Points","FGA","FGM","PPP","WorsePPP","BetterPPP","PossG","PPG",
    "FGAG","FGMG","FGmG","FGm","FG","aFG","FT","TO","SF","PlusOne","Score"]

    """
    endpoint = 'http://stats.nba.com/js/data/playtype/team_Postup.js'
    response = utils.get_response(endpoint, None)
    return response['Offensive']


def team_pnr_roll_off():
    """
    returns synergy PnR roll data for all teams this season
    returns:
        teams (list): PnR roll data for all teams

    each team is a dict with the following available keys
    ["TeamIDSID","TeamName","TeamNameAbbreviation","TeamShortName","GP","Poss",
    "Time","Points","FGA","FGM","PPP","WorsePPP","BetterPPP","PossG","PPG",
    "FGAG","FGMG","FGmG","FGm","FG","aFG","FT","TO","SF","PlusOne","Score"]

    """
    endpoint = 'http://stats.nba.com/js/data/playtype/team_PRRollMan.js'
    response = utils.get_response(endpoint, None)
    return response['Offensive']


def team_spotup_off():
    """
    returns synergy spotup data for all teams this season
    returns:
        teams (list): spotup data for all teams

    each team is a dict with the following available keys
    ["TeamIDSID","TeamName","TeamNameAbbreviation","TeamShortName","GP","Poss",
    "Time","Points","FGA","FGM","PPP","WorsePPP","BetterPPP","PossG","PPG",
    "FGAG","FGMG","FGmG","FGm","FG","aFG","FT","TO","SF","PlusOne","Score"]

    """
    endpoint = 'http://stats.nba.com/js/data/playtype/team_Spotup.js'
    response = utils.get_response(endpoint, None)
    return response['Offensive']


def team_off_rebound_off():
    """
    returns synergy off rebound data for all teams this season
    returns:
        teams (list): off rebound data for all teams

    each team is a dict with the following available keys
    ["TeamIDSID","TeamName","TeamNameAbbreviation","TeamShortName","GP","Poss",
    "Time","Points","FGA","FGM","PPP","WorsePPP","BetterPPP","PossG","PPG",
    "FGAG","FGMG","FGmG","FGm","FG","aFG","FT","TO","SF","PlusOne","Score"]

    """
    endpoint = 'http://stats.nba.com/js/data/playtype/team_OffRebound.js'
    response = utils.get_response(endpoint, None)
    return response['Offensive']


def team_screen_off():
    """
    returns synergy screen data for all teams this season
    returns:
        teams (list): defensive stats for off screen plays for all teams

    each team is a dict with the following available keys
    ["TeamIDSID","TeamName","TeamNameAbbreviation","TeamShortName","GP","Poss",
    "Time","Points","FGA","FGM","PPP","WorsePPP","BetterPPP","PossG","PPG",
    "FGAG","FGMG","FGmG","FGm","FG","aFG","FT","TO","SF","PlusOne","Score"]

    """
    endpoint = 'http://stats.nba.com/js/data/playtype/team_OffScreen.js'
    response = utils.get_response(endpoint, None)
    return response['Offensive']


def team_transition_def():
    """
    returns synergy transition data for all teams this season
    returns:
        teams (list): transition data for all teams

    each team is a dict with the following available keys
    ["TeamIDSID","TeamName","TeamNameAbbreviation","TeamShortName","GP","Poss",
    "Time","Points","FGA","FGM","PPP","WorsePPP","BetterPPP","PossG","PPG",
    "FGAG","FGMG","FGmG","FGm","FG","aFG","FT","TO","SF","PlusOne","Score"]

    """
    endpoint = 'http://stats.nba.com/js/data/playtype/team_Transition.js'
    response = utils.get_response(endpoint, None)
    return response['Defensive']


def team_cut_def():
    """
    returns synergy cut data for all teams this season
    returns:
        teams (list): cut data for all teams

    each team is a dict with the following available keys
    ["TeamIDSID","TeamName","TeamNameAbbreviation","TeamShortName","GP","Poss",
    "Time","Points","FGA","FGM","PPP","WorsePPP","BetterPPP","PossG","PPG",
    "FGAG","FGMG","FGmG","FGm","FG","aFG","FT","TO","SF","PlusOne","Score"]

    """
    endpoint = 'http://stats.nba.com/js/data/playtype/team_Cut.js'
    response = utils.get_response(endpoint, None)
    return response['Defensive']


def team_handoff_def():
    """
    returns synergy handler data for all teams this season
    returns:
        teams (list): handler data for all teams

    each team is a dict with the following available keys
    ["TeamIDSID","TeamName","TeamNameAbbreviation","TeamShortName","GP","Poss",
    "Time","Points","FGA","FGM","PPP","WorsePPP","BetterPPP","PossG","PPG",
    "FGAG","FGMG","FGmG","FGm","FG","aFG","FT","TO","SF","PlusOne","Score"]

    """
    endpoint = 'http://stats.nba.com/js/data/playtype/team_Handoff.js'
    response = utils.get_response(endpoint, None)
    return response['Defensive']


def team_pnr_handler_def():
    """
    returns synergy PnR ball handler data for all teams this season
    returns:
        teams (list): data for all teams

    each team is a dict with the following available keys
    ["TeamIDSID","TeamName","TeamNameAbbreviation","TeamShortName","GP","Poss",
    "Time","Points","FGA","FGM","PPP","WorsePPP","BetterPPP","PossG","PPG",
    "FGAG","FGMG","FGmG","FGm","FG","aFG","FT","TO","SF","PlusOne","Score"]

    """
    endpoint = 'http://stats.nba.com/js/data/playtype/team_PRBallHandler.js'
    response = utils.get_response(endpoint, None)
    return response['Defensive']


def team_isolation_def():
    """
    returns synergy isolation data for all teams this season
    returns:
        teams (list): isolation data for all teams

    each team is a dict with the following available keys
    ["TeamIDSID","TeamName","TeamNameAbbreviation","TeamShortName","GP","Poss",
    "Time","Points","FGA","FGM","PPP","WorsePPP","BetterPPP","PossG","PPG",
    "FGAG","FGMG","FGmG","FGm","FG","aFG","FT","TO","SF","PlusOne","Score"]

    """
    endpoint = 'http://stats.nba.com/js/data/playtype/team_Isolation.js'
    response = utils.get_response(endpoint, None)
    return response['Defensive']


def team_misc_def():
    """
    returns synergy misc data for all teams this season
    returns:
        teams (list): misc data for all teams

    each team is a dict with the following available keys
    ["TeamIDSID","TeamName","TeamNameAbbreviation","TeamShortName","GP","Poss",
    "Time","Points","FGA","FGM","PPP","WorsePPP","BetterPPP","PossG","PPG",
    "FGAG","FGMG","FGmG","FGm","FG","aFG","FT","TO","SF","PlusOne","Score"]

    """
    endpoint = 'http://stats.nba.com/js/data/playtype/team_Misc.js'
    response = utils.get_response(endpoint, None)
    return response['Defensive']


def team_postup_def():
    """
    returns synergy postup data for all teams this season
    returns:
        teams (list): postup data for all teams

    each team is a dict with the following available keys
    ["TeamIDSID","TeamName","TeamNameAbbreviation","TeamShortName","GP","Poss",
    "Time","Points","FGA","FGM","PPP","WorsePPP","BetterPPP","PossG","PPG",
    "FGAG","FGMG","FGmG","FGm","FG","aFG","FT","TO","SF","PlusOne","Score"]

    """
    endpoint = 'http://stats.nba.com/js/data/playtype/team_Postup.js'
    response = utils.get_response(endpoint, None)
    return response['Defensive']


def team_pnr_roll_def():
    """
    returns synergy PnR roll data for all teams this season
    returns:
        teams (list): PnR roll data for all teams

    each team is a dict with the following available keys
    ["TeamIDSID","TeamName","TeamNameAbbreviation","TeamShortName","GP","Poss",
    "Time","Points","FGA","FGM","PPP","WorsePPP","BetterPPP","PossG","PPG",
    "FGAG","FGMG","FGmG","FGm","FG","aFG","FT","TO","SF","PlusOne","Score"]

    """
    endpoint = 'http://stats.nba.com/js/data/playtype/team_PRRollMan.js'
    response = utils.get_response(endpoint, None)
    return response['Defensive']


def team_spotup_def():
    """
    returns synergy spotup data for all teams this season
    returns:
        teams (list): spotup data for all teams

    each team is a dict with the following available keys
    ["TeamIDSID","TeamName","TeamNameAbbreviation","TeamShortName","GP","Poss",
    "Time","Points","FGA","FGM","PPP","WorsePPP","BetterPPP","PossG","PPG",
    "FGAG","FGMG","FGmG","FGm","FG","aFG","FT","TO","SF","PlusOne","Score"]

    """
    endpoint = 'http://stats.nba.com/js/data/playtype/team_Spotup.js'
    response = utils.get_response(endpoint, None)
    return response['Defensive']


def team_off_rebound_def():
    """
    returns synergy off rebound data for all teams this season
    returns:
        teams (list): off rebound data for all teams

    each team is a dict with the following available keys
    ["TeamIDSID","TeamName","TeamNameAbbreviation","TeamShortName","GP","Poss",
    "Time","Points","FGA","FGM","PPP","WorsePPP","BetterPPP","PossG","PPG",
    "FGAG","FGMG","FGmG","FGm","FG","aFG","FT","TO","SF","PlusOne","Score"]

    """
    endpoint = 'http://stats.nba.com/js/data/playtype/team_OffRebound.js'
    response = utils.get_response(endpoint, None)
    return response['Defensive']


def team_screen_def():
    """
    returns synergy screen data for all teams this season
    returns:
        teams (list): offensive stats for off screen plays for all teams

    each team is a dict with the following available keys
    ["TeamIDSID","TeamName","TeamNameAbbreviation","TeamShortName","GP","Poss",
    "Time","Points","FGA","FGM","PPP","WorsePPP","BetterPPP","PossG","PPG",
    "FGAG","FGMG","FGmG","FGm","FG","aFG","FT","TO","SF","PlusOne","Score"]

    """
    endpoint = 'http://stats.nba.com/js/data/playtype/team_OffScreen.js'
    response = utils.get_response(endpoint, None)
    return response['Defensive']