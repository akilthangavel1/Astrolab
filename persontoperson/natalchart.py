from .models import birthchartdb
from pytz import timezone
import pandas as pd
import datetime as dt
import requests

def tz_diff(date, tz1, tz2):
    date = pd.to_datetime(date)
    timeInFloat =  (tz1.localize(date) - tz2.localize(date).astimezone(tz1)).seconds/3600
    if timeInFloat > 12:
        timeInFloat = (tz2.localize(date) - tz1.localize(date).astimezone(tz2)).seconds / 3600
        return timeInFloat, "-"
    else:
        timeInFloat =  (tz1.localize(date) - tz2.localize(date).astimezone(tz1)).seconds/3600
        return timeInFloat , '+'

def getTimezoneIdName(lan, lon):
    idName = requests.get("https://maps.googleapis.com/maps/api/timezone/json?location="+str(lan)+","+str(lon)+"&timestamp=1620469450&key=AIzaSyB7h3PspGaJV_aba1ZkPz9jh-KkGQaKYfw")
    return (idName.json())

def natal_db(full_name, birthdaydate, birthdaytime, location, loc_lat, loc_long,tZoneId, tZoneName, currentTimeDiff):
    fname = full_name
    dob = birthdaydate
    tob = birthdaytime
    print(tob)
    pob = location
    clan = loc_lat
    clon = loc_long
    s = birthchartdb(fullname = fname ,date_of_birth= dob, time_of_birth= tob, place_of_birth = pob, coordinates_lan = clan, coordinates_lon = clon, time_zone = currentTimeDiff, timeZoneId= tZoneId, timeZoneName = tZoneName)
    s.save()


def natal_main(full_name, birthdaydate, birthdaytime, location, loc_lat, loc_long, p1full_name, p1birthdaydate, p1birthdaytime, p1location, p1loc_lat, p1loc_long):
    mapsjson = getTimezoneIdName(loc_lat, loc_long)
    timeZoneId = mapsjson['timeZoneId']
    timeZoneName = mapsjson['timeZoneName']
    utc = timezone('UTC')
    aus = timezone(timeZoneId)
    currentTimeDiff = tz_diff(dt.date.today(), utc, aus)
    print(currentTimeDiff)
    currentTimeDiff = currentTimeDiff[1]+(str(dt.timedelta(hours=currentTimeDiff[0]))[:-3])
    print(currentTimeDiff)
    natal_db(full_name, birthdaydate, birthdaytime, location, loc_lat, loc_long, timeZoneId, timeZoneName, currentTimeDiff)