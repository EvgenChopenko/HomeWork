import datetime
def get_days_to_new_year():
    next_year=datetime.date.today().year+1
    firs_date_next_year=datetime.date(day=1,month=1,year=next_year)
    delta = firs_date_next_year-datetime.date.today()
    return int(delta.days)

