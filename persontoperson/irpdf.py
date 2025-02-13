import pandas as pd
import plotly.graph_objs as go
import plotly.offline as opy
from .p1conp2 import dataframe_to_dict
from .astro_fun import *
from .models import plotimages
import plotly.io as pio


def ir_concatenation_graph(p1xp2_distance_df, p1xp2_distance_planets_df):
    df1 = p1xp2_distance_df.copy()
    df2 = p1xp2_distance_planets_df.copy()
    df1["Su_dp_lst"] = df2.Su_dp_lst.to_list()
    df1["Mo_dp_lst"] = df2.Mo_dp_lst.to_list()
    df1["Me_dp_lst"] = df2.Me_dp_lst.to_list()
    df1["Ma_dp_lst"] = df2.Ma_dp_lst.to_list()
    df1["Ju_dp_lst"] = df2.Ju_dp_lst.to_list()
    df1["Ve_dp_lst"] = df2.Ve_dp_lst.to_list()
    df1["Sa_dp_lst"] = df2.Sa_dp_lst.to_list()
    df1["Ra_dp_lst"] = df2.Ra_dp_lst.to_list()
    df1["Ke_dp_lst"] = df2.Ke_dp_lst.to_list()
    df1["As_dp_lst"] = df2.As_dp_lst.to_list()
    ir_Conj_lst = []
    ir_180_lst = []
    ir_greater120_lst = []
    ir_lesser120_lst = []
    ir_greater90_lst = []
    ir_lesser90_lst = []
    ir_greater60_lst = []
    ir_lesser60_lst = []
    ir_greater150_lst = []
    su_count = 0
    mo_count = 0
    me_count = 0
    ma_count = 0
    ju_count = 0
    ve_count = 0
    sa_count = 0
    ra_count = 0
    ke_count = 0
    as_count = 0
    for index, row in df1.iterrows():
        if row.type == "Conj":
            if len(str(row.Su_Conc)) > 1:
                ir_Conj_lst.insert(su_count, [row.type, "Su", row.Su_Conc, row.Su_Dis_lst, row.Su_dp_lst])
                su_count += 1
                mo_count += 1
                me_count += 1
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Mo_Conc)) > 1:
                ir_Conj_lst.insert(mo_count, [row.type, "Mo", row.Mo_Conc, row.Mo_Dis_lst, row.Mo_dp_lst])
                mo_count += 1
                me_count += 1
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Me_Conc)) > 1:
                ir_Conj_lst.insert(me_count, [row.type, "Me", row.Me_Conc, row.Me_Dis_lst, row.Me_dp_lst])
                me_count += 1
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ma_Conc)) > 1:
                ir_Conj_lst.insert(ma_count, [row.type, "Ma", row.Ma_Conc, row.Ma_Dis_lst, row.Ma_dp_lst])
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1


            if len(str(row.Ju_Conc)) > 1:
                ir_Conj_lst.insert(ju_count, [row.type, "Ju", row.Ju_Conc, row.Ju_Dis_lst, row.Ju_dp_lst])
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ve_Conc)) > 1:
                ir_Conj_lst.insert(ve_count, [row.type, "Ve", row.Ve_Conc, row.Ve_Dis_lst, row.Ve_dp_lst])
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Sa_Conc)) > 1:
                ir_Conj_lst.insert(sa_count, [row.type, "Sa", row.Sa_Conc, row.Sa_Dis_lst, row.Sa_dp_lst])
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ra_Conc)) > 1:
                ir_Conj_lst.insert(ra_count, [row.type, "Ra", row.Ra_Conc, row.Ra_Dis_lst, row.Ra_dp_lst])
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ke_Conc)) > 1:
                ir_Conj_lst.insert(ke_count, [row.type, "Ke", row.Ke_Conc, row.Ke_Dis_lst, row.Ke_dp_lst])
                ke_count += 1
                as_count += 1

            if len(str(row.As_Conc)) > 1:
                ir_Conj_lst.insert(as_count, [row.type, "As", row.As_Conc, row.As_Dis_lst, row.As_dp_lst])
                as_count += 1
    su_count = 0
    mo_count = 0
    me_count = 0
    ma_count = 0
    ju_count = 0
    ve_count = 0
    sa_count = 0
    ra_count = 0
    ke_count = 0
    as_count = 0
    for index, row in df1.iterrows():
        if row.type == "180":
            if len(str(row.Su_Conc)) > 1:
                ir_180_lst.insert(su_count, [row.type, "Su", row.Su_Conc, row.Su_Dis_lst, row.Su_dp_lst])
                su_count += 1
                mo_count += 1
                me_count += 1
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Mo_Conc)) > 1:
                ir_180_lst.insert(mo_count, [row.type, "Mo", row.Mo_Conc, row.Mo_Dis_lst, row.Mo_dp_lst])
                mo_count += 1
                me_count += 1
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Me_Conc)) > 1:
                ir_180_lst.insert(me_count, [row.type, "Me", row.Me_Conc, row.Me_Dis_lst, row.Me_dp_lst])
                me_count += 1
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ma_Conc)) > 1:
                ir_180_lst.insert(ma_count, [row.type, "Ma", row.Ma_Conc, row.Ma_Dis_lst, row.Ma_dp_lst])
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ju_Conc)) > 1:
                ir_180_lst.insert(ju_count, [row.type, "Ju", row.Ju_Conc, row.Ju_Dis_lst, row.Ju_dp_lst])
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ve_Conc)) > 1:
                ir_180_lst.insert(ve_count, [row.type, "Ve", row.Ve_Conc, row.Ve_Dis_lst, row.Ve_dp_lst])
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Sa_Conc)) > 1:
                ir_180_lst.insert(sa_count, [row.type, "Sa", row.Sa_Conc, row.Sa_Dis_lst, row.Sa_dp_lst])
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ra_Conc)) > 1:
                ir_180_lst.insert(ra_count, [row.type, "Ra", row.Ra_Conc, row.Ra_Dis_lst, row.Ra_dp_lst])
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ke_Conc)) > 1:
                ir_180_lst.insert(ke_count, [row.type, "Ke", row.Ke_Conc, row.Ke_Dis_lst, row.Ke_dp_lst])
                ke_count += 1
                as_count += 1

            if len(str(row.As_Conc)) > 1:
                ir_180_lst.insert(as_count, [row.type, "As", row.As_Conc, row.As_Dis_lst, row.As_dp_lst])
                as_count += 1

    su_count = 0
    mo_count = 0
    me_count = 0
    ma_count = 0
    ju_count = 0
    ve_count = 0
    sa_count = 0
    ra_count = 0
    ke_count = 0
    as_count = 0
    for index, row in df1.iterrows():
        if row.type == ">120":
            if len(str(row.Su_Conc)) > 1:
                ir_greater120_lst.insert(su_count, [row.type, "Su", row.Su_Conc, row.Su_Dis_lst, row.Su_dp_lst])
                su_count += 1
                mo_count += 1
                me_count += 1
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Mo_Conc)) > 1:
                ir_greater120_lst.insert(mo_count, [row.type, "Mo", row.Mo_Conc, row.Mo_Dis_lst, row.Mo_dp_lst])
                mo_count += 1
                me_count += 1
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Me_Conc)) > 1:
                ir_greater120_lst.insert(me_count, [row.type, "Me", row.Me_Conc, row.Me_Dis_lst, row.Me_dp_lst])
                me_count += 1
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ma_Conc)) > 1:
                ir_greater120_lst.insert(ma_count, [row.type, "Ma", row.Ma_Conc, row.Ma_Dis_lst, row.Ma_dp_lst])
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ju_Conc)) > 1:
                ir_greater120_lst.insert(ju_count, [row.type, "Ju", row.Ju_Conc, row.Ju_Dis_lst, row.Ju_dp_lst])
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ve_Conc)) > 1:
                ir_greater120_lst.insert(ve_count, [row.type, "Ve", row.Ve_Conc, row.Ve_Dis_lst, row.Ve_dp_lst])
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Sa_Conc)) > 1:
                ir_greater120_lst.insert(sa_count, [row.type, "Sa", row.Sa_Conc, row.Sa_Dis_lst, row.Sa_dp_lst])
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ra_Conc)) > 1:
                ir_greater120_lst.insert(ra_count, [row.type, "Ra", row.Ra_Conc, row.Ra_Dis_lst, row.Ra_dp_lst])
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ke_Conc)) > 1:
                ir_greater120_lst.insert(ke_count, [row.type, "Ke", row.Ke_Conc, row.Ke_Dis_lst, row.Ke_dp_lst])
                ke_count += 1
                as_count += 1

            if len(str(row.As_Conc)) > 1:
                ir_greater120_lst.insert(as_count, [row.type, "As", row.As_Conc, row.As_Dis_lst, row.As_dp_lst])
                as_count += 1
    su_count = 0
    mo_count = 0
    me_count = 0
    ma_count = 0
    ju_count = 0
    ve_count = 0
    sa_count = 0
    ra_count = 0
    ke_count = 0
    as_count = 0
    for index, row in df1.iterrows():
        if row.type == "120<":
            if len(str(row.Su_Conc)) > 1:
                ir_lesser120_lst.insert(su_count, [row.type, "Su", row.Su_Conc, row.Su_Dis_lst, row.Su_dp_lst])
                su_count += 1
                mo_count += 1
                me_count += 1
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Mo_Conc)) > 1:
                ir_lesser120_lst.insert(mo_count, [row.type, "Mo", row.Mo_Conc, row.Mo_Dis_lst, row.Mo_dp_lst])
                mo_count += 1
                me_count += 1
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Me_Conc)) > 1:
                ir_lesser120_lst.insert(me_count, [row.type, "Me", row.Me_Conc, row.Me_Dis_lst, row.Me_dp_lst])
                me_count += 1
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ma_Conc)) > 1:
                ir_lesser120_lst.insert(ma_count, [row.type, "Ma", row.Ma_Conc, row.Ma_Dis_lst, row.Ma_dp_lst])
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ju_Conc)) > 1:
                ir_lesser120_lst.insert(ju_count, [row.type, "Ju", row.Ju_Conc, row.Ju_Dis_lst, row.Ju_dp_lst])
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ve_Conc)) > 1:
                ir_lesser120_lst.insert(ve_count, [row.type, "Ve", row.Ve_Conc, row.Ve_Dis_lst, row.Ve_dp_lst])
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Sa_Conc)) > 1:
                ir_lesser120_lst.insert(sa_count, [row.type, "Sa", row.Sa_Conc, row.Sa_Dis_lst, row.Sa_dp_lst])
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ra_Conc)) > 1:
                ir_lesser120_lst.insert(ra_count, [row.type, "Ra", row.Ra_Conc, row.Ra_Dis_lst, row.Ra_dp_lst])
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ke_Conc)) > 1:
                ir_lesser120_lst.insert(ke_count, [row.type, "Ke", row.Ke_Conc, row.Ke_Dis_lst, row.Ke_dp_lst])
                ke_count += 1
                as_count += 1

            if len(str(row.As_Conc)) > 1:
                ir_lesser120_lst.insert(as_count, [row.type, "As", row.As_Conc, row.As_Dis_lst, row.As_dp_lst])
                as_count += 1
    su_count = 0
    mo_count = 0
    me_count = 0
    ma_count = 0
    ju_count = 0
    ve_count = 0
    sa_count = 0
    ra_count = 0
    ke_count = 0
    as_count = 0
    for index, row in df1.iterrows():
        if row.type == ">90":
            if len(str(row.Su_Conc)) > 1:
                ir_greater90_lst.insert(su_count, [row.type, "Su", row.Su_Conc, row.Su_Dis_lst, row.Su_dp_lst])
                su_count += 1
                mo_count += 1
                me_count += 1
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Mo_Conc)) > 1:
                ir_greater90_lst.insert(mo_count, [row.type, "Mo", row.Mo_Conc, row.Mo_Dis_lst, row.Mo_dp_lst])
                mo_count += 1
                me_count += 1
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Me_Conc)) > 1:
                ir_greater90_lst.insert(me_count, [row.type, "Me", row.Me_Conc, row.Me_Dis_lst, row.Me_dp_lst])
                me_count += 1
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ma_Conc)) > 1:
                ir_greater90_lst.insert(ma_count, [row.type, "Ma", row.Ma_Conc, row.Ma_Dis_lst, row.Ma_dp_lst])
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ju_Conc)) > 1:
                ir_greater90_lst.insert(ju_count, [row.type, "Ju", row.Ju_Conc, row.Ju_Dis_lst, row.Ju_dp_lst])
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ve_Conc)) > 1:
                ir_greater90_lst.insert(ve_count, [row.type, "Ve", row.Ve_Conc, row.Ve_Dis_lst, row.Ve_dp_lst])
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Sa_Conc)) > 1:
                ir_greater90_lst.insert(sa_count, [row.type, "Sa", row.Sa_Conc, row.Sa_Dis_lst, row.Sa_dp_lst])
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ra_Conc)) > 1:
                ir_greater90_lst.insert(ra_count, [row.type, "Ra", row.Ra_Conc, row.Ra_Dis_lst, row.Ra_dp_lst])
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ke_Conc)) > 1:
                ir_greater90_lst.insert(ke_count, [row.type, "Ke", row.Ke_Conc, row.Ke_Dis_lst, row.Ke_dp_lst])
                ke_count += 1
                as_count += 1

            if len(str(row.As_Conc)) > 1:
                ir_greater90_lst.insert(as_count, [row.type, "As", row.As_Conc, row.As_Dis_lst, row.As_dp_lst])
                as_count += 1
    su_count = 0
    mo_count = 0
    me_count = 0
    ma_count = 0
    ju_count = 0
    ve_count = 0
    sa_count = 0
    ra_count = 0
    ke_count = 0
    as_count = 0
    for index, row in df1.iterrows():
        if row.type == "90<":
            if len(str(row.Su_Conc)) > 1:
                ir_lesser90_lst.insert(su_count, [row.type, "Su", row.Su_Conc, row.Su_Dis_lst, row.Su_dp_lst])
                su_count += 1
                mo_count += 1
                me_count += 1
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Mo_Conc)) > 1:
                ir_lesser90_lst.insert(mo_count, [row.type, "Mo", row.Mo_Conc, row.Mo_Dis_lst, row.Mo_dp_lst])
                mo_count += 1
                me_count += 1
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Me_Conc)) > 1:
                ir_lesser90_lst.insert(me_count, [row.type, "Me", row.Me_Conc, row.Me_Dis_lst, row.Me_dp_lst])
                me_count += 1
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ma_Conc)) > 1:
                ir_lesser90_lst.insert(ma_count, [row.type, "Ma", row.Ma_Conc, row.Ma_Dis_lst, row.Ma_dp_lst])
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ju_Conc)) > 1:
                ir_lesser90_lst.insert(ju_count, [row.type, "Ju", row.Ju_Conc, row.Ju_Dis_lst, row.Ju_dp_lst])
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ve_Conc)) > 1:
                ir_lesser90_lst.insert(ve_count, [row.type, "Ve", row.Ve_Conc, row.Ve_Dis_lst, row.Ve_dp_lst])
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Sa_Conc)) > 1:
                ir_lesser90_lst.insert(sa_count, [row.type, "Sa", row.Sa_Conc, row.Sa_Dis_lst, row.Sa_dp_lst])
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ra_Conc)) > 1:
                ir_lesser90_lst.insert(ra_count, [row.type, "Ra", row.Ra_Conc, row.Ra_Dis_lst, row.Ra_dp_lst])
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ke_Conc)) > 1:
                ir_lesser90_lst.insert(ke_count, [row.type, "Ke", row.Ke_Conc, row.Ke_Dis_lst, row.Ke_dp_lst])
                ke_count += 1
                as_count += 1

            if len(str(row.As_Conc)) > 1:
                ir_lesser90_lst.insert(as_count, [row.type, "As", row.As_Conc, row.As_Dis_lst, row.As_dp_lst])
                as_count += 1
    su_count = 0
    mo_count = 0
    me_count = 0
    ma_count = 0
    ju_count = 0
    ve_count = 0
    sa_count = 0
    ra_count = 0
    ke_count = 0
    as_count = 0
    for index, row in df1.iterrows():
        if row.type == ">60":
            if len(str(row.Su_Conc)) > 1:
                ir_greater60_lst.insert(su_count, [row.type, "Su", row.Su_Conc, row.Su_Dis_lst, row.Su_dp_lst])
                su_count += 1
                mo_count += 1
                me_count += 1
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Mo_Conc)) > 1:
                ir_greater60_lst.insert(mo_count, [row.type, "Mo", row.Mo_Conc, row.Mo_Dis_lst, row.Mo_dp_lst])
                mo_count += 1
                me_count += 1
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Me_Conc)) > 1:
                ir_greater60_lst.insert(me_count, [row.type, "Me", row.Me_Conc, row.Me_Dis_lst, row.Me_dp_lst])
                me_count += 1
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ma_Conc)) > 1:
                ir_greater60_lst.insert(ma_count, [row.type, "Ma", row.Ma_Conc, row.Ma_Dis_lst, row.Ma_dp_lst])
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ju_Conc)) > 1:
                ir_greater60_lst.insert(ju_count, [row.type, "Ju", row.Ju_Conc, row.Ju_Dis_lst, row.Ju_dp_lst])
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ve_Conc)) > 1:
                ir_greater60_lst.insert(ve_count, [row.type, "Ve", row.Ve_Conc, row.Ve_Dis_lst, row.Ve_dp_lst])
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Sa_Conc)) > 1:
                ir_greater60_lst.insert(sa_count, [row.type, "Sa", row.Sa_Conc, row.Sa_Dis_lst, row.Sa_dp_lst])
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ra_Conc)) > 1:
                ir_greater60_lst.insert(ra_count, [row.type, "Ra", row.Ra_Conc, row.Ra_Dis_lst, row.Ra_dp_lst])
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ke_Conc)) > 1:
                ir_greater60_lst.insert(ke_count, [row.type, "Ke", row.Ke_Conc, row.Ke_Dis_lst, row.Ke_dp_lst])
                ke_count += 1
                as_count += 1

            if len(str(row.As_Conc)) > 1:
                ir_greater60_lst.insert(as_count, [row.type, "As", row.As_Conc, row.As_Dis_lst, row.As_dp_lst])
                as_count += 1
    su_count = 0
    mo_count = 0
    me_count = 0
    ma_count = 0
    ju_count = 0
    ve_count = 0
    sa_count = 0
    ra_count = 0
    ke_count = 0
    as_count = 0
    for index, row in df1.iterrows():
        if row.type == "60<":
            if len(str(row.Su_Conc)) > 1:
                ir_lesser60_lst.insert(su_count, [row.type, "Su", row.Su_Conc, row.Su_Dis_lst, row.Su_dp_lst])
                su_count += 1
                mo_count += 1
                me_count += 1
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Mo_Conc)) > 1:
                ir_lesser60_lst.insert(mo_count, [row.type, "Mo", row.Mo_Conc, row.Mo_Dis_lst, row.Mo_dp_lst])
                mo_count += 1
                me_count += 1
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Me_Conc)) > 1:
                ir_lesser60_lst.insert(me_count, [row.type, "Me", row.Me_Conc, row.Me_Dis_lst, row.Me_dp_lst])
                me_count += 1
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ma_Conc)) > 1:
                ir_lesser60_lst.insert(ma_count, [row.type, "Ma", row.Ma_Conc, row.Ma_Dis_lst, row.Ma_dp_lst])
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ju_Conc)) > 1:
                ir_lesser60_lst.insert(ju_count, [row.type, "Ju", row.Ju_Conc, row.Ju_Dis_lst, row.Ju_dp_lst])
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ve_Conc)) > 1:
                ir_lesser60_lst.insert(ve_count, [row.type, "Ve", row.Ve_Conc, row.Ve_Dis_lst, row.Ve_dp_lst])
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Sa_Conc)) > 1:
                ir_lesser60_lst.insert(sa_count, [row.type, "Sa", row.Sa_Conc, row.Sa_Dis_lst, row.Sa_dp_lst])
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ra_Conc)) > 1:
                ir_lesser60_lst.insert(ra_count, [row.type, "Ra", row.Ra_Conc, row.Ra_Dis_lst, row.Ra_dp_lst])
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ke_Conc)) > 1:
                ir_lesser60_lst.insert(ke_count, [row.type, "Ke", row.Ke_Conc, row.Ke_Dis_lst, row.Ke_dp_lst])
                ke_count += 1
                as_count += 1

            if len(str(row.As_Conc)) > 1:
                ir_lesser60_lst.insert(as_count, [row.type, "As", row.As_Conc, row.As_Dis_lst, row.As_dp_lst])
                as_count += 1
    su_count = 0
    mo_count = 0
    me_count = 0
    ma_count = 0
    ju_count = 0
    ve_count = 0
    sa_count = 0
    ra_count = 0
    ke_count = 0
    as_count = 0
    for index, row in df1.iterrows():
        if row.type == ">150":
            if len(str(row.Su_Conc)) > 1:
                ir_greater150_lst.insert(su_count, [row.type, "Su", row.Su_Conc, row.Su_Dis_lst, row.Su_dp_lst])
                su_count += 1
                mo_count += 1
                me_count += 1
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Mo_Conc)) > 1:
                ir_greater150_lst.insert(mo_count, [row.type, "Mo", row.Mo_Conc, row.Mo_Dis_lst, row.Mo_dp_lst])
                mo_count += 1
                me_count += 1
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Me_Conc)) > 1:
                ir_greater150_lst.insert(me_count, [row.type, "Me", row.Me_Conc, row.Me_Dis_lst, row.Me_dp_lst])
                me_count += 1
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ma_Conc)) > 1:
                ir_greater150_lst.insert(ma_count, [row.type, "Ma", row.Ma_Conc, row.Ma_Dis_lst, row.Ma_dp_lst])
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ju_Conc)) > 1:
                ir_greater150_lst.insert(ju_count, [row.type, "Ju", row.Ju_Conc, row.Ju_Dis_lst, row.Ju_dp_lst])
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ve_Conc)) > 1:
                ir_greater150_lst.insert(ve_count, [row.type, "Ve", row.Ve_Conc, row.Ve_Dis_lst, row.Ve_dp_lst])
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Sa_Conc)) > 1:
                ir_greater150_lst.insert(sa_count, [row.type, "Sa", row.Sa_Conc, row.Sa_Dis_lst, row.Sa_dp_lst])
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ra_Conc)) > 1:
                ir_greater150_lst.insert(ra_count, [row.type, "Ra", row.Ra_Conc, row.Ra_Dis_lst, row.Ra_dp_lst])
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ke_Conc)) > 1:
                ir_greater150_lst.insert(ke_count, [row.type, "Ke", row.Ke_Conc, row.Ke_Dis_lst, row.Ke_dp_lst])
                ke_count += 1
                as_count += 1

            if len(str(row.As_Conc)) > 1:
                ir_greater150_lst.insert(as_count, [row.type, "As", row.As_Conc, row.As_Dis_lst, row.As_dp_lst])
                as_count += 1
    df_conj = pd.DataFrame(ir_Conj_lst, columns=["type", "planet", "conca", "distance", "point"])
    df_180 = pd.DataFrame(ir_180_lst, columns=["type", "planet", "conca", "distance", "point"])
    df_greater120 = pd.DataFrame(ir_greater120_lst, columns=["type", "planet", "conca", "distance", "point"])
    df_lesser120 = pd.DataFrame(ir_lesser120_lst, columns=["type", "planet", "conca", "distance", "point"])
    df_greater90 = pd.DataFrame(ir_greater90_lst, columns=["type", "planet", "conca", "distance", "point"])
    df_lesser90 = pd.DataFrame(ir_lesser90_lst, columns=["type", "planet", "conca", "distance", "point"])
    df_greater60 = pd.DataFrame(ir_greater60_lst, columns=["type", "planet", "conca", "distance", "point"])
    df_lesser60 = pd.DataFrame(ir_lesser60_lst, columns=["type", "planet", "conca", "distance", "point"])
    df_greater150 = pd.DataFrame(ir_greater150_lst, columns=["type", "planet", "conca", "distance", "point"])
    return df_conj, df_180, df_greater120, df_lesser120,df_greater90, df_lesser90, df_greater60, df_lesser60, df_greater150



def ir_hoz_graph(graph_pd_df):
    df1 = graph_pd_df.copy()
    x_points = df1["point"].to_list()
    x_points = ([round(i, 1) for i in x_points])
    y_names = df1["conca"].to_list()
    fig = go.Figure(go.Bar(
        x=x_points,
        y=y_names,
        width=0.5,
        orientation='h'))
    fig['layout']['yaxis']['autorange'] = "reversed"
    img_bytes = pio.to_image(fig, format="png")

    # ak = fig.write_image("img/fig1.svg")
    # fig['layout']['xaxis']['autorange'] = "reversed"
    bar_div = opy.plot(fig, auto_open=False, output_type='div')
    return img_bytes


def images_to_db(img_conj, img_180, img_120l, img_120g, img_90l, img_90g, img_60l, img_60g, img_150):
    pass

def integrated_report_pdf_main(su_d, mo_d, me_d, ma_d, ju_d, ve_d, sa_d, ra_d, ke_d, as_d, su_d2, mo_d2, me_d2, ma_d2, ju_d2, ve_d2, sa_d2, ra_d2, ke_d2, as_d2):
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
    df_conj_graph = ir_hoz_graph(df_conj)
    df_180_graph = ir_hoz_graph(df_180)
    df_greater120_graph = ir_hoz_graph(df_greater120)
    df_lesser120_graph = ir_hoz_graph(df_lesser120)
    df_greater90_graph = ir_hoz_graph(df_greater90)
    df_lesser90_graph = ir_hoz_graph(df_lesser90)
    df_greater60_graph = ir_hoz_graph(df_greater60)
    df_lesser60_graph = ir_hoz_graph(df_lesser60)
    df_greater150_graph = ir_hoz_graph(df_greater150)
    # s = plotimages(img_conj = df_conj_graph, img_180 = df_conj_graph, img_120l = df_conj_graph, img_120g = df_conj_graph, img_90l = df_conj_graph, img_90g = df_conj_graph, img_60l = df_conj_graph, img_60g = df_conj_graph, img_150 =df_conj_graph )
    # s.save()
    df_conj = dataframe_to_dict(df_conj)
    df_180 = dataframe_to_dict(df_180)
    df_greater120 = dataframe_to_dict(df_greater120)
    df_lesser120 = dataframe_to_dict(df_lesser120)
    df_greater90 = dataframe_to_dict(df_greater90)
    df_lesser90 = dataframe_to_dict(df_lesser90)
    df_greater60 = dataframe_to_dict(df_greater60)
    df_lesser60 = dataframe_to_dict(df_lesser60)
    df_greater150 = dataframe_to_dict(df_greater150)
    main_dic = {"df_conj" : df_conj, "df_180" : df_180, "df_greater120" : df_greater120, "df_lesser120": df_lesser120,
                "df_greater90": df_greater90, "df_lesser90": df_lesser90, "df_greater60": df_greater60,
                "df_lesser60": df_lesser60, "df_greater150": df_greater150, "bar_div": df_conj_graph,
                "df_180_graph": df_180_graph, "df_greater120_graph": df_greater120_graph,
                "df_lesser120_graph": df_lesser120_graph, "df_greater90_graph": df_greater90_graph,
                "df_lesser90_graph": df_lesser90_graph, "df_greater60_graph": df_greater60_graph,
                "df_lesser60_graph":df_lesser60_graph, "df_greater150_graph": df_greater150_graph}
    return main_dic