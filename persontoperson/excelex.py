import pandas as pd
from .models import concatenation_points, distance_multiplier, birthchartdb

def readex():
    file =('ex.ods')
    df1 = pd.read_excel(file)
    df1 = df1.iloc[:, 0:2]
    print(df1)
    df1.columns = ["CONCATENATION", "Conj"]
    print(df1)
    for index, row in df1.iterrows():
        print("##################")
        type = "Conj"
        name = row.CONCATENATION
        points = row.Conj
        print(type,name, points)
        s = concatenation_points(con_type=type, con_name=name, con_points=points)
        s.save()

def readdm():
    file = ('dm.ods')
    df1 = pd.read_excel(file)
    print(df1)
    for index, row in df1.iterrows():
        print(row.DISTANCE, row.MULTIPLIER)
        s = distance_multiplier(distance=row.DISTANCE, multiplier=row.MULTIPLIER)
        s.save()
    print(df1)


def impeopledata():
    file = ('lanadded.xlsx')
    df1 = pd.read_excel(file)
    print(df1)
    for index, row in df1.iterrows():
        try:
            print(index, row.id)
            s = birthchartdb(fullname = row.names, date_of_birth =row.date ,time_of_birth = row.time,place_of_birth =row.place ,coordinates_lan = 0  ,coordinates_lon = 0,time_zone = "None",timeZoneId = "None",timeZoneName = 0)
            s.save()
        except Exception as e:
            print(e)
            continue