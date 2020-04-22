import datetime

print('datetime DATE')
d = datetime.date(2020,4,22)
print(d)
tday = datetime.date.today()
print(tday)
print(tday.year)
print(tday.month)
print(tday.day)
print(tday.weekday())  # Monday is 0 Sunday is 6
print(tday.isoweekday())  # Monday is 1 Sunday is 7

tdelta = datetime.timedelta(days=7)
print(tday + tdelta)
print(tday - tdelta)

bday = datetime.date(2020,4,1)
till_bday = bday - d
print(till_bday)
print(till_bday.days)
print(till_bday.total_seconds())

print('datetime TIME')
t = datetime.time(3,4,5,200000)
print(t)
print(t.hour)
print(t.minute)
print(t.second)

print('datetime DATETIME')
dt = datetime.datetime(2020,4,5,23,34,23,200000)
print(dt)
print(dt.date())
print(dt.time())

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())

print('datetime DATETIME using pytz for time zone')
import pytz
print(datetime.datetime(2020,4,5,23,34,23,200000,tzinfo=pytz.UTC))
print(datetime.datetime.today())
print(datetime.datetime.now(tz=pytz.UTC))
print(datetime.datetime.utcnow().replace(tzinfo=pytz.UTC))

print('datetime DATETIME using pytz for time zone CONVERT TZ')
dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)
dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)

print('Find  time zone from pytz')
for tz in pytz.all_timezones:
    #print(tz)
    pass

print('Convert DATETIME to STRING')
print('strftime CONVERT Datetime to String :')

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow.strftime('%B %d , %Y'))

print('Convert STRING to DATETIME')
print('strptime CONVERT STRING to DATEIIME :')
string_d = 'April 22 , 2020'
dt = datetime.datetime.strptime(string_d,'%B %d , %Y')
print(dt)


