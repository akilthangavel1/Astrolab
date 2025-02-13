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
    idName = requests.get("https://maps.googleapis.com/maps/api/timezone/json?location="+str(lan)+","+str(lon)+"&timestamp=1620469450&key=AIzaSyASsKRcBk1D1J_oWy7teTjodHQ5N1uOl1M")
    return (idName.json())


def homesaveupdate(pfname, plocation, plat, plon, pdate, ptime):
    mapsjson = getTimezoneIdName(plat, plon)
    tZoneId = mapsjson['timeZoneId']
    tZoneName = mapsjson['timeZoneName']
    utc = timezone('UTC')
    aus = timezone(tZoneId)
    currentTimeDiff = tz_diff(dt.date.today(), utc, aus)
    tztime = currentTimeDiff[1] + (str(dt.timedelta(hours=currentTimeDiff[0]))[:-3])
    bdlist = birthchartdb.objects.filter(**{"fullname": pfname})
    if bdlist:
        for i in bdlist:
            s = birthchartdb(id=i.id, fullname= pfname, date_of_birth=pdate, time_of_birth=ptime, place_of_birth=plocation,
                         coordinates_lan=plat, coordinates_lon=plon, time_zone=tztime, timeZoneId=tZoneId, timeZoneName=tZoneName)
            s.save()
    else:
        s = birthchartdb(fullname= pfname, date_of_birth=pdate, time_of_birth=ptime, place_of_birth=plocation,
                         coordinates_lan=plat, coordinates_lon=plon, time_zone=tztime, timeZoneId=tZoneId, timeZoneName=tZoneName)
        s.save()
    # print(pfname, plocation, plat, plon, pdate, ptime, tZoneId, timeZoneName, tztime)