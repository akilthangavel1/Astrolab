import pandas as pd
import json
import numpy as np
from .models import concatenation_points
from django_pandas.io import read_frame
from .models import distance_multiplier

# CONVERTING THE DATAFRAME TO DICTIONARY FOR PASSING THROUGH CONTEXT
def dataframe_to_dict(df):
    json_records = df.reset_index().to_json(orient='records')
    data = []
    data = json.loads(json_records)
    return data

#CONSTANT LIMITS FOR SIGN
def constants_limit_for_sign():
    cons_limit = pd.DataFrame([
        [1, "Ar", 0, 30.00],
        [2, "Ta", 30.01, 60.00],
        [3, "Ge", 60.01, 90.00],
        [4, "Ca", 90.01, 120.00],
        [5, "Le", 120.01, 150.00],
        [6, "Vg", 150.01, 180.00],
        [7, "Li", 180.01, 210.00],
        [8, "Sc", 210.01, 240.00],
        [9, "Sg", 240.01, 270.00],
        [10, "Cp", 270.01, 300.00],
        [11, "Aq", 300.01, 330.00],
        [12, "Pi", 330.01, 360.00],
        ], columns=["sign_num", "sign_name", "start_limit", "end_limit"])
    return cons_limit


# Degree will passed through this fuction to create Event person table
def event_person(cons_limit, su_d, mo_d, me_d, ma_d, ju_d, ve_d, sa_d, ra_d, ke_d, as_d):
    df = pd.DataFrame([["Su", float(su_d)], ["Mo", float(mo_d)], ["Me",float(me_d)], ["Ma", float(ma_d)], ["Ju", float(ju_d)], ["Ve", float(ve_d)],["Sa", float(sa_d)], ["Ra", float(ra_d)], ["Ke", float(ke_d)], ["As", float(as_d)]], columns=["planet", "degree"])
    sign_lis = []
    for index, row in df.iterrows():
        for i, r in cons_limit.iterrows():
            if r.start_limit <= row.degree and r.end_limit >= row.degree:
                sign_lis.append(r.sign_name)
    df["sign_name"] = sign_lis
    df['sign_num'] = df['sign_name'].map(cons_limit.set_index('sign_name')['sign_num'])
    return df


# Generates house numbers with colored cell number 1
def house_table(person_table):
    person_df = person_table.copy()
    df = pd.DataFrame(np.zeros((12, 12)),
                      columns=["H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11", "H12", ])
    df["sign_name"] = ["Ar", "Ta", "Ge", "Ca", "Le", "Vg", "Li", "Sc", "Sg", "Cp", "Aq", "Pi"]
    df.index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    start_block = (person_df.sign_num.tail(1).values)[0]
    start_house = "H1"
    for i in df.index:
        df.loc[start_block, start_house] = 1
        first_letter = start_house[0]
        start_house = "H" + str(int(start_house.replace(first_letter, "")) + 1)
        if start_block == 12:
            start_block = 1
        else:
            start_block += 1
    return df


# house and sign is obtained fron housedf function
def house_and_sign(house_df):
    house_and_respective_sign = pd.DataFrame(columns=["sign_name", "sign_num","house_num"])
    for i in range(1,13):
        house_number = "H"+str(i)
        house_and_respective_sign = house_and_respective_sign.append({'sign_name': house_df.loc[house_df[house_number].isin([1])].sign_name.values[0], 'sign_num': house_df.loc[house_df[house_number].isin([1])].index.values[0], 'house_num': i}, ignore_index=True)
    return house_and_respective_sign


#sign and house is obtained from house and sign function
def sign_and_house(house_sign_df):
    sign_and_respective_house  = house_sign_df.sort_values(by="sign_num")
    return sign_and_respective_house

#sign planet house is obtained from event person one and sign house table
def sign_planet_and_house(df1, df2):
    df1 = df1.drop(["sign_num", "degree"], axis=1)
    df1['house_num'] = df1['sign_name'].map(df2.set_index('sign_name')['house_num'])
    return (df1)

#converts list to list of lists
def list_to_list_of_lists(lst):
    return [[el] for el in lst]

# return planet name using planet number
def planet_num_check(num):
    if num == 1:
        return "Su"
    if num == 2:
        return "Mo"
    if num == 3:
        return "Me"
    if num == 4:
        return "Ma"
    if num == 5:
        return "Ju"
    if num == 6:
        return "Ve"
    if num == 7:
        return "Sa"
    if num == 8:
        return "Ra"
    if num == 9:
        return "Ke"
    if num == 10:
        return "As"

#finding values for degrees using house number
def pasp_table_degs():
    table = pd.DataFrame([
        [1, 7, 8, 5, 9, 4, 10, 3, 11],
        [2, 8, 9, 6, 10, 5, 11, 4, 12],
        [3, 9, 10, 7, 11, 6, 12, 5, 1],
        [4, 10, 11, 8, 12, 7, 1, 6, 2],
        [5, 11, 12, 9, 1, 8, 2, 7, 3],
        [6, 12, 1, 10, 2, 9, 3, 8, 4],
        [7, 1, 2, 11, 3, 10, 4, 9, 5],
        [8, 2, 3, 12, 4, 11, 5, 10, 6],
        [9, 3, 4, 1, 5, 12, 6, 11, 7],
        [10, 4, 5, 2, 6, 1, 7, 12, 8],
        [11, 5, 6, 3, 7, 2, 8, 1, 9],
        [12, 6, 7, 4, 8, 3, 9, 2, 10],
        # ["Conj", "180", ">150", "120<", ">120", "90<", ">90", "60<", ">60"],
    ], columns=["H", "180", "greater150", "120lesser", "greater120", "90lesser", "90greater","60lesser","60greater", ])
    return table

#finding value using sign name for sign aspects
def sign_table_degs():
    table = pd.DataFrame([
        [1, "Ar", "Ar", "Li", "Le", "Sg", "Ca", "Cp", "Ge", "Aq", "Sc"],
        [2, "Ta", "Ta", "Sc", "Vg", "Cp", "Le", "Aq", "Ca", "Pi", "Sg"],
        [3, "Ge", "Ge", "Sg", "Li", "Aq", "Vg", "Pi", "Le", "Ar", "Cp"],
        [4, "Ca", "Ca", "Cp", "Sc", "Pi", "Li", "Ar", "Vg", "Ta", "Aq"],
        [5, "Le", "Le", "Aq", "Sg", "Ar", "Sc", "Ta", "Li", "Ge", "Pi"],
        [6, "Vg", "Vg", "Pi", "Cp", "Ta", "Sg", "Ge", "Sc", "Ca", "Ar"],
        [7, "Li", "Li", "Ar", "Aq", "Ge", "Cp", "Ca", "Sg", "Le", "Ta"],
        [8, "Sc", "Sc", "Ta", "Pi", "Ca", "Aq", "Le", "Cp", "Vg", "Ge"],
        [9, "Sg", "Sg", "Ge", "Ar", "Le", "Pi", "Vg", "Aq", "Li", "Ca"],
        [10, "Cp", "Cp", "Ca", "Ta", "Vg", "Ar", "Li", "Pi", "Sc", "Le"],
        [11, "Aq", "Aq", "Le", "Ge", "Li", "Ta", "Sc", "Ar", "Sg", "Vg"],
        [12, "Pi", "Pi", "Vg", "Ca", "Sc", "Ge", "Sg", "Ta", "Cp", "Li"],
    ], columns=["sign_num","sign_name", "Conj", "180",  "120lesser", "greater120", "90lesser", "90greater","60lesser","60greater","greater150", ])
    table.set_index("sign_num")
    return table


#concatenation table for sign and house
def p1vsp2_concatenation_sign_house(sign_planet_house_df, pasp_table_df, sign_table_df, eve_person_two):
    p_s_h = sign_planet_house_df.copy()
    df2 = pasp_table_df.copy()
    df3 = sign_table_df.copy()
    event_p2 = eve_person_two.copy()
    Su_Conc_lst = []
    Mo_Conc_lst = []
    Me_Conc_lst = []
    Ma_Conc_lst = []
    Ju_Conc_lst = []
    Ve_Conc_lst = []
    Sa_Conc_lst = []
    Ra_Conc_lst = []
    Ke_Conc_lst = []
    As_Conc_lst = []
    df = pd.DataFrame(columns=['type'])
    type_list = ["Conj", "180", "120<" ,">120","90<" ,">90","60<",">60"]
    for i in type_list:
        lst = list_to_list_of_lists([i for j in range(10)])
        for k in lst:
            df.loc[len(df)] = k
    df.loc[len(df)] = [">150"]
    in_house_lst = p_s_h["house_num"].to_list()
    df['planet'] = (["Su", "Mo", "Me", "Ma", "Ju", "Ve", "Sa", "Ra", "Ke", "As"] * (len(df) // 2 + 1))[:len(df)]
    df['in_house'] = (in_house_lst * (len(df) // 2 + 1))[:len(df)]
    df.loc[df['type'] == ">150", 'in_house'] = df.iloc[73, df.columns.get_loc("in_house")]
    lst = []
    for index, row in df.iterrows():
        if row.type == "Conj":
            lst.append(row.in_house)
        elif row.type == "180":
            lst.append(df2.iloc[(row.in_house) - 1, df2.columns.get_loc("180")])
        elif row.type == ">150":
            lst.append(df2.iloc[(row.in_house) - 1, df2.columns.get_loc("greater150")])
        elif row.type == "120<":
            lst.append(df2.iloc[(row.in_house) - 1, df2.columns.get_loc("120lesser")])
        elif row.type == ">120":
            lst.append(df2.iloc[(row.in_house) - 1, df2.columns.get_loc("greater120")])
        elif row.type == "90<":
            lst.append(df2.iloc[(row.in_house) - 1, df2.columns.get_loc("90lesser")])
        elif row.type == ">90":
            lst.append(df2.iloc[(row.in_house) - 1, df2.columns.get_loc("90greater")])
        elif row.type == "60<":
            lst.append(df2.iloc[(row.in_house) - 1, df2.columns.get_loc("60lesser")])
        elif row.type == ">60":
            lst.append(df2.iloc[(row.in_house) - 1, df2.columns.get_loc("60greater")])

    df["he_with_aspect"] = lst
    sign_lst = p_s_h["sign_name"].to_list()
    df['sign_he'] = (sign_lst * (len(df) // 2 + 1))[:len(df)]
    df.loc[df['type'] == ">150", 'sign_he'] = df.iloc[73, df.columns.get_loc("sign_he")]
    s_lst = []
    for index, row in df.iterrows():
        check_sign = 0
        if row.sign_he == "Ar":
            check_sign = 1
        elif row.sign_he == "Ta":
            check_sign = 2
        elif row.sign_he == "Ge":
            check_sign = 3
        elif row.sign_he == "Ca":
            check_sign = 4
        elif row.sign_he == "Le":
            check_sign = 5
        elif row.sign_he == "Vg":
            check_sign = 6
        elif row.sign_he == "Li":
            check_sign = 7
        elif row.sign_he == "Sc":
            check_sign = 8
        elif row.sign_he == "Sg":
            check_sign = 9
        elif row.sign_he == "Cp":
            check_sign = 10
        elif row.sign_he == "Aq":
            check_sign = 11
        elif row.sign_he == "Pi":
            check_sign = 12
        if row.type == "Conj":
            s_lst.append(df3.iloc[check_sign- 1, df3.columns.get_loc("Conj")])
        elif row.type == "180":
            s_lst.append(df3.iloc[check_sign- 1, df3.columns.get_loc("180")])
        elif row.type == ">150":
            s_lst.append(df3.iloc[check_sign - 1, df3.columns.get_loc("greater150")])
        elif row.type == "120<":
            s_lst.append(df3.iloc[check_sign - 1, df3.columns.get_loc("120lesser")])
        elif row.type == ">120":
            s_lst.append(df3.iloc[check_sign - 1, df3.columns.get_loc("greater120")])
        elif row.type == "90<":
            s_lst.append(df3.iloc[check_sign - 1, df3.columns.get_loc("90lesser")])
        elif row.type == ">90":
            s_lst.append(df3.iloc[check_sign - 1, df3.columns.get_loc("90greater")])
        elif row.type == "60<":
            s_lst.append(df3.iloc[check_sign - 1, df3.columns.get_loc("60lesser")])
        elif row.type == ">60":
            s_lst.append(df3.iloc[check_sign - 1, df3.columns.get_loc("60greater")])
    df["sign_he_aspect"] = s_lst
    sign_she_lst = event_p2["sign_name"].to_list()
    df['sign_she'] = (sign_she_lst * (len(df) // 2 + 1))[:len(df)]
    df.loc[df['type'] == ">150", 'sign_she'] = df.iloc[73, df.columns.get_loc("sign_she")]
    count = 0
    for index, row in df.iterrows():
        if row.type == ">150":
            Su_Conc_lst.append(0)
            Mo_Conc_lst.append(0)
            Me_Conc_lst.append(0)
            Ma_Conc_lst.append(0)
            Ju_Conc_lst.append(0)
            Ve_Conc_lst.append(0)
            Sa_Conc_lst.append(0)
            Ra_Conc_lst.append(0)
            Ke_Conc_lst.append(0)
            As_Conc_lst.append(0)
        else:
            count += 1
            planet_count = 0
            for i in sign_she_lst:
                planet_count += 1
                if count == 1:
                    if row.sign_he_aspect == i:
                        Su_Conc_lst.append(str(row.sign_he+ row.planet+i+planet_num_check(planet_count)))
                    else:
                        Su_Conc_lst.append(0)
                if count == 2:
                    if row.sign_he_aspect == i:
                        Mo_Conc_lst.append(str(row.sign_he+ row.planet+i+planet_num_check(planet_count)))
                    else:
                        Mo_Conc_lst.append(0)
                if count == 3:
                    if row.sign_he_aspect == i:
                        Me_Conc_lst.append(str(row.sign_he+ row.planet+i+planet_num_check(planet_count)))
                    else:
                        Me_Conc_lst.append(0)
                if count == 4:
                    if row.sign_he_aspect == i:
                        Ma_Conc_lst.append(str(row.sign_he+ row.planet+i+planet_num_check(planet_count)))
                    else:
                        Ma_Conc_lst.append(0)
                if count == 5:
                    if row.sign_he_aspect == i:
                        Ju_Conc_lst.append(str(row.sign_he+ row.planet+i+planet_num_check(planet_count)))
                    else:
                        Ju_Conc_lst.append(0)
                if count == 6:
                    if row.sign_he_aspect == i:
                        Ve_Conc_lst.append(str(row.sign_he+ row.planet+i+planet_num_check(planet_count)))
                    else:
                        Ve_Conc_lst.append(0)
                if count == 7:
                    if row.sign_he_aspect == i:
                        Sa_Conc_lst.append(str(row.sign_he+ row.planet+i+planet_num_check(planet_count)))
                    else:
                        Sa_Conc_lst.append(0)
                if count == 8:
                    if row.sign_he_aspect == i:
                        Ra_Conc_lst.append(str(row.sign_he+ row.planet+i+planet_num_check(planet_count)))
                    else:
                        Ra_Conc_lst.append(0)
                if count == 9:
                    if row.sign_he_aspect == i:
                        Ke_Conc_lst.append(str(row.sign_he+ row.planet+i+planet_num_check(planet_count)))
                    else:
                        Ke_Conc_lst.append(0)
                if count == 10:
                    if row.sign_he_aspect == i:
                        As_Conc_lst.append(str(row.sign_he+ row.planet+i+planet_num_check(planet_count)))
                    else:
                        As_Conc_lst.append(0)
                if count == 10 and planet_count == 10:
                    count = 0

    df.loc[df.type == ">150", "planet"] = "Ma"
    for index,row in df.iterrows():
        if row.type == ">150":
            p_count = 0
            for i in sign_she_lst:
                p_count += 1
                if row.sign_he_aspect == i:
                    if p_count == 1:
                        Su_Conc_lst[-1] = (str(row.sign_he+ row.planet+i+planet_num_check(p_count)))
                    elif p_count == 2:
                        Mo_Conc_lst[-1] = (str(row.sign_he+ row.planet+i+planet_num_check(p_count)))
                    elif p_count == 3:
                        Me_Conc_lst[-1] = (str(row.sign_he+ row.planet+i+planet_num_check(p_count)))
                    elif p_count == 4:
                        Ma_Conc_lst[-1] = (str(row.sign_he+ row.planet+i+planet_num_check(p_count)))
                    elif p_count == 5:
                        Ju_Conc_lst[-1] = (str(row.sign_he+ row.planet+i+planet_num_check(p_count)))
                    elif p_count == 6:
                        Ve_Conc_lst[-1] = (str(row.sign_he+ row.planet+i+planet_num_check(p_count)))
                    elif p_count == 7:
                        Sa_Conc_lst[-1] = (str(row.sign_he+ row.planet+i+planet_num_check(p_count)))
                    elif p_count == 8:
                        Ra_Conc_lst[-1] = (str(row.sign_he+ row.planet+i+planet_num_check(p_count)))
                    elif p_count == 9:
                        Ke_Conc_lst[-1] = (str(row.sign_he+ row.planet+i+planet_num_check(p_count)))
                    elif p_count == 10:
                        As_Conc_lst[-1] = (str(row.sign_he+ row.planet+i+planet_num_check(p_count)))
    df["Su_Conc"] = Su_Conc_lst
    df["Mo_Conc"] = Mo_Conc_lst
    df["Me_Conc"] = Me_Conc_lst
    df["Ma_Conc"] = Ma_Conc_lst
    df["Ju_Conc"] = Ju_Conc_lst
    df["Ve_Conc"] =  Ve_Conc_lst
    df["Sa_Conc"] = Sa_Conc_lst
    df["Ra_Conc"] = Ra_Conc_lst
    df["Ke_Conc"] = Ke_Conc_lst
    df["As_Conc"] = As_Conc_lst
    df.loc[(df.type != "Conj") , "As_Conc"] = 0
    df.loc[df.type != "Conj", "Ke_Conc"] = 0
    df.loc[df.type == "180", "Ra_Conc"] = 0
    # df.loc[df.type == ">150", "Ra_Conc"] = 0
    return df

#getting concatenation points from the database
def concatenation_points_database():
    db = concatenation_points.objects.all()
    db = read_frame(db)
    return db


#point table for concatenation of sign and planets
def p1vsp2_points_table(con_sign_planet_df, point_planet_aspects_df):
    df = con_sign_planet_df.copy()
    df2 = point_planet_aspects_df.copy()
    db = concatenation_points_database()
    Su_point_lst = []
    Mo_point_lst = []
    Me_point_lst = []
    Ma_point_lst = []
    Ju_point_lst = []
    Ve_point_lst = []
    Sa_point_lst = []
    Ra_point_lst = []
    Ke_point_lst = []
    As_point_lst = []
    for index, row in df.iterrows():
        if row.Su_Conc != 0:
            Su_point_lst.append((db[db['con_type'].isin([row.type]) & db['con_name'].isin([row.Su_Conc])].con_points.values)[0])
        else:
            Su_point_lst.append(0)

        if row.Mo_Conc != 0:
            Mo_point_lst.append((db[db['con_type'].isin([row.type]) & db['con_name'].isin([row.Mo_Conc])].con_points.values)[0])
        else:
            Mo_point_lst.append(0)


        if row.Me_Conc != 0:
            Me_point_lst.append((db[db['con_type'].isin([row.type]) & db['con_name'].isin([row.Me_Conc])].con_points.values)[0])
        else:
            Me_point_lst.append(0)


        if row.Ma_Conc != 0:
            Ma_point_lst.append((db[db['con_type'].isin([row.type]) & db['con_name'].isin([row.Ma_Conc])].con_points.values)[0])
        else:
            Ma_point_lst.append(0)


        if row.Ju_Conc != 0:
            Ju_point_lst.append((db[db['con_type'].isin([row.type]) & db['con_name'].isin([row.Ju_Conc])].con_points.values)[0])
        else:
            Ju_point_lst.append(0)


        if row.Ve_Conc != 0:
            Ve_point_lst.append((db[db['con_type'].isin([row.type]) & db['con_name'].isin([row.Ve_Conc])].con_points.values)[0])
        else:
            Ve_point_lst.append(0)


        if row.Sa_Conc != 0:
            Sa_point_lst.append((db[db['con_type'].isin([row.type]) & db['con_name'].isin([row.Sa_Conc])].con_points.values)[0])
        else:
            Sa_point_lst.append(0)


        if row.Ra_Conc != 0:
            Ra_point_lst.append((db[db['con_type'].isin([row.type]) & db['con_name'].isin([row.Ra_Conc])].con_points.values)[0])
        else:
            Ra_point_lst.append(0)


        if row.Ke_Conc != 0:
            Ke_point_lst.append((db[db['con_type'].isin([row.type]) & db['con_name'].isin([row.Ke_Conc])].con_points.values)[0])
        else:
            Ke_point_lst.append(0)


        if row.As_Conc != 0:
            As_point_lst.append((db[db['con_type'].isin([row.type]) & db['con_name'].isin([row.As_Conc])].con_points.values)[0])
        else:
            As_point_lst.append(0)
    df["Su_Point"] = Su_point_lst
    df["Mo_Point"] = Mo_point_lst
    df["Me_Point"] = Me_point_lst
    df["Ma_Point"] = Ma_point_lst
    df["Ju_Point"] = Ju_point_lst
    df["Ve_Point"] = Ve_point_lst
    df["Sa_Point"] = Sa_point_lst
    df["Ra_Point"] = Ra_point_lst
    df["Ke_Point"] = Ke_point_lst
    df["As_Point"] = As_point_lst
    Su_point_lst_v2 = []
    Mo_point_lst_v2 = []
    Me_point_lst_v2 = []
    Ma_point_lst_v2 = []
    Ju_point_lst_v2 = []
    Ve_point_lst_v2 = []
    Sa_point_lst_v2 = []
    Ra_point_lst_v2 = []
    Ke_point_lst_v2 = []
    As_point_lst_v2 = []
    for index, row in df.iterrows():
        if (row.Su_Point) != 0:
            Su_point_lst_v2.append(row.Su_Point + df2.consolidate[0])
        else:
            Su_point_lst_v2.append(0)

        if (row.Mo_Point) != 0:
            Mo_point_lst_v2.append(row.Mo_Point + df2.consolidate[1])
        else:
            Mo_point_lst_v2.append(0)

        if (row.Me_Point) != 0:
            Me_point_lst_v2.append(row.Me_Point + df2.consolidate[2])
        else:
            Me_point_lst_v2.append(0)

        if (row.Ma_Point) != 0:
            Ma_point_lst_v2.append(row.Ma_Point + df2.consolidate[3])
        else:
            Ma_point_lst_v2.append(0)

        if (row.Ju_Point) != 0:
            Ju_point_lst_v2.append(row.Ju_Point + df2.consolidate[4])
        else:
            Ju_point_lst_v2.append(0)

        if (row.Ve_Point) != 0:
            Ve_point_lst_v2.append(row.Ve_Point + df2.consolidate[5])
        else:
            Ve_point_lst_v2.append(0)

        if (row.Sa_Point) != 0:
            Sa_point_lst_v2.append(row.Sa_Point + df2.consolidate[6])
        else:
            Sa_point_lst_v2.append(0)

        if (row.Ra_Point) != 0:
            Ra_point_lst_v2.append(row.Ra_Point + df2.consolidate[7])
        else:
            Ra_point_lst_v2.append(0)

        if (row.Ke_Point) != 0:
            Ke_point_lst_v2.append(row.Ke_Point + df2.consolidate[8])
        else:
            Ke_point_lst_v2.append(0)

        if (row.As_Point) != 0:
            As_point_lst_v2.append(row.As_Point + df2.consolidate[9])
        else:
            As_point_lst_v2.append(0)
    if (Su_point_lst_v2[-1]) != 0:
        Su_point_lst_v2[-1] = Su_point_lst_v2[-1] * 0.6
    if (Mo_point_lst_v2[-1]) != 0:
        Mo_point_lst_v2[-1] = Mo_point_lst_v2[-1] * 0.6
    if (Me_point_lst_v2[-1]) != 0:
        Me_point_lst_v2[-1] = Me_point_lst_v2[-1] * 0.6
    if (Ma_point_lst_v2[-1]) != 0:
        Ma_point_lst_v2[-1] = Ma_point_lst_v2[-1] * 0.6
    if (Ju_point_lst_v2[-1]) != 0:
        Ju_point_lst_v2[-1] = Ju_point_lst_v2[-1] * 0.6
    if (Ve_point_lst_v2[-1]) != 0:
        Ve_point_lst_v2[-1] = Ve_point_lst_v2[-1] * 0.6
    if (Sa_point_lst_v2[-1]) != 0:
        Sa_point_lst_v2[-1] = Sa_point_lst_v2[-1] * 0.6
    if (Ra_point_lst_v2[-1]) != 0:
        Ra_point_lst_v2[-1] = Ra_point_lst_v2[-1] * 0.6
    if (Ke_point_lst_v2[-1]) != 0:
        Ke_point_lst_v2[-1] = Ke_point_lst_v2[-1] * 0.6
    if (As_point_lst_v2[-1]) != 0:
        As_point_lst_v2[-1] = As_point_lst_v2[-1] * 0.6
    df["Su_Point"] = Su_point_lst_v2
    df["Mo_Point"] = Mo_point_lst_v2
    df["Me_Point"] = Me_point_lst_v2
    df["Ma_Point"] = Ma_point_lst_v2
    df["Ju_Point"] = Ju_point_lst_v2
    df["Ve_Point"] = Ve_point_lst_v2
    df["Sa_Point"] = Sa_point_lst_v2
    df["Ra_Point"] = Ra_point_lst_v2
    df["Ke_Point"] = Ke_point_lst_v2
    df["As_Point"] = As_point_lst_v2
    df["total"]  = df["Su_Point"] + df["Mo_Point"] + df["Me_Point"] + df["Ma_Point"] + df["Ju_Point"] + df["Ve_Point"] + df["Sa_Point"] + df["Ra_Point"] + df["Ke_Point"] + df["As_Point"]
    df.loc[df['type'] == ">150", 'sign_she'] = "Ma"
    df.loc[df['type'] == ">150", 'planet'] = "Ma"
    return df

def p1vsp2_sep_degree(eve_person_one, eve_person_two):
    df = pd.DataFrame()
    df["planet"] = eve_person_one["planet"].to_list()
    df["p1_degrees"] = eve_person_one["degree"].to_list()
    df["p2_degrees"] = eve_person_two["degree"].to_list()
    return df

def p1xp2_distance_table(con_sign_planet_df, sep_degree_df):
    df1 = con_sign_planet_df.copy()
    df2 = sep_degree_df.copy()
    Su_Dis_lst = []
    Mo_Dis_lst = []
    Me_Dis_lst = []
    Ma_Dis_lst = []
    Ju_Dis_lst = []
    Ve_Dis_lst = []
    Sa_Dis_lst = []
    Ra_Dis_lst = []
    Ke_Dis_lst = []
    As_Dis_lst = []
    row_count = 0
    for index, row in df1.iterrows():
        row_count += 1
        if row.type == "Conj":
            if len(str(row.Su_Conc)) > 1:
                Su_Dis_lst.append(df2["p1_degrees"][0] - df2["p2_degrees"][row_count-1])
            else:
                Su_Dis_lst.append(0)

            if len(str(row.Mo_Conc)) > 1:
                Mo_Dis_lst.append(df2["p1_degrees"][1] - df2["p2_degrees"][row_count-1])
            else:
                Mo_Dis_lst.append(0)
            if len(str(row.Me_Conc)) > 1:
                Me_Dis_lst.append(df2["p1_degrees"][2] - df2["p2_degrees"][row_count-1])
            else:
                Me_Dis_lst.append(0)
            if len(str(row.Ma_Conc)) > 1:
                Ma_Dis_lst.append(df2["p1_degrees"][3] - df2["p2_degrees"][row_count-1])
            else:
                Ma_Dis_lst.append(0)
            if len(str(row.Ju_Conc)) > 1:
                Ju_Dis_lst.append(df2["p1_degrees"][4] - df2["p2_degrees"][row_count-1])
            else:
                Ju_Dis_lst.append(0)
            if len(str(row.Ve_Conc)) > 1:
                Ve_Dis_lst.append(df2["p1_degrees"][5] - df2["p2_degrees"][row_count-1])
            else:
                Ve_Dis_lst.append(0)
            if len(str(row.Sa_Conc)) > 1:
                Sa_Dis_lst.append(df2["p1_degrees"][6] - df2["p2_degrees"][row_count-1])
            else:
                Sa_Dis_lst.append(0)
            if len(str(row.Ra_Conc)) > 1:
                Ra_Dis_lst.append(df2["p1_degrees"][7] - df2["p2_degrees"][row_count-1])
            else:
                Ra_Dis_lst.append(0)
            if len(str(row.Ke_Conc)) > 1:
                Ke_Dis_lst.append(df2["p1_degrees"][8] - df2["p2_degrees"][row_count-1])
            else:
                Ke_Dis_lst.append(0)
            if len(str(row.As_Conc)) > 1:
                As_Dis_lst.append(df2["p1_degrees"][9] - df2["p2_degrees"][row_count-1])
            else:
                As_Dis_lst.append(0)
            if row_count == 10:
                row_count = 0
        if row.type == "180":
            if len(str(row.Su_Conc)) > 1:
                if df2["p1_degrees"][0] > df2["p2_degrees"][row_count-1]:
                    Su_Dis_lst.append(df2["p1_degrees"][0] - (df2["p2_degrees"][row_count-1]+ 180))
                if df2["p1_degrees"][0] < df2["p2_degrees"][row_count-1]:
                    Su_Dis_lst.append(df2["p2_degrees"][row_count-1] - (df2["p1_degrees"][0] + 180))
            else:
                Su_Dis_lst.append(0)

            if len(str(row.Mo_Conc)) > 1:
                if df2["p1_degrees"][1] > df2["p2_degrees"][row_count - 1]:
                    Mo_Dis_lst.append(df2["p1_degrees"][1] - (df2["p2_degrees"][row_count - 1] + 180))
                if df2["p1_degrees"][1] < df2["p2_degrees"][row_count - 1]:
                    Mo_Dis_lst.append(df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][1] + 180))
            else:
                Mo_Dis_lst.append(0)
            if len(str(row.Me_Conc)) > 1:
                if (df2["p1_degrees"][2]) > (df2["p2_degrees"][row_count - 1]):
                    Me_Dis_lst.append(df2["p1_degrees"][2] - (df2["p2_degrees"][row_count - 1] + 180))
                if df2["p1_degrees"][2] < df2["p2_degrees"][row_count - 1]:
                    Me_Dis_lst.append(df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][2] + 180))
            else:
                Me_Dis_lst.append(0)
            if len(str(row.Ma_Conc)) > 1:
                if df2["p1_degrees"][3] > df2["p2_degrees"][row_count - 1]:
                    Ma_Dis_lst.append(df2["p1_degrees"][3] - (df2["p2_degrees"][row_count - 1] + 180))
                if df2["p1_degrees"][3] < df2["p2_degrees"][row_count - 1]:
                    Ma_Dis_lst.append(df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][3] + 180))
            else:
                Ma_Dis_lst.append(0)
            if len(str(row.Ju_Conc)) > 1:
                if df2["p1_degrees"][4] > df2["p2_degrees"][row_count - 1]:
                    Ju_Dis_lst.append(df2["p1_degrees"][4] - (df2["p2_degrees"][row_count - 1] + 180))
                if df2["p1_degrees"][4] < df2["p2_degrees"][row_count - 1]:
                    Ju_Dis_lst.append(df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][4] + 180))
            else:
                Ju_Dis_lst.append(0)
            if len(str(row.Ve_Conc)) > 1:
                if df2["p1_degrees"][5] > df2["p2_degrees"][row_count - 1]:
                    Ve_Dis_lst.append(df2["p1_degrees"][5] - (df2["p2_degrees"][row_count - 1] + 180))
                if df2["p1_degrees"][5] < df2["p2_degrees"][row_count - 1]:
                    Ve_Dis_lst.append(df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][5] + 180))
            else:
                Ve_Dis_lst.append(0)
            if len(str(row.Sa_Conc)) > 1:
                if df2["p1_degrees"][6] > df2["p2_degrees"][row_count - 1]:
                    Sa_Dis_lst.append(df2["p1_degrees"][6] - (df2["p2_degrees"][row_count - 1] + 180))
                if df2["p1_degrees"][6] < df2["p2_degrees"][row_count - 1]:
                    Sa_Dis_lst.append(df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][6] + 180))
            else:
                Sa_Dis_lst.append(0)
            if len(str(row.Ra_Conc)) > 1:
                if df2["p1_degrees"][7] > df2["p2_degrees"][row_count - 1]:
                    Ra_Dis_lst.append(df2["p1_degrees"][7] - (df2["p2_degrees"][row_count - 1] + 180))
                if df2["p1_degrees"][7] < df2["p2_degrees"][row_count - 1]:
                    Ra_Dis_lst.append(df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][7] + 180))
            else:
                Ra_Dis_lst.append(0)
            if len(str(row.Ke_Conc)) > 1:
                if df2["p1_degrees"][8] > df2["p2_degrees"][row_count - 1]:
                    Ke_Dis_lst.append(df2["p1_degrees"][8] - (df2["p2_degrees"][row_count - 1] + 180))
                if df2["p1_degrees"][8] < df2["p2_degrees"][row_count - 1]:
                    Ke_Dis_lst.append(df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][8] + 180))
            else:
                Ke_Dis_lst.append(0)
            if len(str(row.As_Conc)) > 1:
                if df2["p1_degrees"][9] > df2["p2_degrees"][row_count - 1]:
                    As_Dis_lst.append(df2["p1_degrees"][9] - (df2["p2_degrees"][row_count - 1] + 180))
                if df2["p1_degrees"][9] < df2["p2_degrees"][row_count - 1]:
                    As_Dis_lst.append(df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][9] + 180))
            else:
                As_Dis_lst.append(0)
            if row_count == 10:
                row_count = 0
        if row.type == "120<":
            if len(str(row.Su_Conc)) > 1:
                if df2["p1_degrees"][0] > df2["p2_degrees"][row_count-1]:
                    temp = df2["p1_degrees"][0] - (df2["p2_degrees"][row_count-1]+ 240)
                    Su_Dis_lst.append(temp)
                if df2["p1_degrees"][0] < df2["p2_degrees"][row_count-1]:
                    temp = df2["p2_degrees"][row_count-1] - (df2["p1_degrees"][0] + 120)
                    Su_Dis_lst.append(temp * -1)
            else:
                Su_Dis_lst.append(0)
            if len(str(row.Mo_Conc)) > 1:
                if df2["p1_degrees"][1] > df2["p2_degrees"][row_count - 1]:
                    Mo_Dis_lst.append((df2["p1_degrees"][1] - (df2["p2_degrees"][row_count - 1] + 240)))
                if df2["p1_degrees"][1] < df2["p2_degrees"][row_count - 1]:
                    Mo_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][1] + 120)) * -1)
            else:
                Mo_Dis_lst.append(0)
            if len(str(row.Me_Conc)) > 1:
                if (df2["p1_degrees"][2]) > (df2["p2_degrees"][row_count - 1]):
                    Me_Dis_lst.append(df2["p1_degrees"][2] - (df2["p2_degrees"][row_count - 1] + 240))
                if df2["p1_degrees"][2] < df2["p2_degrees"][row_count - 1]:
                    Me_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][2] + 120)) * -1)
            else:
                Me_Dis_lst.append(0)
            if len(str(row.Ma_Conc)) > 1:
                if df2["p1_degrees"][3] > df2["p2_degrees"][row_count - 1]:
                    Ma_Dis_lst.append(df2["p1_degrees"][3] - (df2["p2_degrees"][row_count - 1] + 240))
                if df2["p1_degrees"][3] < df2["p2_degrees"][row_count - 1]:
                    Ma_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][3] + 120)) * -1)
            else:
                Ma_Dis_lst.append(0)
            if len(str(row.Ju_Conc)) > 1:
                if df2["p1_degrees"][4] > df2["p2_degrees"][row_count - 1]:
                    Ju_Dis_lst.append(df2["p1_degrees"][4] - (df2["p2_degrees"][row_count - 1] + 240))
                if df2["p1_degrees"][4] < df2["p2_degrees"][row_count - 1]:
                    Ju_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][4] + 120)) * -1)
            else:
                Ju_Dis_lst.append(0)
            if len(str(row.Ve_Conc)) > 1:
                if df2["p1_degrees"][5] > df2["p2_degrees"][row_count - 1]:
                    Ve_Dis_lst.append(df2["p1_degrees"][5] - (df2["p2_degrees"][row_count - 1] + 240))
                if df2["p1_degrees"][5] < df2["p2_degrees"][row_count - 1]:
                    Ve_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][5] + 120)) * -1)
            else:
                Ve_Dis_lst.append(0)
            if len(str(row.Sa_Conc)) > 1:
                if df2["p1_degrees"][6] > df2["p2_degrees"][row_count - 1]:
                    Sa_Dis_lst.append(df2["p1_degrees"][6] - (df2["p2_degrees"][row_count - 1] + 240))
                if df2["p1_degrees"][6] < df2["p2_degrees"][row_count - 1]:
                    Sa_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][6] + 120)) * -1)
            else:
                Sa_Dis_lst.append(0)
            if len(str(row.Ra_Conc)) > 1:
                if df2["p1_degrees"][7] > df2["p2_degrees"][row_count - 1]:
                    Ra_Dis_lst.append(df2["p1_degrees"][7] - (df2["p2_degrees"][row_count - 1] + 240))
                if df2["p1_degrees"][7] < df2["p2_degrees"][row_count - 1]:
                    Ra_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][7] + 120)) * -1)
            else:
                Ra_Dis_lst.append(0)
            if len(str(row.Ke_Conc)) > 1:
                if df2["p1_degrees"][8] > df2["p2_degrees"][row_count - 1]:
                    Ke_Dis_lst.append(df2["p1_degrees"][8] - (df2["p2_degrees"][row_count - 1] + 240))
                if df2["p1_degrees"][8] < df2["p2_degrees"][row_count - 1]:
                    Ke_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][8] + 120))*  -1)
            else:
                Ke_Dis_lst.append(0)
            if len(str(row.As_Conc)) > 1:
                if df2["p1_degrees"][9] > df2["p2_degrees"][row_count - 1]:
                    As_Dis_lst.append((df2["p1_degrees"][9] - (df2["p2_degrees"][row_count - 1] + 240)))
                if df2["p1_degrees"][9] < df2["p2_degrees"][row_count - 1]:
                    As_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][9] + 120)) *-1)
            else:
                As_Dis_lst.append(0)
            if row_count == 10:
                row_count = 0

        if row.type == ">120":
            if len(str(row.Su_Conc)) > 1:
                if df2["p1_degrees"][0] > df2["p2_degrees"][row_count-1]:
                    temp = df2["p1_degrees"][0] - (df2["p2_degrees"][row_count-1]+ 120)
                    Su_Dis_lst.append(temp)
                if df2["p1_degrees"][0] < df2["p2_degrees"][row_count-1]:
                    temp = df2["p2_degrees"][row_count-1] - (df2["p1_degrees"][0] + 240)
                    Su_Dis_lst.append(temp * -1)
            else:
                Su_Dis_lst.append(0)

            if len(str(row.Mo_Conc)) > 1:
                if df2["p1_degrees"][1] > df2["p2_degrees"][row_count - 1]:
                    Mo_Dis_lst.append((df2["p1_degrees"][1] - (df2["p2_degrees"][row_count - 1] + 120)))
                if df2["p1_degrees"][1] < df2["p2_degrees"][row_count - 1]:
                    Mo_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][1] + 240)) * -1)
            else:
                Mo_Dis_lst.append(0)
            if len(str(row.Me_Conc)) > 1:
                if (df2["p1_degrees"][2]) > (df2["p2_degrees"][row_count - 1]):
                    Me_Dis_lst.append(df2["p1_degrees"][2] - (df2["p2_degrees"][row_count - 1] + 120))
                if df2["p1_degrees"][2] < df2["p2_degrees"][row_count - 1]:
                    Me_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][2] + 240)) * -1)
            else:
                Me_Dis_lst.append(0)
            if len(str(row.Ma_Conc)) > 1:
                if df2["p1_degrees"][3] > df2["p2_degrees"][row_count - 1]:
                    Ma_Dis_lst.append(df2["p1_degrees"][3] - (df2["p2_degrees"][row_count - 1] + 120))
                if df2["p1_degrees"][3] < df2["p2_degrees"][row_count - 1]:
                    Ma_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][3] + 240)) * -1)
            else:
                Ma_Dis_lst.append(0)
            if len(str(row.Ju_Conc)) > 1:
                if df2["p1_degrees"][4] > df2["p2_degrees"][row_count - 1]:
                    Ju_Dis_lst.append(df2["p1_degrees"][4] - (df2["p2_degrees"][row_count - 1] + 120))
                if df2["p1_degrees"][4] < df2["p2_degrees"][row_count - 1]:
                    Ju_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][4] + 240)) * -1)
            else:
                Ju_Dis_lst.append(0)
            if len(str(row.Ve_Conc)) > 1:
                if df2["p1_degrees"][5] > df2["p2_degrees"][row_count - 1]:
                    Ve_Dis_lst.append(df2["p1_degrees"][5] - (df2["p2_degrees"][row_count - 1] + 120))
                if df2["p1_degrees"][5] < df2["p2_degrees"][row_count - 1]:
                    Ve_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][5] + 240)) * -1)
            else:
                Ve_Dis_lst.append(0)
            if len(str(row.Sa_Conc)) > 1:
                if df2["p1_degrees"][6] > df2["p2_degrees"][row_count - 1]:
                    Sa_Dis_lst.append(df2["p1_degrees"][6] - (df2["p2_degrees"][row_count - 1] + 120))
                if df2["p1_degrees"][6] < df2["p2_degrees"][row_count - 1]:
                    Sa_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][6] + 240)) * -1)
            else:
                Sa_Dis_lst.append(0)
            if len(str(row.Ra_Conc)) > 1:
                if df2["p1_degrees"][7] > df2["p2_degrees"][row_count - 1]:
                    Ra_Dis_lst.append(df2["p1_degrees"][7] - (df2["p2_degrees"][row_count - 1] + 120))
                if df2["p1_degrees"][7] < df2["p2_degrees"][row_count - 1]:
                    Ra_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][7] + 240)) * -1)
            else:
                Ra_Dis_lst.append(0)
            if len(str(row.Ke_Conc)) > 1:
                if df2["p1_degrees"][8] > df2["p2_degrees"][row_count - 1]:
                    Ke_Dis_lst.append(df2["p1_degrees"][8] - (df2["p2_degrees"][row_count - 1] + 120))
                if df2["p1_degrees"][8] < df2["p2_degrees"][row_count - 1]:
                    Ke_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][8] + 240))*  -1)
            else:
                Ke_Dis_lst.append(0)
            if len(str(row.As_Conc)) > 1:
                if df2["p1_degrees"][9] > df2["p2_degrees"][row_count - 1]:
                    As_Dis_lst.append((df2["p1_degrees"][9] - (df2["p2_degrees"][row_count - 1] + 120)))
                if df2["p1_degrees"][9] < df2["p2_degrees"][row_count - 1]:
                    As_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][9] + 240)) *-1)
            else:
                As_Dis_lst.append(0)
            if row_count == 10:
                row_count = 0
        if row.type == "90<":
            if len(str(row.Su_Conc)) > 1:
                if df2["p1_degrees"][0] > df2["p2_degrees"][row_count-1]:
                    temp = df2["p1_degrees"][0] - (df2["p2_degrees"][row_count-1]+ 270)
                    Su_Dis_lst.append(temp)
                if df2["p1_degrees"][0] < df2["p2_degrees"][row_count-1]:
                    temp = df2["p2_degrees"][row_count-1] - (df2["p1_degrees"][0] + 90)
                    Su_Dis_lst.append(temp * -1)
            else:
                Su_Dis_lst.append(0)
            if len(str(row.Mo_Conc)) > 1:
                if df2["p1_degrees"][1] > df2["p2_degrees"][row_count - 1]:
                    Mo_Dis_lst.append((df2["p1_degrees"][1] - (df2["p2_degrees"][row_count - 1] + 270)))
                if df2["p1_degrees"][1] < df2["p2_degrees"][row_count - 1]:
                    Mo_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][1] + 90)) * -1)
            else:
                Mo_Dis_lst.append(0)
            if len(str(row.Me_Conc)) > 1:
                if (df2["p1_degrees"][2]) > (df2["p2_degrees"][row_count - 1]):
                    Me_Dis_lst.append((df2["p1_degrees"][2] - (df2["p2_degrees"][row_count - 1] + 270)))
                if df2["p1_degrees"][2] < df2["p2_degrees"][row_count - 1]:
                    Me_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][2] + 90)) * -1)
            else:
                Me_Dis_lst.append(0)
            if len(str(row.Ma_Conc)) > 1:
                if df2["p1_degrees"][3] > df2["p2_degrees"][row_count - 1]:
                    Ma_Dis_lst.append(df2["p1_degrees"][3] - (df2["p2_degrees"][row_count - 1] + 270))
                if df2["p1_degrees"][3] < df2["p2_degrees"][row_count - 1]:
                    Ma_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][3] + 90)) * -1)
            else:
                Ma_Dis_lst.append(0)
            if len(str(row.Ju_Conc)) > 1:
                if df2["p1_degrees"][4] > df2["p2_degrees"][row_count - 1]:
                    Ju_Dis_lst.append(df2["p1_degrees"][4] - (df2["p2_degrees"][row_count - 1] + 270))
                if df2["p1_degrees"][4] < df2["p2_degrees"][row_count - 1]:
                    Ju_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][4] + 90)) * -1)
            else:
                Ju_Dis_lst.append(0)
            if len(str(row.Ve_Conc)) > 1:
                if df2["p1_degrees"][5] > df2["p2_degrees"][row_count - 1]:
                    Ve_Dis_lst.append(df2["p1_degrees"][5] - (df2["p2_degrees"][row_count - 1] + 270))
                if df2["p1_degrees"][5] < df2["p2_degrees"][row_count - 1]:
                    Ve_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][5] + 90)) * -1)
            else:
                Ve_Dis_lst.append(0)
            if len(str(row.Sa_Conc)) > 1:
                if df2["p1_degrees"][6] > df2["p2_degrees"][row_count - 1]:
                    Sa_Dis_lst.append(df2["p1_degrees"][6] - (df2["p2_degrees"][row_count - 1] + 270))
                if df2["p1_degrees"][6] < df2["p2_degrees"][row_count - 1]:
                    Sa_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][6] + 90)) * -1)
            else:
                Sa_Dis_lst.append(0)
            if len(str(row.Ra_Conc)) > 1:
                if df2["p1_degrees"][7] > df2["p2_degrees"][row_count - 1]:
                    Ra_Dis_lst.append(df2["p1_degrees"][7] - (df2["p2_degrees"][row_count - 1] + 270))
                if df2["p1_degrees"][7] < df2["p2_degrees"][row_count - 1]:
                    Ra_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][7] + 90)) * -1)
            else:
                Ra_Dis_lst.append(0)
            if len(str(row.Ke_Conc)) > 1:
                if df2["p1_degrees"][8] > df2["p2_degrees"][row_count - 1]:
                    Ke_Dis_lst.append(df2["p1_degrees"][8] - (df2["p2_degrees"][row_count - 1] + 270))
                if df2["p1_degrees"][8] < df2["p2_degrees"][row_count - 1]:
                    Ke_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][8] + 90))*  -1)
            else:
                Ke_Dis_lst.append(0)
            if len(str(row.As_Conc)) > 1:
                if df2["p1_degrees"][9] > df2["p2_degrees"][row_count - 1]:
                    As_Dis_lst.append((df2["p1_degrees"][9] - (df2["p2_degrees"][row_count - 1] + 270)))
                if df2["p1_degrees"][9] < df2["p2_degrees"][row_count - 1]:
                    As_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][9] + 90)) *-1)
            else:
                As_Dis_lst.append(0)
            if row_count == 10:
                row_count = 0
        if row.type == ">90":
            if len(str(row.Su_Conc)) > 1:
                if df2["p1_degrees"][0] > df2["p2_degrees"][row_count-1]:
                    temp = df2["p1_degrees"][0] - (df2["p2_degrees"][row_count-1]+ 270)
                    Su_Dis_lst.append(temp)
                if df2["p1_degrees"][0] < df2["p2_degrees"][row_count-1]:
                    temp = df2["p2_degrees"][row_count-1] - (df2["p1_degrees"][0] + 90)
                    Su_Dis_lst.append(temp * -1)
            else:
                Su_Dis_lst.append(0)
            if len(str(row.Mo_Conc)) > 1:
                if df2["p1_degrees"][1] > df2["p2_degrees"][row_count - 1]:
                    Mo_Dis_lst.append((df2["p1_degrees"][1] - (df2["p2_degrees"][row_count - 1] + 90)))
                if df2["p1_degrees"][1] < df2["p2_degrees"][row_count - 1]:
                    Mo_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][1] + 270)) * -1)
            else:
                Mo_Dis_lst.append(0)
            if len(str(row.Me_Conc)) > 1:
                if (df2["p1_degrees"][2]) > (df2["p2_degrees"][row_count - 1]):
                    Me_Dis_lst.append(df2["p1_degrees"][2] - (df2["p2_degrees"][row_count - 1] + 90))
                if df2["p1_degrees"][2] < df2["p2_degrees"][row_count - 1]:
                    Me_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][2] + 270)) * -1)
            else:
                Me_Dis_lst.append(0)
            if len(str(row.Ma_Conc)) > 1:
                if df2["p1_degrees"][3] > df2["p2_degrees"][row_count - 1]:
                    Ma_Dis_lst.append(df2["p1_degrees"][3] - (df2["p2_degrees"][row_count - 1] + 90))
                if df2["p1_degrees"][3] < df2["p2_degrees"][row_count - 1]:
                    Ma_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][3] + 270)) * -1)
            else:
                Ma_Dis_lst.append(0)
            if len(str(row.Ju_Conc)) > 1:
                if df2["p1_degrees"][4] > df2["p2_degrees"][row_count - 1]:
                    Ju_Dis_lst.append(df2["p1_degrees"][4] - (df2["p2_degrees"][row_count - 1] + 90))
                if df2["p1_degrees"][4] < df2["p2_degrees"][row_count - 1]:
                    Ju_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][4] + 270)) * -1)
            else:
                Ju_Dis_lst.append(0)
            if len(str(row.Ve_Conc)) > 1:
                if df2["p1_degrees"][5] > df2["p2_degrees"][row_count - 1]:
                    Ve_Dis_lst.append(df2["p1_degrees"][5] - (df2["p2_degrees"][row_count - 1] + 90))
                if df2["p1_degrees"][5] < df2["p2_degrees"][row_count - 1]:
                    Ve_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][5] + 270)) * -1)
            else:
                Ve_Dis_lst.append(0)
            if len(str(row.Sa_Conc)) > 1:
                if df2["p1_degrees"][6] > df2["p2_degrees"][row_count - 1]:
                    Sa_Dis_lst.append(df2["p1_degrees"][6] - (df2["p2_degrees"][row_count - 1] + 90))
                if df2["p1_degrees"][6] < df2["p2_degrees"][row_count - 1]:
                    Sa_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][6] + 270)) * -1)
            else:
                Sa_Dis_lst.append(0)
            if len(str(row.Ra_Conc)) > 1:
                if df2["p1_degrees"][7] > df2["p2_degrees"][row_count - 1]:
                    Ra_Dis_lst.append(df2["p1_degrees"][7] - (df2["p2_degrees"][row_count - 1] + 90))
                if df2["p1_degrees"][7] < df2["p2_degrees"][row_count - 1]:
                    Ra_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][7] + 270)) * -1)
            else:
                Ra_Dis_lst.append(0)
            if len(str(row.Ke_Conc)) > 1:
                if df2["p1_degrees"][8] > df2["p2_degrees"][row_count - 1]:
                    Ke_Dis_lst.append(df2["p1_degrees"][8] - (df2["p2_degrees"][row_count - 1] + 90))
                if df2["p1_degrees"][8] < df2["p2_degrees"][row_count - 1]:
                    Ke_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][8] + 270))*  -1)
            else:
                Ke_Dis_lst.append(0)
            if len(str(row.As_Conc)) > 1:
                if df2["p1_degrees"][9] > df2["p2_degrees"][row_count - 1]:
                    As_Dis_lst.append((df2["p1_degrees"][9] - (df2["p2_degrees"][row_count - 1] + 90)))
                if df2["p1_degrees"][9] < df2["p2_degrees"][row_count - 1]:
                    As_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][9] + 270)) *-1)
            else:
                As_Dis_lst.append(0)
            if row_count == 10:
                row_count = 0
        if row.type == "60<":
            if len(str(row.Su_Conc)) > 1:
                if df2["p1_degrees"][0] > df2["p2_degrees"][row_count-1]:
                    temp = df2["p1_degrees"][0] - (df2["p2_degrees"][row_count-1]+ 300)
                    Su_Dis_lst.append(temp)
                if df2["p1_degrees"][0] < df2["p2_degrees"][row_count-1]:
                    temp = df2["p2_degrees"][row_count-1] - (df2["p1_degrees"][0] + 60)
                    Su_Dis_lst.append(temp * -1)
            else:
                Su_Dis_lst.append(0)
            if len(str(row.Mo_Conc)) > 1:
                if df2["p1_degrees"][1] > df2["p2_degrees"][row_count - 1]:
                    Mo_Dis_lst.append((df2["p1_degrees"][1] - (df2["p2_degrees"][row_count - 1] + 300)))
                if df2["p1_degrees"][1] < df2["p2_degrees"][row_count - 1]:
                    Mo_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][1] + 60)) * -1)
            else:
                Mo_Dis_lst.append(0)
            if len(str(row.Me_Conc)) > 1:
                if (df2["p1_degrees"][2]) > (df2["p2_degrees"][row_count - 1]):
                    Me_Dis_lst.append(df2["p1_degrees"][2] - (df2["p2_degrees"][row_count - 1] + 300))
                if df2["p1_degrees"][2] < df2["p2_degrees"][row_count - 1]:
                    Me_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][2] + 60)) * -1)
            else:
                Me_Dis_lst.append(0)
            if len(str(row.Ma_Conc)) > 1:
                if df2["p1_degrees"][3] > df2["p2_degrees"][row_count - 1]:
                    Ma_Dis_lst.append(df2["p1_degrees"][3] - (df2["p2_degrees"][row_count - 1] + 300))
                if df2["p1_degrees"][3] < df2["p2_degrees"][row_count - 1]:
                    Ma_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][3] + 60)) * -1)
            else:
                Ma_Dis_lst.append(0)
            if len(str(row.Ju_Conc)) > 1:
                if df2["p1_degrees"][4] > df2["p2_degrees"][row_count - 1]:
                    Ju_Dis_lst.append(df2["p1_degrees"][4] - (df2["p2_degrees"][row_count - 1] + 300))
                if df2["p1_degrees"][4] < df2["p2_degrees"][row_count - 1]:
                    Ju_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][4] + 60)) * -1)
            else:
                Ju_Dis_lst.append(0)
            if len(str(row.Ve_Conc)) > 1:
                if df2["p1_degrees"][5] > df2["p2_degrees"][row_count - 1]:
                    Ve_Dis_lst.append(df2["p1_degrees"][5] - (df2["p2_degrees"][row_count - 1] + 300))
                if df2["p1_degrees"][5] < df2["p2_degrees"][row_count - 1]:
                    Ve_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][5] + 60)) * -1)
            else:
                Ve_Dis_lst.append(0)
            if len(str(row.Sa_Conc)) > 1:
                if df2["p1_degrees"][6] > df2["p2_degrees"][row_count - 1]:
                    Sa_Dis_lst.append(df2["p1_degrees"][6] - (df2["p2_degrees"][row_count - 1] + 300))
                if df2["p1_degrees"][6] < df2["p2_degrees"][row_count - 1]:
                    Sa_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][6] + 60)) * -1)
            else:
                Sa_Dis_lst.append(0)
            if len(str(row.Ra_Conc)) > 1:
                if df2["p1_degrees"][7] > df2["p2_degrees"][row_count - 1]:
                    Ra_Dis_lst.append(df2["p1_degrees"][7] - (df2["p2_degrees"][row_count - 1] + 300))
                if df2["p1_degrees"][7] < df2["p2_degrees"][row_count - 1]:
                    Ra_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][7] + 60)) * -1)
            else:
                Ra_Dis_lst.append(0)
            if len(str(row.Ke_Conc)) > 1:
                if df2["p1_degrees"][8] > df2["p2_degrees"][row_count - 1]:
                    Ke_Dis_lst.append(df2["p1_degrees"][8] - (df2["p2_degrees"][row_count - 1] + 300))
                if df2["p1_degrees"][8] < df2["p2_degrees"][row_count - 1]:
                    Ke_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][8] + 60))*  -1)
            else:
                Ke_Dis_lst.append(0)
            if len(str(row.As_Conc)) > 1:
                if df2["p1_degrees"][9] > df2["p2_degrees"][row_count - 1]:
                    As_Dis_lst.append((df2["p1_degrees"][9] - (df2["p2_degrees"][row_count - 1] + 300)))
                if df2["p1_degrees"][9] < df2["p2_degrees"][row_count - 1]:
                    As_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][9] + 60)) *-1)
            else:
                As_Dis_lst.append(0)
            if row_count == 10:
                row_count = 0
        if row.type == ">60":
            if len(str(row.Su_Conc)) > 1:
                if df2["p1_degrees"][0] > df2["p2_degrees"][row_count-1]:
                    temp = df2["p1_degrees"][0] - (df2["p2_degrees"][row_count-1]+ 60)
                    Su_Dis_lst.append(temp)
                if df2["p1_degrees"][0] < df2["p2_degrees"][row_count-1]:
                    temp = df2["p2_degrees"][row_count-1] - (df2["p1_degrees"][0] + 300)
                    Su_Dis_lst.append(temp * -1)
            else:
                Su_Dis_lst.append(0)
            if len(str(row.Mo_Conc)) > 1:
                if df2["p1_degrees"][1] > df2["p2_degrees"][row_count - 1]:
                    Mo_Dis_lst.append((df2["p1_degrees"][1] - (df2["p2_degrees"][row_count - 1] + 60)))
                if df2["p1_degrees"][1] < df2["p2_degrees"][row_count - 1]:
                    Mo_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][1] + 300)) * -1)
            else:
                Mo_Dis_lst.append(0)
            if len(str(row.Me_Conc)) > 1:
                if (df2["p1_degrees"][2]) > (df2["p2_degrees"][row_count - 1]):
                    Me_Dis_lst.append(df2["p1_degrees"][2] - (df2["p2_degrees"][row_count - 1] + 60))
                if df2["p1_degrees"][2] < df2["p2_degrees"][row_count - 1]:
                    Me_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][2] + 300)) * -1)
            else:
                Me_Dis_lst.append(0)
            if len(str(row.Ma_Conc)) > 1:
                if df2["p1_degrees"][3] > df2["p2_degrees"][row_count - 1]:
                    Ma_Dis_lst.append(df2["p1_degrees"][3] - (df2["p2_degrees"][row_count - 1] + 60))
                if df2["p1_degrees"][3] < df2["p2_degrees"][row_count - 1]:
                    Ma_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][3] + 300)) * -1)
            else:
                Ma_Dis_lst.append(0)
            if len(str(row.Ju_Conc)) > 1:
                if df2["p1_degrees"][4] > df2["p2_degrees"][row_count - 1]:
                    Ju_Dis_lst.append(df2["p1_degrees"][4] - (df2["p2_degrees"][row_count - 1] + 60))
                if df2["p1_degrees"][4] < df2["p2_degrees"][row_count - 1]:
                    Ju_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][4] + 300)) * -1)
            else:
                Ju_Dis_lst.append(0)
            if len(str(row.Ve_Conc)) > 1:
                if df2["p1_degrees"][5] > df2["p2_degrees"][row_count - 1]:
                    Ve_Dis_lst.append(df2["p1_degrees"][5] - (df2["p2_degrees"][row_count - 1] + 60))
                if df2["p1_degrees"][5] < df2["p2_degrees"][row_count - 1]:
                    Ve_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][5] + 300)) * -1)
            else:
                Ve_Dis_lst.append(0)
            if len(str(row.Sa_Conc)) > 1:
                if df2["p1_degrees"][6] > df2["p2_degrees"][row_count - 1]:
                    Sa_Dis_lst.append(df2["p1_degrees"][6] - (df2["p2_degrees"][row_count - 1] + 60))
                if df2["p1_degrees"][6] < df2["p2_degrees"][row_count - 1]:
                    Sa_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][6] + 300)) * -1)
            else:
                Sa_Dis_lst.append(0)
            if len(str(row.Ra_Conc)) > 1:
                if df2["p1_degrees"][7] > df2["p2_degrees"][row_count - 1]:
                    Ra_Dis_lst.append(df2["p1_degrees"][7] - (df2["p2_degrees"][row_count - 1] + 60))
                if df2["p1_degrees"][7] < df2["p2_degrees"][row_count - 1]:
                    Ra_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][7] + 300)) * -1)
            else:
                Ra_Dis_lst.append(0)
            if len(str(row.Ke_Conc)) > 1:
                if df2["p1_degrees"][8] > df2["p2_degrees"][row_count - 1]:
                    Ke_Dis_lst.append(df2["p1_degrees"][8] - (df2["p2_degrees"][row_count - 1] + 60))
                if df2["p1_degrees"][8] < df2["p2_degrees"][row_count - 1]:
                    Ke_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][8] + 300))*  -1)
            else:
                Ke_Dis_lst.append(0)
            if len(str(row.As_Conc)) > 1:
                if df2["p1_degrees"][9] > df2["p2_degrees"][row_count - 1]:
                    As_Dis_lst.append((df2["p1_degrees"][9] - (df2["p2_degrees"][row_count - 1] + 60)))
                if df2["p1_degrees"][9] < df2["p2_degrees"][row_count - 1]:
                    As_Dis_lst.append((df2["p2_degrees"][row_count - 1] - (df2["p1_degrees"][9] + 300)) *-1)
            else:
                As_Dis_lst.append(0)
            if row_count == 10:
                row_count = 0
        if row.type == ">150":
            if len(str(row.Su_Conc)) > 1:
                if df2["p1_degrees"][3] > df2["p2_degrees"][0]:
                    temp = df2["p1_degrees"][3] - (df2["p2_degrees"][0] + 150)
                    Su_Dis_lst.append(temp)
                if df2["p1_degrees"][3] < df2["p2_degrees"][0]:
                    temp = df2["p2_degrees"][1] - (df2["p1_degrees"][3] + 210)
                    Su_Dis_lst.append(temp * -1)
            else:
                Su_Dis_lst.append(0)
            if len(str(row.Mo_Conc)) > 1:
                if df2["p1_degrees"][3] > df2["p2_degrees"][1]:
                    Mo_Dis_lst.append(df2["p1_degrees"][3] - (df2["p2_degrees"][1] + 150))
                if df2["p1_degrees"][3] < df2["p2_degrees"][1]:
                    Mo_Dis_lst.append((df2["p2_degrees"][1] - (df2["p1_degrees"][3] + 210)) * -1)
            else:
                Mo_Dis_lst.append(0)
            if len(str(row.Me_Conc)) > 1:
                if (df2["p1_degrees"][3]) > (df2["p2_degrees"][2]):
                    Me_Dis_lst.append(df2["p1_degrees"][3] - (df2["p2_degrees"][2] + 150))
                if df2["p1_degrees"][3] < df2["p2_degrees"][2]:
                    Me_Dis_lst.append((df2["p2_degrees"][2] - (df2["p1_degrees"][3] + 210)) * -1)
            else:
                Me_Dis_lst.append(0)
            if len(str(row.Ma_Conc)) > 1:
                if df2["p1_degrees"][3] > df2["p2_degrees"][3]:
                    Ma_Dis_lst.append(df2["p1_degrees"][3] - (df2["p2_degrees"][3] + 150))
                if df2["p1_degrees"][3] < df2["p2_degrees"][3]:
                    Ma_Dis_lst.append((df2["p2_degrees"][3] - (df2["p1_degrees"][3] + 210)) * -1)
            else:
                Ma_Dis_lst.append(0)
            if len(str(row.Ju_Conc)) > 1:
                if df2["p1_degrees"][3] > df2["p2_degrees"][4]:
                    Ju_Dis_lst.append(df2["p1_degrees"][3] - (df2["p2_degrees"][4] + 150))
                if df2["p1_degrees"][3] < df2["p2_degrees"][4]:
                    Ju_Dis_lst.append((df2["p2_degrees"][4] - (df2["p1_degrees"][3] + 210)) * -1)
            else:
                Ju_Dis_lst.append(0)
            if len(str(row.Ve_Conc)) > 1:
                if df2["p1_degrees"][3] > df2["p2_degrees"][5]:
                    Ve_Dis_lst.append(df2["p1_degrees"][3] - (df2["p2_degrees"][5] + 150))
                if df2["p1_degrees"][3] < df2["p2_degrees"][5]:
                    Ve_Dis_lst.append((df2["p2_degrees"][5] - (df2["p1_degrees"][3] + 210)) * -1)
            else:
                Ve_Dis_lst.append(0)
            if len(str(row.Sa_Conc)) > 1:
                if df2["p1_degrees"][3] > df2["p2_degrees"][6]:
                    Sa_Dis_lst.append(df2["p1_degrees"][3] - (df2["p2_degrees"][6] + 150))
                if df2["p1_degrees"][3] < df2["p2_degrees"][6]:
                    Sa_Dis_lst.append((df2["p2_degrees"][6] - (df2["p1_degrees"][3] + 210)) * -1)
            else:
                Sa_Dis_lst.append(0)
            if len(str(row.Ra_Conc)) > 1:
                if df2["p1_degrees"][3] > df2["p2_degrees"][7]:
                    Ra_Dis_lst.append(df2["p1_degrees"][3] - (df2["p2_degrees"][7] + 150))

                if df2["p1_degrees"][3] < df2["p2_degrees"][7]:
                    Ra_Dis_lst.append((df2["p2_degrees"][7] - (df2["p1_degrees"][3] + 210)) * -1)
            else:
                Ra_Dis_lst.append(0)
            if len(str(row.Ke_Conc)) > 1:
                if df2["p1_degrees"][3] > df2["p2_degrees"][8]:
                    Ke_Dis_lst.append(df2["p1_degrees"][3] - (df2["p2_degrees"][8] + 150))
                if df2["p1_degrees"][3] < df2["p2_degrees"][8]:
                    Ke_Dis_lst.append((df2["p2_degrees"][8] - (df2["p1_degrees"][3] + 210)) * -1)
            else:
                Ke_Dis_lst.append(0)
            if len(str(row.As_Conc)) > 1:
                if df2["p1_degrees"][3] > df2["p2_degrees"][9]:
                    As_Dis_lst.append((df2["p1_degrees"][3] - (df2["p2_degrees"][9] + 150)))
                if df2["p1_degrees"][3] < df2["p2_degrees"][9]:
                    As_Dis_lst.append((df2["p2_degrees"][9] - (df2["p1_degrees"][3] + 210)) * -1)
            else:
                As_Dis_lst.append(0)
            if row_count == 10:
                row_count = 0
    df1["Su_Dis_lst"] = Su_Dis_lst
    df1["Mo_Dis_lst"] = Mo_Dis_lst
    df1["Me_Dis_lst"]  = Me_Dis_lst
    df1["Ma_Dis_lst"] = Ma_Dis_lst
    df1["Ju_Dis_lst"] = Ju_Dis_lst
    df1["Ve_Dis_lst"] = Ve_Dis_lst
    df1["Sa_Dis_lst"] = Sa_Dis_lst
    df1["Ra_Dis_lst"] = Ra_Dis_lst
    df1["Ke_Dis_lst"] =  Ke_Dis_lst
    df1["As_Dis_lst"] = As_Dis_lst
    return df1

def list_to_list_of_lists(lst):
    return [[el] for el in lst]

def p1_concatenation_table(shp_df,pasp_table_df, signtable):
    Su_Conc_lst = []
    Mo_Conc_lst = []
    Me_Conc_lst = []
    Ma_Conc_lst = []
    Ju_Conc_lst = []
    Ve_Conc_lst = []
    Sa_Conc_lst = []
    Ra_Conc_lst = []
    Ke_Conc_lst = []
    As_Conc_lst = []
    df = pd.DataFrame(columns=['type'])
    type_list = ["Conj", "180", "120<", ">120", "90<", ">90", "60<", ">60"]
    for i in type_list:
        lst = list_to_list_of_lists([i for j in range(10)])
        for k in lst:
            df.loc[len(df)] = k
    df.loc[len(df)] = [">150"]
    df['planet'] = (["Su", "Mo", "Me", "Ma", "Ju", "Ve", "Sa", "Ra", "Ke", "As"] * (len(df) // 2 + 1))[:len(df)]
    house_lst = shp_df["house_num"].to_list()
    df["in_house"] = (house_lst * (len(df) // 2 + 1))[:len(df)]
    df.loc[df['type'] == ">150", 'in_house'] = df.iloc[73, df.columns.get_loc("in_house")]
    sign_lst = shp_df["sign_name"].to_list()
    df["sign_he"] = (sign_lst * (len(df) // 2 + 1))[:len(df)]
    df.loc[df['type'] == ">150", 'sign_he'] = df.iloc[73, df.columns.get_loc("sign_he")]
    df2 = pasp_table_df.copy()
    lst = []
    for index, row in df.iterrows():
        if row.type == "Conj":
            lst.append(row.in_house)
        elif row.type == "180":
            lst.append(df2.iloc[(row.in_house) - 1, df2.columns.get_loc("180")])
        elif row.type == ">150":
            lst.append(df2.iloc[(row.in_house) - 1, df2.columns.get_loc("greater150")])
        elif row.type == "120<":
            lst.append(df2.iloc[(row.in_house) - 1, df2.columns.get_loc("120lesser")])
        elif row.type == ">120":
            lst.append(df2.iloc[(row.in_house) - 1, df2.columns.get_loc("greater120")])
        elif row.type == "90<":
            lst.append(df2.iloc[(row.in_house) - 1, df2.columns.get_loc("90lesser")])
        elif row.type == ">90":
            lst.append(df2.iloc[(row.in_house) - 1, df2.columns.get_loc("90greater")])
        elif row.type == "60<":
            lst.append(df2.iloc[(row.in_house) - 1, df2.columns.get_loc("60lesser")])
        elif row.type == ">60":
            lst.append(df2.iloc[(row.in_house) - 1, df2.columns.get_loc("60greater")])
    df["he_with_aspects"] = lst
    df3 = signtable.copy()
    s_lst = []
    for index, row in df.iterrows():
        check_sign = 0
        if row.sign_he == "Ar":
            check_sign = 1
        elif row.sign_he == "Ta":
            check_sign = 2
        elif row.sign_he == "Ge":
            check_sign = 3
        elif row.sign_he == "Ca":
            check_sign = 4
        elif row.sign_he == "Le":
            check_sign = 5
        elif row.sign_he == "Vg":
            check_sign = 6
        elif row.sign_he == "Li":
            check_sign = 7
        elif row.sign_he == "Sc":
            check_sign = 8
        elif row.sign_he == "Sg":
            check_sign = 9
        elif row.sign_he == "Cp":
            check_sign = 10
        elif row.sign_he == "Aq":
            check_sign = 11
        elif row.sign_he == "Pi":
            check_sign = 12
        if row.type == "Conj":
            s_lst.append(df3.iloc[check_sign - 1, df3.columns.get_loc("Conj")])
        elif row.type == "180":
            s_lst.append(df3.iloc[check_sign - 1, df3.columns.get_loc("180")])
        elif row.type == ">150":
            s_lst.append(df3.iloc[check_sign - 1, df3.columns.get_loc("greater150")])
        elif row.type == "120<":
            s_lst.append(df3.iloc[check_sign - 1, df3.columns.get_loc("120lesser")])
        elif row.type == ">120":
            s_lst.append(df3.iloc[check_sign - 1, df3.columns.get_loc("greater120")])
        elif row.type == "90<":
            s_lst.append(df3.iloc[check_sign - 1, df3.columns.get_loc("90lesser")])
        elif row.type == ">90":
            s_lst.append(df3.iloc[check_sign - 1, df3.columns.get_loc("90greater")])
        elif row.type == "60<":
            s_lst.append(df3.iloc[check_sign - 1, df3.columns.get_loc("60lesser")])
        elif row.type == ">60":
            s_lst.append(df3.iloc[check_sign - 1, df3.columns.get_loc("60greater")])
    df["sign_he_aspect"] = s_lst
    count = 0
    for index, row in df.iterrows():
        if row.type == ">150":
            Su_Conc_lst.append(0)
            Mo_Conc_lst.append(0)
            Me_Conc_lst.append(0)
            Ma_Conc_lst.append(0)
            Ju_Conc_lst.append(0)
            Ve_Conc_lst.append(0)
            Sa_Conc_lst.append(0)
            Ra_Conc_lst.append(0)
            Ke_Conc_lst.append(0)
            As_Conc_lst.append(0)
        else:
            count += 1
            planet_count = 0
            for i in sign_lst:
                planet_count += 1
                if count == 1:
                    if row.sign_he_aspect == i:
                        if row.planet == planet_num_check(planet_count):
                            Su_Conc_lst.append(0)
                        else:
                            Su_Conc_lst.append(str(row.sign_he + row.planet + i + planet_num_check(planet_count)))
                    else:
                        Su_Conc_lst.append(0)
                if count == 2:
                    if row.sign_he_aspect == i:
                        if row.planet == planet_num_check(planet_count):
                            Mo_Conc_lst.append(0)
                        else:
                            Mo_Conc_lst.append(str(row.sign_he + row.planet + i + planet_num_check(planet_count)))
                    else:
                        Mo_Conc_lst.append(0)
                if count == 3:
                    if row.sign_he_aspect == i:
                        if row.planet == planet_num_check(planet_count):
                            Me_Conc_lst.append(0)
                        else:
                            Me_Conc_lst.append(str(row.sign_he + row.planet + i + planet_num_check(planet_count)))
                    else:
                        Me_Conc_lst.append(0)
                if count == 4:
                    if row.sign_he_aspect == i:
                        if row.planet == planet_num_check(planet_count):
                            Ma_Conc_lst.append(0)
                        else:
                            Ma_Conc_lst.append(str(row.sign_he + row.planet + i + planet_num_check(planet_count)))
                    else:
                        Ma_Conc_lst.append(0)
                if count == 5:
                    if row.sign_he_aspect == i:
                        if row.planet == planet_num_check(planet_count):
                            Ju_Conc_lst.append(0)
                        else:
                            Ju_Conc_lst.append(str(row.sign_he + row.planet + i + planet_num_check(planet_count)))
                    else:
                        Ju_Conc_lst.append(0)
                if count == 6:
                    if row.sign_he_aspect == i:
                        if row.planet == planet_num_check(planet_count):
                            Ve_Conc_lst.append(0)
                        else:
                            Ve_Conc_lst.append(str(row.sign_he + row.planet + i + planet_num_check(planet_count)))
                    else:
                        Ve_Conc_lst.append(0)
                if count == 7:
                    if row.sign_he_aspect == i:
                        if row.planet == planet_num_check(planet_count):
                            Sa_Conc_lst.append(0)
                        else:
                            Sa_Conc_lst.append(str(row.sign_he + row.planet + i + planet_num_check(planet_count)))
                    else:
                        Sa_Conc_lst.append(0)
                if count == 8:
                    if row.sign_he_aspect == i:
                        if row.planet == planet_num_check(planet_count):
                            Ra_Conc_lst.append(0)
                        else:
                            Ra_Conc_lst.append(str(row.sign_he + row.planet + i + planet_num_check(planet_count)))
                    else:
                        Ra_Conc_lst.append(0)
                if count == 9:
                    if row.sign_he_aspect == i:
                        if row.planet == planet_num_check(planet_count):
                            Ke_Conc_lst.append(0)
                        else:
                            Ke_Conc_lst.append(str(row.sign_he + row.planet + i + planet_num_check(planet_count)))
                    else:
                        Ke_Conc_lst.append(0)
                if count == 10:
                    if row.sign_he_aspect == i:
                        if row.planet == planet_num_check(planet_count):
                            As_Conc_lst.append(0)
                        else:
                            As_Conc_lst.append(str(row.sign_he + row.planet + i + planet_num_check(planet_count)))
                    else:
                        As_Conc_lst.append(0)
                if count == 10 and planet_count == 10:
                    count = 0

    df.loc[df.type == ">150", "planet"] = "Ma"
    df.loc[df.type == ">150", "Su_Conc"] = "AK"
    mars_c = ""
    for index, row in df.iterrows():
        if row.type == ">150":
            p_count = 0
            for i in sign_lst:
                p_count += 1
                if row.sign_he_aspect == i:
                    if row.sign_he_aspect == i:
                        mars_c = (str(row.sign_he + row.planet + i + planet_num_check(p_count)))
    if len(mars_c) > 1:
        Su_Conc_lst[-1] = mars_c
    df["Su_Conc"] = Su_Conc_lst
    df["Mo_Conc"] = Mo_Conc_lst
    df["Me_Conc"] = Me_Conc_lst
    df["Ma_Conc"] = Ma_Conc_lst
    df["Ju_Conc"] = Ju_Conc_lst
    df["Ve_Conc"] = Ve_Conc_lst
    df["Sa_Conc"] = Sa_Conc_lst
    df["Ra_Conc"] = Ra_Conc_lst
    df["Ke_Conc"] = Ke_Conc_lst
    df["As_Conc"] = As_Conc_lst
    df.loc[(df.type != "Conj"), "As_Conc"] = 0
    # df.loc[df.type != "Conj", "Ke_Conc"] = 0
    df.loc[df.type == "180", "Ra_Conc"] = 0
    df.loc[df.type == "180", "Ke_Conc"] = 0
    # df.loc[df.type == ">150", "Ra_Conc"] = 0
    return df

def p1_points_table(df):
    db = concatenation_points_database()
    Su_point_lst = []
    Mo_point_lst = []
    Me_point_lst = []
    Ma_point_lst = []
    Ju_point_lst = []
    Ve_point_lst = []
    Sa_point_lst = []
    Ra_point_lst = []
    Ke_point_lst = []
    As_point_lst = []
    df1 = pd.DataFrame(columns=['type'])
    type_list = ["Conj", "180", "120<", ">120", "90<", ">90", "60<", ">60"]
    for i in type_list:
        lst = list_to_list_of_lists([i for j in range(10)])
        for k in lst:
            df1.loc[len(df1)] = k
    df1.loc[len(df1)] = [">150"]
    for index, row in df.iterrows():
        if row.Su_Conc != 0:
            Su_point_lst.append((db[db['con_type'].isin([row.type]) & db['con_name'].isin([row.Su_Conc])].con_points.values)[0])
        else:
            Su_point_lst.append(0)
        if row.Mo_Conc != 0:
            Mo_point_lst.append((db[db['con_type'].isin([row.type]) & db['con_name'].isin([row.Mo_Conc])].con_points.values)[0])
        else:
            Mo_point_lst.append(0)


        if row.Me_Conc != 0:
            Me_point_lst.append((db[db['con_type'].isin([row.type]) & db['con_name'].isin([row.Me_Conc])].con_points.values)[0])
        else:
            Me_point_lst.append(0)


        if row.Ma_Conc != 0:
            Ma_point_lst.append((db[db['con_type'].isin([row.type]) & db['con_name'].isin([row.Ma_Conc])].con_points.values)[0])
        else:
            Ma_point_lst.append(0)


        if row.Ju_Conc != 0:
            Ju_point_lst.append((db[db['con_type'].isin([row.type]) & db['con_name'].isin([row.Ju_Conc])].con_points.values)[0])
        else:
            Ju_point_lst.append(0)


        if row.Ve_Conc != 0:
            Ve_point_lst.append((db[db['con_type'].isin([row.type]) & db['con_name'].isin([row.Ve_Conc])].con_points.values)[0])
        else:
            Ve_point_lst.append(0)


        if row.Sa_Conc != 0:
            Sa_point_lst.append((db[db['con_type'].isin([row.type]) & db['con_name'].isin([row.Sa_Conc])].con_points.values)[0])
        else:
            Sa_point_lst.append(0)


        if row.Ra_Conc != 0:
            Ra_point_lst.append((db[db['con_type'].isin([row.type]) & db['con_name'].isin([row.Ra_Conc])].con_points.values)[0])
        else:
            Ra_point_lst.append(0)


        if row.Ke_Conc != 0:
            Ke_point_lst.append((db[db['con_type'].isin([row.type]) & db['con_name'].isin([row.Ke_Conc])].con_points.values)[0])
        else:
            Ke_point_lst.append(0)


        if row.As_Conc != 0:
            As_point_lst.append((db[db['con_type'].isin([row.type]) & db['con_name'].isin([row.As_Conc])].con_points.values)[0])
        else:
            As_point_lst.append(0)
    df1["Su_Point"] = Su_point_lst
    df1["Mo_Point"] = Mo_point_lst
    df1["Me_Point"] = Me_point_lst
    df1["Ma_Point"] = Ma_point_lst
    df1["Ju_Point"] = Ju_point_lst
    df1["Ve_Point"] = Ve_point_lst
    df1["Sa_Point"] = Sa_point_lst
    df1["Ra_Point"] = Ra_point_lst
    df1["Ke_Point"] = Ke_point_lst
    df1["As_Point"] = As_point_lst

    df1['planet'] = (["Su", "Mo", "Me", "Ma", "Ju", "Ve", "Sa", "Ra", "Ke", "As"] * (len(df1) // 2 + 1))[:len(df1)]
    df1.loc[df['type'] == ">150", 'planet'] = "Ma"
    df1.loc[df['type'] == "Conj", 'total'] = ((df1["Su_Point"] + df1["Mo_Point"] + df1["Me_Point"] + df1["Ma_Point"] + df1["Ju_Point"] + df1["Ve_Point"] + df1["Sa_Point"] + df1["Ra_Point"] + df1["Ke_Point"] ) * 9)
    df1.loc[df["type"]== "180", "total"] =  ((df1["Su_Point"] + df1["Mo_Point"] + df1["Me_Point"] + df1["Ma_Point"] + df1["Ju_Point"] + df1["Ve_Point"] + df1["Sa_Point"] + df1["Ra_Point"] + df1["Ke_Point"] ) * 7)
    df1.loc[((df["type"]== "120<") | (df["type"]== ">120")),  "total"] =  ((df1["Su_Point"] + df1["Mo_Point"] + df1["Me_Point"] + df1["Ma_Point"] + df1["Ju_Point"] + df1["Ve_Point"] + df1["Sa_Point"] + df1["Ra_Point"] + df1["Ke_Point"] ) * 5)
    df1.loc[((df["type"]== "90<") | (df["type"]== ">90")),  "total"] =  ((df1["Su_Point"] + df1["Mo_Point"] + df1["Me_Point"] + df1["Ma_Point"] + df1["Ju_Point"] + df1["Ve_Point"] + df1["Sa_Point"] + df1["Ra_Point"] + df1["Ke_Point"] ) * 3)
    df1.loc[((df["type"]== "60<") | (df["type"]== ">60")),  "total"] =  ((df1["Su_Point"] + df1["Mo_Point"] + df1["Me_Point"] + df1["Ma_Point"] + df1["Ju_Point"] + df1["Ve_Point"] + df1["Sa_Point"] + df1["Ra_Point"] + df1["Ke_Point"]) * 2)
    df1.loc[df["type"]== ">150", "total"] =  ((df1["Su_Point"] + df1["Mo_Point"] + df1["Me_Point"] + df1["Ma_Point"] + df1["Ju_Point"] + df1["Ve_Point"] + df1["Sa_Point"] + df1["Ra_Point"] + df1["Ke_Point"]) * 7)
    return df1

def p1_point_planets_planet_aspects(single_point_df):
    df1 = single_point_df.copy()
    Conj_list = []
    lst_180 = []
    lst_120lesser = []
    lst_120greater = []
    lst_90lesser = []
    lst_90greater = []
    lst_60lesser = []
    lst_60greater = []
    lst_150greater = []
    for index, row in df1.iterrows():
        if row.type == "Conj":
            Conj_list.append(row.total)
        if row.type == "180":
            lst_180.append(row.total)
        if row.type == "120<":
            lst_120lesser.append(row.total)
        if row.type == ">120":
            lst_120greater.append(row.total)
        if row.type == "90<":
            lst_90lesser.append(row.total)
        if row.type == ">90":
            lst_90greater.append(row.total)
        if row.type == "60<":
            lst_60lesser.append(row.total)
        if row.type == ">60":
            lst_60greater.append(row.total)
        if row.type == ">150":
            lst_150greater.append(row.total)
    for i in range(9):
        lst_150greater.append(0)

    df = pd.DataFrame(columns=["Conj", "180", "120lesser", "120greater", "90lesser", "90greater", "60lesser", "60greater", "150greater"])
    df["Conj"] = Conj_list
    df["180"] = lst_180
    df["120lesser"] = lst_120lesser
    df["120greater"] = lst_120greater
    df["90lesser"] = lst_90lesser
    df["90greater"] = lst_90greater
    df["60lesser"] = lst_60lesser
    df["60greater"] = lst_60greater
    df["150greater"] = lst_150greater
    df['planet'] = (["Su", "Mo", "Me", "Ma", "Ju", "Ve", "Sa", "Ra", "Ke", "As"])
    df['total'] = df["Conj"] + df["180"] + df["120lesser"] + df["120greater"] + df["90lesser"] + df["90greater"] + df["60lesser"] + df["60greater"] + df["150greater"]
    df["consolidate"] = df["total"] * 0.5
    return df

def p1xp2_dm_data():
    data = distance_multiplier.objects.all()
    data = read_frame(data)
    return data

def p1xp2_distance_between_planets(distance_df, dm_data_df):
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
