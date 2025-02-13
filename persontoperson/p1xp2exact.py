import pandas as pd
from .p1conp2 import *
from .models import distance_multiplier
from django_pandas.io import read_frame
from .personone import single_concatenation_table, single_points_table, point_planets_planet_aspects


def dm_data():
    data = distance_multiplier.objects.all()
    data = read_frame(data)
    return data


def distance_between_planets(distance_df, dm_data_df):
    df1 = distance_df.copy()
    df2 = dm_data_df.copy()
    Su_dp_lst = []
    Mo_dp_lst = []
    Me_dp_lst = []
    Ma_dp_lst = []
    Ju_dp_lst = []
    Ve_dp_lst = []
    Sa_dp_lst = []
    Ra_dp_lst = []
    Ke_dp_lst = []
    As_dp_lst = []
    dp_total_lst = []
    for index, row in df1.iterrows():
        if len(str(row.Su_Conc)) > 1:
            try:
                temp = (df2.loc[df2['distance'] == round(row.Su_Dis_lst,1)]["multiplier"].values[0])
                Su_dp_lst.append(row.Su_Point * float(temp))
            except Exception as e:
                Su_dp_lst.append(0)
        else:
            Su_dp_lst.append(0)

        if len(str(row.Mo_Conc)) > 1:
            temp = (df2.loc[df2['distance'] == round(row.Mo_Dis_lst, 1)]["multiplier"].values[0])
            Mo_dp_lst.append(row.Mo_Point * float(temp))
        else:
            Mo_dp_lst.append(0)

        if len(str(row.Me_Conc)) > 1:
            temp = (df2.loc[df2['distance'] == round(row.Me_Dis_lst, 1)]["multiplier"].values[0])
            Me_dp_lst.append(row.Me_Point * float(temp))
        else:
            Me_dp_lst.append(0)

        if len(str(row.Ma_Conc)) > 1:
            temp = (df2.loc[df2['distance'] == round(row.Ma_Dis_lst, 1)]["multiplier"].values[0])
            Ma_dp_lst.append(row.Ma_Point * float(temp))
        else:
            Ma_dp_lst.append(0)

        if len(str(row.Ju_Conc)) > 1:
            temp = (df2.loc[df2['distance'] == round(row.Ju_Dis_lst, 1)]["multiplier"].values[0])
            Ju_dp_lst.append(row.Ju_Point * float(temp))
        else:
            Ju_dp_lst.append(0)

        if len(str(row.Ve_Conc)) > 1:
            temp = (df2.loc[df2['distance'] == round(row.Ve_Dis_lst, 1)]["multiplier"].values[0])
            Ve_dp_lst.append(row.Ve_Point * float(temp))
        else:
            Ve_dp_lst.append(0)

        if len(str(row.Sa_Conc)) > 1:
            temp = (df2.loc[df2['distance'] == round(row.Sa_Dis_lst, 1)]["multiplier"].values[0])
            Sa_dp_lst.append(row.Sa_Point * float(temp))
        else:
            Sa_dp_lst.append(0)

        if len(str(row.Ra_Conc)) > 1:
            temp = (df2.loc[df2['distance'] == round(row.Ra_Dis_lst, 1)]["multiplier"].values[0])
            Ra_dp_lst.append(row.Ra_Point * float(temp))
        else:
            Ra_dp_lst.append(0)

        if len(str(row.Ke_Conc)) > 1:
            temp = (df2.loc[df2['distance'] == round(row.Ke_Dis_lst, 1)]["multiplier"].values[0])
            Ke_dp_lst.append(row.Ke_Point * float(temp))
        else:
            Ke_dp_lst.append(0)

        if len(str(row.As_Conc)) > 1:
            temp = (df2.loc[df2['distance'] == round(row.As_Dis_lst, 1)]["multiplier"].values[0])
            As_dp_lst.append(row.As_Point * float(temp))
        else:
            As_dp_lst.append(0)
    df = pd.DataFrame(columns=['type'])
    type_list = ["Conj", "180", "120<", ">120", "90<", ">90", "60<", ">60"]
    for i in type_list:
        lst = list_to_list_of_lists([i for j in range(10)])
        for k in lst:
            df.loc[len(df)] = k
    df.loc[len(df)] = [">150"]
    df['planet'] = (["Su", "Mo", "Me", "Ma", "Ju", "Ve", "Sa", "Ra", "Ke", "As"] * (len(df) // 2 + 1))[:len(df)]
    df.loc[df.type == ">150", "planet"] = "Ma"
    if Su_dp_lst[-1] != 0:
        Su_dp_lst[-1] = (Su_dp_lst[-1] * 1.5)
    if Mo_dp_lst[-1] != 0:
        Mo_dp_lst[-1] = (Mo_dp_lst[-1] * 1.5)
    if Me_dp_lst[-1] != 0:
        Me_dp_lst[-1] = (Me_dp_lst[-1] * 1.5)
    if Ma_dp_lst[-1] != 0:
        Ma_dp_lst[-1] = (Ma_dp_lst[-1] * 1.5)
    if Ju_dp_lst[-1] != 0:
        Ju_dp_lst[-1] = (Ju_dp_lst[-1] * 1.5)
    if Ve_dp_lst[-1] != 0:
        Ve_dp_lst[-1] = (Ve_dp_lst[-1] * 1.5)
    if Sa_dp_lst[-1] != 0:
        Sa_dp_lst[-1] = (Sa_dp_lst[-1] * 1.5)
    if Ra_dp_lst[-1] != 0:
        Ra_dp_lst[-1] = (Ra_dp_lst[-1] * 1.5)
    if Ke_dp_lst[-1] != 0:
        Ke_dp_lst[-1] = (Ke_dp_lst[-1] * 1.5)
    if As_dp_lst[-1] != 0:
        As_dp_lst = (As_dp_lst[-1] * 1.5)



    df["Su_dp_lst"] = Su_dp_lst
    df["Mo_dp_lst"] = Mo_dp_lst
    df["Me_dp_lst"] = Me_dp_lst
    df["Ma_dp_lst"] = Ma_dp_lst
    df["Ju_dp_lst"] = Ju_dp_lst
    df["Ve_dp_lst"] = Ve_dp_lst
    df["Sa_dp_lst"] = Sa_dp_lst
    df["Ra_dp_lst"] = Ra_dp_lst
    df["Ke_dp_lst"] = Ke_dp_lst
    df["As_dp_lst"] = As_dp_lst
    for index, row in df.iterrows():
        if row.type == "Conj":
            dp_total_lst.append((row.Su_dp_lst + row.Mo_dp_lst + row.Me_dp_lst + row.Ma_dp_lst  + row.Ju_dp_lst
                 + row.Ve_dp_lst + row.Sa_dp_lst + row.Ra_dp_lst + row.Ke_dp_lst + row.As_dp_lst)*2)
        if row.type == "180":
            dp_total_lst.append((row.Su_dp_lst + row.Mo_dp_lst + row.Me_dp_lst + row.Ma_dp_lst + row.Ju_dp_lst
                                 + row.Ve_dp_lst + row.Sa_dp_lst + row.Ra_dp_lst + row.Ke_dp_lst + row.As_dp_lst) * 1.5)
        if row.type == "120<":
            dp_total_lst.append((row.Su_dp_lst + row.Mo_dp_lst + row.Me_dp_lst + row.Ma_dp_lst + row.Ju_dp_lst
                                 + row.Ve_dp_lst + row.Sa_dp_lst + row.Ra_dp_lst + row.Ke_dp_lst + row.As_dp_lst))
        if row.type == ">120":
            dp_total_lst.append((row.Su_dp_lst + row.Mo_dp_lst + row.Me_dp_lst + row.Ma_dp_lst + row.Ju_dp_lst
                                 + row.Ve_dp_lst + row.Sa_dp_lst + row.Ra_dp_lst + row.Ke_dp_lst + row.As_dp_lst))
        if row.type == "90<":
            dp_total_lst.append((row.Su_dp_lst + row.Mo_dp_lst + row.Me_dp_lst + row.Ma_dp_lst + row.Ju_dp_lst
                                 + row.Ve_dp_lst + row.Sa_dp_lst + row.Ra_dp_lst + row.Ke_dp_lst + row.As_dp_lst) * 0.7)
        if row.type == ">90":
            dp_total_lst.append((row.Su_dp_lst + row.Mo_dp_lst + row.Me_dp_lst + row.Ma_dp_lst + row.Ju_dp_lst
                                 + row.Ve_dp_lst + row.Sa_dp_lst + row.Ra_dp_lst + row.Ke_dp_lst + row.As_dp_lst)* 0.7)
        if row.type == "60<":
            dp_total_lst.append((row.Su_dp_lst + row.Mo_dp_lst + row.Me_dp_lst + row.Ma_dp_lst + row.Ju_dp_lst
                                 + row.Ve_dp_lst + row.Sa_dp_lst + row.Ra_dp_lst + row.Ke_dp_lst + row.As_dp_lst)* 0.4)
        if row.type == ">60":
            dp_total_lst.append((row.Su_dp_lst + row.Mo_dp_lst + row.Me_dp_lst + row.Ma_dp_lst + row.Ju_dp_lst
                                 + row.Ve_dp_lst + row.Sa_dp_lst + row.Ra_dp_lst + row.Ke_dp_lst + row.As_dp_lst)* 0.4)
        if row.type == ">150":
            dp_total_lst.append((row.Su_dp_lst + row.Mo_dp_lst + row.Me_dp_lst + row.Ma_dp_lst + row.Ju_dp_lst
                                 + row.Ve_dp_lst + row.Sa_dp_lst + row.Ra_dp_lst + row.Ke_dp_lst + row.As_dp_lst)* 1.5)
    df["dp_total_lst"] = dp_total_lst
    return df


def interaccion(distance_planets_df):
    df1 = distance_planets_df.copy()
    df = pd.DataFrame()
    temp_lst = []
    planets = ["Su", "Mo", "Me", "Ma", "Ju", "Ve", "Sa", "Ra", "Ke", "As"]
    for i in planets:
        for j in planets:
            temp_lst.append(i+("(p1)") +"<" + j+("(p2)"))
    df["INTERACCIÓN"] = temp_lst
    df2 = df1.set_index("planet")
    inter_list = []
    main_lis = []
    temp = df2.Su_dp_lst
    for i in planets:
        inter_list.append(temp[i].to_list())
    temp = df2.Mo_dp_lst
    for i in planets:
        inter_list.append(temp[i].to_list())
    temp = df2.Me_dp_lst
    for i in planets:
        inter_list.append(temp[i].to_list())
    temp = df2.Ma_dp_lst
    for i in planets:
        inter_list.append(temp[i].to_list())
    temp = df2.Ju_dp_lst
    for i in planets:
        inter_list.append(temp[i].to_list())
    temp = df2.Ve_dp_lst
    for i in planets:
        inter_list.append(temp[i].to_list())
    temp = df2.Sa_dp_lst
    for i in planets:
        inter_list.append(temp[i].to_list())
    temp = df2.Ra_dp_lst
    for i in planets:
        inter_list.append(temp[i].to_list())
    temp = df2.Ke_dp_lst
    for i in planets:
        inter_list.append(temp[i].to_list())
    temp = df2.As_dp_lst
    for i in planets:
        inter_list.append(temp[i].to_list())
    for i in inter_list:
        main_lis.append(i[0]*2 + i[1]*1.5+i[2]+i[3]+(i[4]+i[5])*0.7+ (i[6]+i[7])*0.4)
    main_lis[30] = main_lis[30] + df1.iloc[80, df1.columns.get_loc("Su_dp_lst")]
    main_lis[31] = main_lis[31] + df1.iloc[80, df1.columns.get_loc("Mo_dp_lst")]
    main_lis[32] = main_lis[32] + df1.iloc[80, df1.columns.get_loc("Me_dp_lst")]
    main_lis[33] = main_lis[33] + df1.iloc[80, df1.columns.get_loc("Ma_dp_lst")]
    main_lis[34] = main_lis[34] + df1.iloc[80, df1.columns.get_loc("Ju_dp_lst")]
    main_lis[35] = main_lis[35] + df1.iloc[80, df1.columns.get_loc("Ve_dp_lst")]
    main_lis[36] = main_lis[36] + df1.iloc[80, df1.columns.get_loc("Sa_dp_lst")]
    main_lis[37] = main_lis[37] + df1.iloc[80, df1.columns.get_loc("Ra_dp_lst")]
    main_lis[38] = main_lis[38] + df1.iloc[80, df1.columns.get_loc("Ke_dp_lst")]
    main_lis[39] = main_lis[39] + df1.iloc[80, df1.columns.get_loc("As_dp_lst")]
    df["puntaje"] = main_lis
    return df

def p1p2recibe(interaccion_df):
    planets = ["Su", "Mo", "Me", "Ma", "Ju", "Ve", "Sa", "Ra", "Ke", "As"]
    df1 = interaccion_df.copy()
    df1['planet'] = (["Su", "Mo", "Me", "Ma", "Ju", "Ve", "Sa", "Ra", "Ke", "As"] * (len(df1) // 2 + 1))[:len(df1)]
    temp = df1.groupby("planet").sum()
    temp_lst = []
    for i in planets:
        temp_lst.append(temp.loc[i][0])
    df = pd.DataFrame()
    df["planet"] = planets
    df["P2_Recibe_a"] = temp_lst
    df["P2_Recibe_b"] = temp_lst
    return df



def p1xp2ex_main(su_d, mo_d, me_d, ma_d, ju_d, ve_d, sa_d, ra_d, ke_d, as_d, su_d2, mo_d2, me_d2, ma_d2, ju_d2, ve_d2, sa_d2, ra_d2, ke_d2, as_d2):
    constants_start_and_end_limit = constants_limit_for_sign()
    eve_person_one = event_person(constants_start_and_end_limit, su_d, mo_d, me_d, ma_d, ju_d, ve_d, sa_d, ra_d, ke_d, as_d)
    eve_person_two = event_person(constants_start_and_end_limit, su_d2, mo_d2, me_d2, ma_d2, ju_d2, ve_d2, sa_d2, ra_d2, ke_d2, as_d2)
    house_df = house_table(eve_person_one)
    house_sign_df = house_and_sign(house_df)
    sign_house_df = sign_and_house(house_sign_df)
    sign_planet_house_df = sign_planet_and_house(eve_person_one, sign_house_df)
    pasp_table_df = pasp_table_degs()
    sign_table_df = sign_table_degs()
    sep_degree_df = sep_degree_p1p2(eve_person_one, eve_person_two)
    con_sign_planet_df = concatenation_sign_house(sign_planet_house_df, pasp_table_df, sign_table_df, eve_person_two)
    single_concatenation_df = single_concatenation_table(sign_planet_house_df)
    single_point_df = single_points_table(single_concatenation_df)
    point_planet_aspects_df = point_planets_planet_aspects(single_point_df)
    point_df = points_table(con_sign_planet_df, point_planet_aspects_df)
    distance_df = distance_table(point_df, sep_degree_df)
    dm_data_df = dm_data()
    distance_planets_df = distance_between_planets(distance_df, dm_data_df)
    interaccion_df = interaccion(distance_planets_df)
    p1p2recibe_df = p1p2recibe(interaccion_df)
    eve_person_one = dataframe_to_dict(eve_person_one)
    eve_person_two = dataframe_to_dict(eve_person_two)
    house_df = dataframe_to_dict(house_df)
    house_sign_df = dataframe_to_dict(house_sign_df)
    sign_house_df = dataframe_to_dict(sign_house_df)
    sign_planet_house_df = dataframe_to_dict(sign_planet_house_df)
    con_sign_planet_df = dataframe_to_dict(con_sign_planet_df)
    point_df = dataframe_to_dict(point_df)
    distance_df = dataframe_to_dict(distance_df)
    distance_planets_df = dataframe_to_dict(distance_planets_df)
    interaccion_df = dataframe_to_dict(interaccion_df)
    p1p2recibe_df = dataframe_to_dict(p1p2recibe_df)
    main_dic = {"eve_person_one": eve_person_one, "eve_person_two": eve_person_two, "house_df": house_df,
                "house_sign_df": house_sign_df, "sign_house_df": sign_house_df,
                "sign_planet_house_df": sign_planet_house_df,
                "con_sign_planet_df": con_sign_planet_df, "point_df": point_df, "distance_df": distance_df,
                "distance_planets_df": distance_planets_df, "interaccion_df": interaccion_df, "p1p2recibe_df": p1p2recibe_df}
    return main_dic
