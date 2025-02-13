import os
import googlemaps
from pandas import read_excel
from flatlib import const
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.chart import Chart
import datetime as dt



def bdate_time_place_to_degs(api, bdate, btime, bplace, lati=None, long=None):
    bdate = [int(i) for i in bdate.split('.')]
    if bdate[0] < 10:
        bdate[0] = '0' + str(bdate[0])
    else:
        bdate[0] = str(bdate[0])
    if bdate[1] < 10:
        bdate[1] = '0' + str(bdate[1])
    else:
        bdate[1] = str(bdate[1])
    bdate[2] = str(bdate[2])

    if len(bdate[0]) == 2:
        bdate = bdate[2] + '/' + bdate[1] + '/' + bdate[0]
    else:
        bdate = bdate[0] + '/' + bdate[1] + '/' + bdate[2]

    btime = str(btime)
    #
    if bplace is not None:
        place = api.geocode(bplace)
        
        lat, lon = place[0]['geometry']['location']['lat'], place[0]['geometry']['location']['lng']
    else:
        lat, lon = lati, long

    utcdiff = api.timezone([lat, lon])['rawOffset']
    udsign = str(utcdiff)[0]
    udsign = udsign if udsign == '-' else '+'
    utcdiff = abs(utcdiff)
    udh = utcdiff // 3600
    udm = (utcdiff - udh * 3600) // 60
    if udh < 10:
        udh = '0' + str(udh)
    else:
        udh = str(udh)
    if udm < 10:
        udm = '0' + str(udm)
    else:
        udm = str(udm)
    utcdiff = udsign + udh + ':' + udm

    nslat = None
    ewlon = None
    if lat < 0:
        nslat = 's'
    else:
        nslat = 'n'
    if lon < 0:
        ewlon = 'w'
    else:
        ewlon = 'e'
    lat = abs(lat)
    lon = abs(lon)
    lat_d = int(str(lat).split('.')[0])
    lat_m = str(int((lat - lat_d) * 60))
    lat_d = str(lat_d)
    lon_d = int(str(lon).split('.')[0])
    lon_m = str(int((lon - lon_d) * 60))
    lon_d = str(lon_d)
    bpl = [lat_d + nslat + lat_m, lon_d + ewlon + lon_m]
    date = Datetime(bdate, btime, utcdiff)
    pos = GeoPos(bpl[0], bpl[1])
    chart = Chart(date, pos)
    res=[]
    res.append(chart.get(const.SUN).lon)
    res.append(chart.get(const.MOON).lon)
    res.append(chart.get(const.MERCURY).lon)
    res.append(chart.get(const.MARS).lon)
    res.append(chart.get(const.JUPITER).lon)
    res.append(chart.get(const.VENUS).lon)
    res.append(chart.get(const.SATURN).lon)
    res.append(chart.get(const.NORTH_NODE).lon)
    res.append(chart.get(const.SOUTH_NODE).lon), "########################################"
    res.append(chart.get(const.ASC).lon)
    for i in range(len(res)):
        if res[i] - 23.17 < 0:
            res[i] = 360 + (res[i] - 23)
        else:
            res[i] -= 23.17
    return res


def onematch(bdate1, time1=None, place1=None):
    KEY = 'AIzaSyDpksPTT2PW4ZOSlzltN0QLV4zxT6U09pA'
    api = googlemaps.Client(key=KEY)
    array1 = bdate_time_place_to_degs(api, bdate1, time1, place1)
    return array1

