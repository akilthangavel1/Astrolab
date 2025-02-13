from persontoperson.astro_fun import *
from persontoperson.integrated_report import ir_concatenation_graph
from controlpanel.models import divisionName, modelNames
from persontoperson.singledegree import onematch
import datetime as dt

def integrated_report_multi4(su_d, mo_d, me_d, ma_d, ju_d, ve_d, sa_d, ra_d, ke_d, as_d, su_d2, mo_d2, me_d2, ma_d2, ju_d2, ve_d2, sa_d2, ra_d2, ke_d2, as_d2):
    # print(su_d, mo_d, me_d, ma_d, ju_d, ve_d, sa_d, ra_d, ke_d, as_d, su_d2, mo_d2, me_d2, ma_d2, ju_d2, ve_d2, sa_d2, ra_d2, ke_d2, as_d2)
    constants_start_and_end_limit = constants_limit_for_sign()
    pasp_table_df = pasp_table_degs()
    sign_table_df = sign_table_degs()
    p1vsp2_eve_person_one = event_person(constants_start_and_end_limit, su_d, mo_d, me_d, ma_d, ju_d, ve_d, sa_d, ra_d, ke_d, as_d)
    p1vsp2_eve_person_two = event_person(constants_start_and_end_limit, su_d2, mo_d2, me_d2, ma_d2, ju_d2, ve_d2, sa_d2, ra_d2, ke_d2, as_d2)
    p1vsp2_house_df = house_table(p1vsp2_eve_person_one)
    p1vsp2_house_sign_df = house_and_sign(p1vsp2_house_df)
    p1vsp2_sign_house_df = sign_and_house(p1vsp2_house_sign_df)
    p1vsp2_sign_planet_house_df = sign_planet_and_house(p1vsp2_eve_person_one, p1vsp2_sign_house_df)
    p1vsp2_con_sign_planet_df = p1vsp2_concatenation_sign_house(p1vsp2_sign_planet_house_df, pasp_table_df, sign_table_df, p1vsp2_eve_person_two)
    p1_concatenation_df = p1_concatenation_table(p1vsp2_sign_planet_house_df, pasp_table_df, sign_table_df)
    p1_point_df = p1_points_table(p1_concatenation_df)
    p1_point_planet_aspects_df = p1_point_planets_planet_aspects(p1_point_df)
    p1vsp2_point_df = p1vsp2_points_table(p1vsp2_con_sign_planet_df, p1_point_planet_aspects_df)
    p1xp2_sep_degree_df = p1vsp2_sep_degree(p1vsp2_eve_person_one, p1vsp2_eve_person_two)
    p1xp2_distance_df = p1xp2_distance_table(p1vsp2_point_df, p1xp2_sep_degree_df)
    p1xp2_dm_data_df = p1xp2_dm_data()
    p1xp2_distance_planets_df = p1xp2_distance_between_planets(p1xp2_distance_df, p1xp2_dm_data_df)
    ir_con_graph_df = ir_concatenation_graph(p1xp2_distance_df, p1xp2_distance_planets_df)
    df_conj, df_180, df_greater120, df_lesser120, df_greater90, df_lesser90, df_greater60, df_lesser60, df_greater150 = ir_con_graph_df[0], ir_con_graph_df[1], ir_con_graph_df[2], ir_con_graph_df[3], ir_con_graph_df[4], ir_con_graph_df[5], ir_con_graph_df[6], ir_con_graph_df[7], ir_con_graph_df[8]
    # ir_con_graph_df = pd.DataFrame(ir_con_graph_df)
    df1 = pd.DataFrame()
    dfLis = []
    for i in ir_con_graph_df:
        tempDf = pd.DataFrame.from_records(i, columns=['type', 'planet', 'conca', 'distance', 'point'])
        dfLis.append(tempDf)
    data = pd.concat(dfLis, axis=0)
    data = data.reset_index()
    return data



def multi4_main(peopleCategory, fullName, birthDate, birthTime, location):
    category_obj = divisionName.objects.get(divName=peopleCategory)
    listOfModelNames = modelNames.objects.filter(modelcategory=category_obj)
    nameLen = len(listOfModelNames)
    personTwoBirthDate = birthDate.replace("-", ".")
    lisCount = []
    keyLis = []
    dfLis = []
    nameLis = []
    for i in range(nameLen):
        lisCount.append(0)
    for i in listOfModelNames:
        nameLis.append(i.modelFullName)
        datetime_obj = i.birthDateTime
        datetime_obj = datetime_obj.replace("T", " ")
        personOneBirthDate = (dt.datetime.strptime(datetime_obj, '%Y-%m-%d %H:%M').date()).strftime('%d.%m.%Y')
        personOneBirthTime = (dt.datetime.strptime(datetime_obj, '%Y-%m-%d %H:%M').time()).strftime('%H:%M')
        personOneDegrees = onematch(personOneBirthDate, personOneBirthTime, i.modelLocation)
        personTwoDegrees = onematch(personTwoBirthDate, birthTime, location)
        df = integrated_report_multi4(personOneDegrees[0], personOneDegrees[1], personOneDegrees[2], personOneDegrees[3], personOneDegrees[4], personOneDegrees[5], personOneDegrees[6], personOneDegrees[7], personOneDegrees[8], personOneDegrees[9], personTwoDegrees[0], personTwoDegrees[1], personTwoDegrees[2], personTwoDegrees[3], personTwoDegrees[4], personTwoDegrees[5], personTwoDegrees[6], personTwoDegrees[7], personTwoDegrees[8], personTwoDegrees[9])
        dfLis.append(df)
    for df in dfLis:
        for index, row in df.iterrows():
            if row.conca not in keyLis:
                keyLis.append(row.conca)
    resultDic = dict((smallItem, {"pnt": []}
                   ) for smallItem in keyLis)
    count = 0
    for df in dfLis:
        for i in resultDic:
            try:
                value = df.loc[df['conca'] == i, 'point'].iloc[0]
                resultDic[i]["pnt"].append(value)
            except IndexError:
                resultDic[i]["pnt"].append(0)
    return nameLis, resultDic