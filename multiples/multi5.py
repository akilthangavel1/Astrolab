from persontoperson.personone import *
from controlpanel.models import divisionName, modelNames
from persontoperson.singledegree import onematch
import  datetime as dt

def p1main_call(su_d, mo_d, me_d, ma_d, ju_d, ve_d, sa_d, ra_d, ke_d, as_d):
    constants_start_and_end_limit = constants_limit_for_sign()
    eve_person_one = event_person(constants_start_and_end_limit, su_d, mo_d, me_d, ma_d, ju_d, ve_d, sa_d, ra_d, ke_d, as_d)
    house_df = house_table(eve_person_one)
    house_sign_df = house_and_sign(house_df)
    sign_house_df = sign_and_house(house_sign_df)
    sign_planet_house_df = sign_planet_and_house(eve_person_one, sign_house_df)
    single_concatenation_df = single_concatenation_table(sign_planet_house_df)
    single_point_df = single_points_table(single_concatenation_df)
    point_planet_aspects_df = point_planets_planet_aspects(single_point_df)
    return single_concatenation_df, single_point_df


def p1_person_loop(peopleCategory):
    category_obj = divisionName.objects.get(divName=peopleCategory)
    listOfModelNames = modelNames.objects.filter(modelcategory=category_obj)
    dfLis = []
    conLis = []
    dfPointLis = []
    nameLis = []
    for i in listOfModelNames:
        print(i.modelFullName)
        nameLis.append(str(i.modelFullName))
        datetime_obj = i.birthDateTime
        datetime_obj = datetime_obj.replace("T", " ")
        personOneBirthDate = (dt.datetime.strptime(datetime_obj, '%Y-%m-%d %H:%M').date()).strftime('%d.%m.%Y')
        personOneBirthTime = (dt.datetime.strptime(datetime_obj, '%Y-%m-%d %H:%M').time()).strftime('%H:%M')
        arr = onematch(personOneBirthDate, personOneBirthTime, i.modelLocation)
        print(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8], arr[9])
        single_concatenation_df, single_point_df = p1main_call(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8], arr[9])
        dfPointLis.append(single_point_df)
        dfLis.append(single_concatenation_df)
        # print(single_concatenation_df, single_point_df)
    resultDic = dict((smallItem, {}
                   ) for smallItem in nameLis)
    
    count = 0
    for df in dfLis:
        rowCount = 0
        for index, row in df.iterrows():
            if len(str(row.Su_Conc)) > 1:
                resultDic[nameLis[count]][str(row.Su_Conc)] = dfPointLis[count]["Su_Point"][rowCount]
            if len(str(row.Mo_Conc)) > 1:
                resultDic[nameLis[count]][str(row.Mo_Conc)] = dfPointLis[count]["Mo_Point"][rowCount]
            if len(str(row.Me_Conc)) > 1:
                resultDic[nameLis[count]][str(row.Me_Conc)] = dfPointLis[count]["Me_Point"][rowCount]
            if len(str(row.Ma_Conc)) > 1:
                resultDic[nameLis[count]][str(row.Ma_Conc)] = dfPointLis[count]["Ma_Point"][rowCount]
            if len(str(row.Ju_Conc)) > 1:
                resultDic[nameLis[count]][str(row.Ju_Conc)] = dfPointLis[count]["Ju_Point"][rowCount]
            if len(str(row.Ve_Conc)) > 1:
                resultDic[nameLis[count]][str(row.Ve_Conc)] = dfPointLis[count]["Ve_Point"][rowCount]
            if len(str(row.Sa_Conc)) > 1:
                resultDic[nameLis[count]][str(row.Sa_Conc)] = dfPointLis[count]["Ve_Point"][rowCount]
            if len(str(row.Ra_Conc)) > 1:
                resultDic[nameLis[count]][str(row.Ra_Conc)] = dfPointLis[count]["Ra_Point"][rowCount]
            if len(str(row.Ke_Conc)) > 1:
                resultDic[nameLis[count]][str(row.Ke_Conc)] = dfPointLis[count]["Ke_Point"][rowCount]
            if len(str(row.As_Conc)) > 1:
                resultDic[nameLis[count]][str(row.As_Conc)] = dfPointLis[count]["As_Point"][rowCount]
            rowCount += 1
        count += 1
    print(resultDic)
    return nameLis, resultDic