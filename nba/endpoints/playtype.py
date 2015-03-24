from nba import utils

'''
TODO make sure player defensive endpoints docs are right

available methods
    {team/player}_transition_{off/def}_data
    {team/player}_cut_{off/def}_data
    {team/player}_pr_ball_handler_{off/def}_data
    {team/player}_handoff_{off/def}_data
    {team/player}_isolation_{off/def}_data
    {team/player}_misc_{off/def}_data
    {team/player}_post_up_{off/def}_data
    {team/player}_pr_roll_{off/def}_data
    {team/player}_spotup_{off/def}_data
TODO
    http://stats.nba.com/js/data/playtype/player_OffScreen.js

'''

def player_transition_off_data():
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


def player_cut_off_data():
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


def player_handoff_off_data():
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


def player_pnr_handler_off_data():
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


def player_isolation_off_data():
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


def player_misc_off_data():
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


def player_postup_off_data():
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


def player_pnr_roll_off_data():
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


def player_spotup_off_data():
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


def player_off_rebound_data():
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


def player_transition_def_data():
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
    return response['Defensive']


def player_cut_def_data():
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
    return response['Defensive']


def player_handoff_def_data():
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
    return response['Defensive']


def player_pnr_handler_def_data():
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
    return response['Defensive']


def player_isolation_def_data():
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
    return response['Defensive']


def player_misc_def_data():
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
    return response['Defensive']


def player_postup_def_data():
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
    return response['Defensive']


def player_pnr_roll_def_data():
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
    return response['Defensive']


def player_spotup_def_data():
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
    return response['Defensive']


def team_transition_off_data():
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


def team_cut_off_data():
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


def team_handoff_off_data():
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


def team_pnr_handler_off_data():
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


def team_isolation_off_data():
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


def team_misc_off_data():
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


def team_postup_off_data():
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


def team_pnr_roll_off_data():
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


def team_spotup_off_data():
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


def team_off_rebound_off_data():
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


def team_transition_def_data():
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


def team_cut_def_data():
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


def team_handoff_def_data():
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


def team_pnr_handler_def_data():
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


def team_isolation_def_data():
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


def team_misc_def_data():
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


def team_postup_def_data():
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


def team_pnr_roll_def_data():
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


def team_spotup_def_data():
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


def team_off_rebound_def_data():
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

