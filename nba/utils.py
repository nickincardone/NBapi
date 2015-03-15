import datetime
import requests

def clease_season(season):
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
            header = result_set['headers'][i]
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