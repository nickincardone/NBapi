import datetime

def clease_season(date):
    first_year = 1940
    cur_year = datetime.date.today().year

    if type(date) is str:
        # TODO
        pass

    if type(date) is int:
        if date == 99:
            return '1999-00'
        if date == 1999:
            return '1999-00'
        if date == 0:
            return '2000-01'

        #two or single digit numbers
        if date < 100 and date >=10:
            if date < 40:
                return '20%s-%s' % (date, date+1)
            if date >= 40:
                return '19%s-%s' % (date, date+1)
        elif date == 9:
            return '2009-10'
        elif date < 10:
            return '200%s-0%s' % (date, date+1)

        #four digit
        if first_year <= date <= cur_year:
            if 2000 <= date <= 2008:
                next_date_year = (date%100)+1
                return '%s-0%s' % (date, next_date_year)
            next_date_year = (date%100)+1
            return '%s-%s' % (date, next_date_year)

    # TODO throw custom error
    print 'pass through'

