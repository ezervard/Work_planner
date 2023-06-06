import calendar
import datetime
days = []
now = datetime.datetime.now()
year = now.year
month = now.month
def prew():
    global month , year
    month -=1
    if month == 0:
        month = 12
        year -= 1
def next():
    global month, year
    month += 1
    if month == 13:
        month = 1
        year += 1