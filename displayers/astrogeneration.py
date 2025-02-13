from persontoperson.models import birthchartdb
from persontoperson.personone import *
from persontoperson.singledegree import onematch

def table_calu_num(sheetNo, sheetRowNo, count, symbol, deg):
    if count==1 or count==6:
        if count ==1:
            return ([sheetNo[0], sheetRowNo[0], symbol, deg])
        if count ==6:
            return ([sheetNo[0], sheetRowNo[1], symbol, deg])
    if count==2 or count==7:
        if count ==2:
            return ([sheetNo[1], sheetRowNo[0], symbol, deg])
        if count ==7:
            return ([sheetNo[1], sheetRowNo[1], symbol, deg])
    if count==3 or count==8:
        if count ==3:
            return ([sheetNo[2], sheetRowNo[0], symbol, deg])
        if count ==8:
            return ([sheetNo[2], sheetRowNo[1], symbol, deg])
    if count==4 or count==9:
        if count ==4:
            return ([sheetNo[3], sheetRowNo[0], symbol, deg])
        if count ==9:
            return ([sheetNo[3], sheetRowNo[1], symbol, deg])
    if count==5 or count==10:
        if count ==5:
            return ([sheetNo[4], sheetRowNo[0], symbol, deg])
        if count ==10:
            return ([sheetNo[4], sheetRowNo[1], symbol, deg])
        

def astrogen(personName):
    personDb = birthchartdb.objects.get(fullname= personName)
    p1datelist = []
    p1date = str(personDb.date_of_birth).split('-')
    p1datelist.append(p1date[2])
    p1datelist.append(p1date[1])
    p1datelist.append(p1date[0])
    p1date = '.'.join(p1datelist)
    deg = onematch(p1date, personDb.time_of_birth, personDb.place_of_birth)
    constants_start_and_end_limit = constants_limit_for_sign()
    eve_person_one = event_person(constants_start_and_end_limit, deg[0], deg[1], deg[2], deg[3], deg[4], deg[5], deg[6], deg[7], deg[8], deg[9])
    eve_person_one['deg'] = round(eve_person_one["degree"] - (((eve_person_one['sign_num'] - 1) *30)))
    tableLis = []
    for index, row in eve_person_one.iterrows():
        if row.sign_num == 1:
            sheetColNo = list(range(1,6))
            sheetRowNo = [3,4]
            tableLis.append(table_calu_num(sheetColNo, sheetRowNo, index+1, row.planet, row.deg))
        if row.sign_num == 2:
            sheetColNo = list(range(1,6))
            sheetRowNo = [5,6]
            tableLis.append(table_calu_num(sheetColNo, sheetRowNo, index+1, row.planet, row.deg))
        if row.sign_num == 3:
            sheetColNo = list(range(1,6))
            sheetRowNo = [7,8]
            tableLis.append(table_calu_num(sheetColNo, sheetRowNo, index+1, row.planet, row.deg))
        if row.sign_num == 4:
            sheetColNo = list(range(6,11))
            sheetRowNo = [7,8]
            tableLis.append(table_calu_num(sheetColNo, sheetRowNo, index+1, row.planet, row.deg))
        if row.sign_num == 5:
            sheetColNo = list(range(11,16))
            sheetRowNo = [7,8]
            tableLis.append(table_calu_num(sheetColNo, sheetRowNo, index+1, row.planet, row.deg))
        if row.sign_num == 6:
            sheetColNo = list(range(16,21))
            sheetRowNo = [7,8]
            tableLis.append(table_calu_num(sheetColNo, sheetRowNo, index+1, row.planet, row.deg))
        if row.sign_num == 7:
            sheetColNo = list(range(16,21))
            sheetRowNo = [5,6]
            tableLis.append(table_calu_num(sheetColNo, sheetRowNo, index+1, row.planet, row.deg))
        if row.sign_num == 8:
            sheetColNo = list(range(16,21))
            sheetRowNo = [3,4]
            tableLis.append(table_calu_num(sheetColNo, sheetRowNo, index+1, row.planet, row.deg))
        if row.sign_num == 9:
            sheetColNo = list(range(16,21))
            sheetRowNo = [1,2]
            tableLis.append(table_calu_num(sheetColNo, sheetRowNo, index+1, row.planet, row.deg))
        if row.sign_num == 10:
            sheetColNo = list(range(11,16))
            sheetRowNo = [1,2]
            tableLis.append(table_calu_num(sheetColNo, sheetRowNo, index+1, row.planet, row.deg))
        if row.sign_num == 11:
            sheetColNo = list(range(6,11))
            sheetRowNo = [1,2]
            tableLis.append(table_calu_num(sheetColNo, sheetRowNo, index+1, row.planet, row.deg))
        if row.sign_num == 12:
            sheetColNo = list(range(1,6))
            sheetRowNo = [1,2]
            tableLis.append(table_calu_num(sheetColNo, sheetRowNo, index+1, row.planet, row.deg))
    return tableLis