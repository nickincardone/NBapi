import datetime
import requests

_team_ids = {
    'atlanta': 1610612737,
    'cleveland': 1610612739,
    'toronto': 1610612761,
    'chicago': 1610612741,
    'washington': 1610612764,
    'milwaukee': 1610612749,
    'indiana': 1610612754,
    'charlotte': 1610612766,
    'boston': 1610612738,
    'miami': 1610612748,
    'brooklyn': 1610612751,
    'detroit': 1610612765,
    'orlando': 1610612753,
    'philadelphia': 1610612755,
    'new york': 1610612752,
    'golden state': 1610612744,
    'memphis': 1610612763,
    'portland': 1610612757,
    'houston': 1610612745,
    'san antonio': 1610612759,
    'dallas': 1610612742,
    'l.a. clippers': 1610612746,
    'oklahoma city': 1610612760,
    'new orleans': 1610612740,
    'phoenix': 1610612756,
    'utah': 1610612762,
    'denver': 1610612743,
    'sacramento': 1610612758,
    'l.a. lakers': 1610612747,
    'minnesota': 1610612750
}

_other_team_names = {
    'atl': 'atlanta',
    'cle': 'cleveland',
    'tor': 'toronto',
    'chi': 'chicago',
    'was': 'washington',
    'mil': 'milwaukee',
    'ind': 'indiana',
    'cha': 'charlotte',
    'bos': 'boston',
    'mia': 'miami',
    'brk': 'brooklyn',
    'det': 'detroit',
    'orl': 'orlando',
    'phi': 'philadelphia',
    'nyk': 'new york',
    'ny': 'new york',
    'gs': 'golden state',
    'gsw': 'golden state',
    'mem': 'memphis',
    'por': 'portland',
    'hou': 'houston',
    'sa': 'san antonio',
    'sas': 'san antonio',
    'dal': 'dallas',
    'lac': 'l.a. clippers',
    'la clippers': 'l.a. clippers',
    'okc': 'oklahoma city',
    'no': 'new orleans',
    'nop': 'new orleans',
    'pho': 'phoenix',
    'uta': 'utah',
    'den': 'denver',
    'sac': 'sacramento',
    'lal': 'l.a. lakers',
    'la lakers': 'l.a. lakers',
    'min': 'minnesota'
}

def get_team_id(team):
    team_clean = team.lower()
    if team_clean in _other_team_names:
        full_name = _other_team_names[team_clean]
        return _team_ids[full_name]
    if team_clean in _team_ids:
        return _team_ids[team]
    return None

def cleanse_team(team):
    if team in _team_ids.values():
        return team
    if type(team) is not str:
        return None
    if team.isdigit():
        if int(team) in _team_ids.values():
            return int(team)
        else:
            return None
    if team_id = get_team_id(team):
        return team_id

def cleanse_date(date):
    #TODO
    pass

def cleanse_season(season):
    def int_to_season(num):
        if num == 99:
            return '1999-00'
        if num == 1999:
            return '1999-00'
        if num == 0:
            return '2000-01'

        #two or single digit numbers
        if num < 100 and num >=10:
            if num < 40:
                return '20%s-%s' % (num, num+1)
            if num >= 40:
                return '19%s-%s' % (num, num+1)
        elif num == 9:
            return '2009-10'
        elif num < 10:
            return '200%s-0%s' % (num, num+1)

        #four digit
        if first_year <= num <= cur_year:
            if 2000 <= num <= 2008:
                next_year = (num%100)+1
                return '%s-0%s' % (num, next_year)
            next_year = (num%100)+1
            return '%s-%s' % (num, next_year)

        # input has number but doesn't correspond to a valid year
        raise ValueError('Input does not have corresponding year')

    first_year = 1940
    if datetime.date.today().month >= 7:
        cur_year = datetime.date.today().year + 1
    else:
        cur_year = datetime.date.today().year

    if type(season) is str:
        if '-' not in season:
            try:
                season_int = int(season)
                return int_to_season(season_int)
            except:
                raise ValueError('Invalid input, example input: 1999, 1999-00, 1999-2000, 99')
        else:
            try:
                season_int = int(season.split('-')[0])
                return int_to_season(season_int)
            except:
                raise ValueError('Invalid input, example input: 1999, 1999-00, 99')

    if type(season) is int:
        return int_to_season(season)
        
    raise ValueError('Invalid input, example input: 1999, 1999-00, 99')

def set_to_dict(result_set):
    result = []
    for row in result_set['rowSet']:
        cur_row = {}
        for i, item in enumerate(row):
            #uppercase all headers to prevent discrepencacy i.e. Game_ID vs GAME_ID
            header = result_set['headers'][i].upper()
            cur_row[header] = item
        result.append(cur_row)
    return result

def get_response(endpoint, payload):
    r = requests.get(endpoint, params=payload)
    response = r.json()
    result = {}
    result['params'] = response['parameters']
    result['resource'] = response['resource']
    for result_set in response['resultSets']:
        set_name = result_set['name']
        result[set_name] = set_to_dict(result_set)
    return result