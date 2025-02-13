from numpy import degrees
import pandas as pd
from persontoperson.astro_fun import *
from persontoperson.models import GlobalDegree
from persontoperson.personone import *
compTable = pd.DataFrame([[ 'SuAr' , 20 ],
[ 'SuTa' , 4 ],
[ 'SuGe' , 7 ],
[ 'SuCa' , 6 ],
[ 'SuLe' , 15 ],
[ 'SuVg' , 4 ],
[ 'SuLi' , -10 ],
[ 'SuSc' , 5 ],
[ 'SuSg' , 9 ],
[ 'SuCp' , 2 ],
[ 'SuAq' , 5 ],
[ 'SuPi' , 1 ],
[ 'MoAr' , 3 ],
[ 'MoTa' , 15 ],
[ 'MoGe' , 10 ],
[ 'MoCa' , 7 ],
[ 'MoLe' , 9 ],
[ 'MoVg' , 7 ],
[ 'MoLi' , 8 ],
[ 'MoSc' , -10 ],
[ 'MoSg' , 7 ],
[ 'MoCp' , 3 ],
[ 'MoAq' , 5 ],
[ 'MoPi' , 4 ],
[ 'MeAr' , 8 ],
[ 'MeTa' , 2 ],
[ 'MeGe' , 12 ],
[ 'MeCa' , 2 ],
[ 'MeLe' , 8 ],
[ 'MeVg' , 9 ],
[ 'MeLi' , 7 ],
[ 'MeSc' , 5 ],
[ 'MeSg' , 4 ],
[ 'MeCp' , 8 ],
[ 'MeAq' , 8 ],
[ 'MePi' , 1 ],
[ 'MaAr' , 16 ],
[ 'MaTa' , 4 ],
[ 'MaGe' , 8 ],
[ 'MaCa' , -10 ],
[ 'MaLe' , 18 ],
[ 'MaVg' , 5 ],
[ 'MaLi' , 5 ],
[ 'MaSc' , 7 ],
[ 'MaSg' , 7 ],
[ 'MaCp' , 20 ],
[ 'MaAq' , 10 ],
[ 'MaPi' , -5 ],
[ 'JuAr' , 3 ],
[ 'JuTa' , 4 ],
[ 'JuGe' , 3 ],
[ 'JuCa' , 20 ],
[ 'JuLe' , 15 ],
[ 'JuVg' , 3 ],
[ 'JuLi' , 4 ],
[ 'JuSc' , -8 ],
[ 'JuSg' , 15 ],
[ 'JuCp' , -5 ],
[ 'JuAq' , 5 ],
[ 'JuPi' , 15 ],
[ 'VeAr' , 4 ],
[ 'VeTa' , 10 ],
[ 'VeGe' , 7 ],
[ 'VeCa' , 5 ],
[ 'VeLe' , 8 ],
[ 'VeVg' , -5 ],
[ 'VeLi' , 15 ],
[ 'VeSc' , -8 ],
[ 'VeSg' , 5 ],
[ 'VeCp' , 4 ],
[ 'VeAq' , 6 ],
[ 'VePi' , 20 ],
[ 'SaAr' , -10 ],
[ 'SaTa' , 8 ],
[ 'SaGe' , 7 ],
[ 'SaCa' , 4 ],
[ 'SaLe' , -7 ],
[ 'SaVg' , 5 ],
[ 'SaLi' , 25 ],
[ 'SaSc' , -10 ],
[ 'SaSg' , 5 ],
[ 'SaCp' , 17 ],
[ 'SaAq' , 15 ],
[ 'SaPi' , 4 ],
[ 'RaAr' , -10 ],
[ 'RaTa' , 10 ],
[ 'RaGe' , -2 ],
[ 'RaCa' , -12 ],
[ 'RaLe' , -10 ],
[ 'RaVg' , -4 ],
[ 'RaLi' , -2 ],
[ 'RaSc' , -30 ],
[ 'RaSg' , -4 ],
[ 'RaCp' , -8 ],
[ 'RaAq' , -5 ],
[ 'RaPi' , -15 ],
[ 'KeAr' , -15 ],
[ 'KeTa' , -4 ],
[ 'KeGe' , -3 ],
[ 'KeCa' , -15 ],
[ 'KeLe' , -5 ],
[ 'KeVg' , -5 ],
[ 'KeLi' , -4 ],
[ 'KeSc' , -20 ],
[ 'KeSg' , -4 ],
[ 'KeCp' , -4 ],
[ 'KeAq' , -3 ],
[ 'KePi' , -15 ],
[ 'AsAr' , 10 ],
[ 'AsTa' , 12 ],
[ 'AsGe' , 15 ],
[ 'AsCa' , 5 ],
[ 'AsLe' , 15 ],
[ 'AsVg' , 8 ],
[ 'AsLi' , 15 ],
[ 'AsSc' , 2 ],
[ 'AsSg' , 12 ],
[ 'AsCp' , 15 ],
[ 'AsAq' , 10 ],
[ 'AsPi' , 5 ]], columns=["com", "points"])

def graph_point_without_zeroes(single_concatenation_df, single_point_df):
    df1 = single_concatenation_df.copy()
    df2 = single_point_df.copy()
    df1["Su_Point"] = df2.Su_Point.to_list()
    df1["Mo_Point"] = df2.Mo_Point.to_list()
    df1["Me_Point"] = df2.Me_Point.to_list()
    df1["Ma_Point"] = df2.Ma_Point.to_list()
    df1["Ju_Point"] = df2.Ju_Point.to_list()
    df1["Ve_Point"] = df2.Ve_Point.to_list()
    df1["Sa_Point"] = df2.Sa_Point.to_list()
    df1["Ra_Point"] = df2.Ra_Point.to_list()
    df1["Ke_Point"] = df2.Ke_Point.to_list()
    df1["As_Point"] = df2.As_Point.to_list()
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
                ir_Conj_lst.insert(su_count, [row.type, "Su", row.Su_Conc, row.Su_Point])
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
                ir_Conj_lst.insert(mo_count, [row.type, "Mo", row.Mo_Conc, row.Mo_Point])
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
                ir_Conj_lst.insert(me_count, [row.type, "Me", row.Me_Conc, row.Me_Point])
                me_count += 1
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ma_Conc)) > 1:
                ir_Conj_lst.insert(ma_count, [row.type, "Ma", row.Ma_Conc, row.Ma_Point])
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1


            if len(str(row.Ju_Conc)) > 1:
                ir_Conj_lst.insert(ju_count, [row.type, "Ju", row.Ju_Conc, row.Ju_Point])
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ve_Conc)) > 1:
                ir_Conj_lst.insert(ve_count, [row.type, "Ve", row.Ve_Conc, row.Ve_Point])
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Sa_Conc)) > 1:
                ir_Conj_lst.insert(sa_count, [row.type, "Sa", row.Sa_Conc, row.Sa_Point])
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ra_Conc)) > 1:
                ir_Conj_lst.insert(ra_count, [row.type, "Ra", row.Ra_Conc, row.Ra_Point])
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ke_Conc)) > 1:
                ir_Conj_lst.insert(ke_count, [row.type, "Ke", row.Ke_Conc, row.Ke_Point])
                ke_count += 1
                as_count += 1

            if len(str(row.As_Conc)) > 1:
                ir_Conj_lst.insert(as_count, [row.type, "As", row.As_Conc, row.As_Point])
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
                ir_180_lst.insert(su_count, [row.type, "Su", row.Su_Conc, row.Su_Point])
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
                ir_180_lst.insert(mo_count, [row.type, "Mo", row.Mo_Conc,  row.Mo_Point])
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
                ir_180_lst.insert(me_count, [row.type, "Me", row.Me_Conc, row.Me_Point])
                me_count += 1
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ma_Conc)) > 1:
                ir_180_lst.insert(ma_count, [row.type, "Ma", row.Ma_Conc, row.Ma_Point])
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ju_Conc)) > 1:
                ir_180_lst.insert(ju_count, [row.type, "Ju", row.Ju_Conc,  row.Ju_Point])
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ve_Conc)) > 1:
                ir_180_lst.insert(ve_count, [row.type, "Ve", row.Ve_Conc, row.Ve_Point])
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Sa_Conc)) > 1:
                ir_180_lst.insert(sa_count, [row.type, "Sa", row.Sa_Conc,  row.Sa_Point])
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ra_Conc)) > 1:
                ir_180_lst.insert(ra_count, [row.type, "Ra", row.Ra_Conc,  row.Ra_Point])
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ke_Conc)) > 1:
                ir_180_lst.insert(ke_count, [row.type, "Ke", row.Ke_Conc,  row.Ke_Point])
                ke_count += 1
                as_count += 1

            if len(str(row.As_Conc)) > 1:
                ir_180_lst.insert(as_count, [row.type, "As", row.As_Conc,  row.As_Point])
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
                ir_greater120_lst.insert(su_count, [row.type, "Su", row.Su_Conc,  row.Su_Point])
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
                ir_greater120_lst.insert(mo_count, [row.type, "Mo", row.Mo_Conc,  row.Mo_Point])
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
                ir_greater120_lst.insert(me_count, [row.type, "Me", row.Me_Conc, row.Me_Point])
                me_count += 1
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ma_Conc)) > 1:
                ir_greater120_lst.insert(ma_count, [row.type, "Ma", row.Ma_Conc, row.Ma_Point])
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ju_Conc)) > 1:
                ir_greater120_lst.insert(ju_count, [row.type, "Ju", row.Ju_Conc,  row.Ju_Point])
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ve_Conc)) > 1:
                ir_greater120_lst.insert(ve_count, [row.type, "Ve", row.Ve_Conc, row.Ve_Point])
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Sa_Conc)) > 1:
                ir_greater120_lst.insert(sa_count, [row.type, "Sa", row.Sa_Conc,  row.Sa_Point])
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ra_Conc)) > 1:
                ir_greater120_lst.insert(ra_count, [row.type, "Ra", row.Ra_Conc,  row.Ra_Point])
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ke_Conc)) > 1:
                ir_greater120_lst.insert(ke_count, [row.type, "Ke", row.Ke_Conc,  row.Ke_Point])
                ke_count += 1
                as_count += 1

            if len(str(row.As_Conc)) > 1:
                ir_greater120_lst.insert(as_count, [row.type, "As", row.As_Conc,  row.As_Point])
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
                ir_lesser120_lst.insert(su_count, [row.type, "Su", row.Su_Conc,  row.Su_Point])
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
                ir_lesser120_lst.insert(mo_count, [row.type, "Mo", row.Mo_Conc,  row.Mo_Point])
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
                ir_lesser120_lst.insert(me_count, [row.type, "Me", row.Me_Conc, row.Me_Point])
                me_count += 1
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ma_Conc)) > 1:
                ir_lesser120_lst.insert(ma_count, [row.type, "Ma", row.Ma_Conc, row.Ma_Point])
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ju_Conc)) > 1:
                ir_lesser120_lst.insert(ju_count, [row.type, "Ju", row.Ju_Conc,  row.Ju_Point])
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ve_Conc)) > 1:
                ir_lesser120_lst.insert(ve_count, [row.type, "Ve", row.Ve_Conc, row.Ve_Point])
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Sa_Conc)) > 1:
                ir_lesser120_lst.insert(sa_count, [row.type, "Sa", row.Sa_Conc,  row.Sa_Point])
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ra_Conc)) > 1:
                ir_lesser120_lst.insert(ra_count, [row.type, "Ra", row.Ra_Conc,  row.Ra_Point])
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ke_Conc)) > 1:
                ir_lesser120_lst.insert(ke_count, [row.type, "Ke", row.Ke_Conc,  row.Ke_Point])
                ke_count += 1
                as_count += 1

            if len(str(row.As_Conc)) > 1:
                ir_lesser120_lst.insert(as_count, [row.type, "As", row.As_Conc,  row.As_Point])
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
                ir_greater90_lst.insert(su_count, [row.type, "Su", row.Su_Conc,  row.Su_Point])
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
                ir_greater90_lst.insert(mo_count, [row.type, "Mo", row.Mo_Conc,  row.Mo_Point])
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
                ir_greater90_lst.insert(me_count, [row.type, "Me", row.Me_Conc, row.Me_Point])
                me_count += 1
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ma_Conc)) > 1:
                ir_greater90_lst.insert(ma_count, [row.type, "Ma", row.Ma_Conc, row.Ma_Point])
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ju_Conc)) > 1:
                ir_greater90_lst.insert(ju_count, [row.type, "Ju", row.Ju_Conc,  row.Ju_Point])
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ve_Conc)) > 1:
                ir_greater90_lst.insert(ve_count, [row.type, "Ve", row.Ve_Conc, row.Ve_Point])
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Sa_Conc)) > 1:
                ir_greater90_lst.insert(sa_count, [row.type, "Sa", row.Sa_Conc,  row.Sa_Point])
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ra_Conc)) > 1:
                ir_greater90_lst.insert(ra_count, [row.type, "Ra", row.Ra_Conc,  row.Ra_Point])
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ke_Conc)) > 1:
                ir_greater90_lst.insert(ke_count, [row.type, "Ke", row.Ke_Conc,  row.Ke_Point])
                ke_count += 1
                as_count += 1

            if len(str(row.As_Conc)) > 1:
                ir_greater90_lst.insert(as_count, [row.type, "As", row.As_Conc,  row.As_Point])
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
                ir_lesser90_lst.insert(su_count, [row.type, "Su", row.Su_Conc,  row.Su_Point])
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
                ir_lesser90_lst.insert(mo_count, [row.type, "Mo", row.Mo_Conc,  row.Mo_Point])
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
                ir_lesser90_lst.insert(me_count, [row.type, "Me", row.Me_Conc, row.Me_Point])
                me_count += 1
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ma_Conc)) > 1:
                ir_lesser90_lst.insert(ma_count, [row.type, "Ma", row.Ma_Conc, row.Ma_Point])
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ju_Conc)) > 1:
                ir_lesser90_lst.insert(ju_count, [row.type, "Ju", row.Ju_Conc,  row.Ju_Point])
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ve_Conc)) > 1:
                ir_lesser90_lst.insert(ve_count, [row.type, "Ve", row.Ve_Conc, row.Ve_Point])
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Sa_Conc)) > 1:
                ir_lesser90_lst.insert(sa_count, [row.type, "Sa", row.Sa_Conc,  row.Sa_Point])
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ra_Conc)) > 1:
                ir_lesser90_lst.insert(ra_count, [row.type, "Ra", row.Ra_Conc,  row.Ra_Point])
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ke_Conc)) > 1:
                ir_lesser90_lst.insert(ke_count, [row.type, "Ke", row.Ke_Conc,  row.Ke_Point])
                ke_count += 1
                as_count += 1

            if len(str(row.As_Conc)) > 1:
                ir_lesser90_lst.insert(as_count, [row.type, "As", row.As_Conc,  row.As_Point])
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
                ir_greater60_lst.insert(su_count, [row.type, "Su", row.Su_Conc,  row.Su_Point])
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
                ir_greater60_lst.insert(mo_count, [row.type, "Mo", row.Mo_Conc,  row.Mo_Point])
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
                ir_greater60_lst.insert(me_count, [row.type, "Me", row.Me_Conc, row.Me_Point])
                me_count += 1
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ma_Conc)) > 1:
                ir_greater60_lst.insert(ma_count, [row.type, "Ma", row.Ma_Conc, row.Ma_Point])
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ju_Conc)) > 1:
                ir_greater60_lst.insert(ju_count, [row.type, "Ju", row.Ju_Conc,  row.Ju_Point])
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ve_Conc)) > 1:
                ir_greater60_lst.insert(ve_count, [row.type, "Ve", row.Ve_Conc, row.Ve_Point])
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Sa_Conc)) > 1:
                ir_greater60_lst.insert(sa_count, [row.type, "Sa", row.Sa_Conc,  row.Sa_Point])
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ra_Conc)) > 1:
                ir_greater60_lst.insert(ra_count, [row.type, "Ra", row.Ra_Conc,  row.Ra_Point])
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ke_Conc)) > 1:
                ir_greater60_lst.insert(ke_count, [row.type, "Ke", row.Ke_Conc,  row.Ke_Point])
                ke_count += 1
                as_count += 1

            if len(str(row.As_Conc)) > 1:
                ir_greater60_lst.insert(as_count, [row.type, "As", row.As_Conc,  row.As_Point])
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
                ir_lesser60_lst.insert(su_count, [row.type, "Su", row.Su_Conc,  row.Su_Point])
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
                ir_lesser60_lst.insert(mo_count, [row.type, "Mo", row.Mo_Conc,  row.Mo_Point])
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
                ir_lesser60_lst.insert(me_count, [row.type, "Me", row.Me_Conc, row.Me_Point])
                me_count += 1
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ma_Conc)) > 1:
                ir_lesser60_lst.insert(ma_count, [row.type, "Ma", row.Ma_Conc, row.Ma_Point])
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ju_Conc)) > 1:
                ir_lesser60_lst.insert(ju_count, [row.type, "Ju", row.Ju_Conc,  row.Ju_Point])
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ve_Conc)) > 1:
                ir_lesser60_lst.insert(ve_count, [row.type, "Ve", row.Ve_Conc, row.Ve_Point])
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Sa_Conc)) > 1:
                ir_lesser60_lst.insert(sa_count, [row.type, "Sa", row.Sa_Conc,  row.Sa_Point])
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ra_Conc)) > 1:
                ir_lesser60_lst.insert(ra_count, [row.type, "Ra", row.Ra_Conc,  row.Ra_Point])
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ke_Conc)) > 1:
                ir_lesser60_lst.insert(ke_count, [row.type, "Ke", row.Ke_Conc,  row.Ke_Point])
                ke_count += 1
                as_count += 1

            if len(str(row.As_Conc)) > 1:
                ir_lesser60_lst.insert(as_count, [row.type, "As", row.As_Conc,  row.As_Point])
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
                ir_greater150_lst.insert(su_count, [row.type, "Su", row.Su_Conc,  row.Su_Point])
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
                ir_greater150_lst.insert(mo_count, [row.type, "Mo", row.Mo_Conc,  row.Mo_Point])
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
                ir_greater150_lst.insert(me_count, [row.type, "Me", row.Me_Conc, row.Me_Point])
                me_count += 1
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ma_Conc)) > 1:
                ir_greater150_lst.insert(ma_count, [row.type, "Ma", row.Ma_Conc, row.Ma_Point])
                ma_count += 1
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ju_Conc)) > 1:
                ir_greater150_lst.insert(ju_count, [row.type, "Ju", row.Ju_Conc,  row.Ju_Point])
                ju_count += 1
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ve_Conc)) > 1:
                ir_greater150_lst.insert(ve_count, [row.type, "Ve", row.Ve_Conc, row.Ve_Point])
                ve_count += 1
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Sa_Conc)) > 1:
                ir_greater150_lst.insert(sa_count, [row.type, "Sa", row.Sa_Conc,  row.Sa_Point])
                sa_count += 1
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ra_Conc)) > 1:
                ir_greater150_lst.insert(ra_count, [row.type, "Ra", row.Ra_Conc,  row.Ra_Point])
                ra_count += 1
                ke_count += 1
                as_count += 1

            if len(str(row.Ke_Conc)) > 1:
                ir_greater150_lst.insert(ke_count, [row.type, "Ke", row.Ke_Conc,  row.Ke_Point])
                ke_count += 1
                as_count += 1

            if len(str(row.As_Conc)) > 1:
                ir_greater150_lst.insert(as_count, [row.type, "As", row.As_Conc,  row.As_Point])
                as_count += 1
    df_conj = pd.DataFrame(ir_Conj_lst, columns=["type", "planet", "conca", "point"])
    df_180 = pd.DataFrame(ir_180_lst, columns=["type", "planet", "conca",  "point"])
    df_greater120 = pd.DataFrame(ir_greater120_lst, columns=["type", "planet", "conca",  "point"])
    df_lesser120 = pd.DataFrame(ir_lesser120_lst, columns=["type", "planet", "conca",  "point"])
    df_greater90 = pd.DataFrame(ir_greater90_lst, columns=["type", "planet", "conca","point"])
    df_lesser90 = pd.DataFrame(ir_lesser90_lst, columns=["type", "planet", "conca", "point"])
    df_greater60 = pd.DataFrame(ir_greater60_lst, columns=["type", "planet", "conca", "point"])
    df_lesser60 = pd.DataFrame(ir_lesser60_lst, columns=["type", "planet", "conca", "point"])
    df_greater150 = pd.DataFrame(ir_greater150_lst, columns=["type", "planet", "conca","point"])
    return df_conj, df_180, df_greater120, df_lesser120,df_greater90, df_lesser90, df_greater60, df_lesser60, df_greater150

def ir_hoz_graph(graph_pd_df):
    a = []
    concaLis = graph_pd_df["conca"].tolist()
    disLis = graph_pd_df["point"].tolist()
    a.append(concaLis)
    a.append(disLis)
    return a


def person_one_chart_main():
    degrees = GlobalDegree.objects.get(id=1)
    constants_start_and_end_limit = constants_limit_for_sign()
    eve_person_one = event_person(constants_start_and_end_limit, degrees.suDegree,degrees.moDegree,degrees.meDegree,degrees.maDegree,degrees.juDegree,degrees.veDegree,degrees.saDegree,degrees.raDegree,degrees.keDegree,degrees.asDegree)
    house_df = house_table(eve_person_one)
    house_sign_df = house_and_sign(house_df)
    sign_house_df = sign_and_house(house_sign_df)
    sign_planet_house_df = sign_planet_and_house(eve_person_one, sign_house_df)
    single_concatenation_df = single_concatenation_table(sign_planet_house_df)
    single_point_df = single_points_table(single_concatenation_df)
    ir_con_graph_df = (graph_point_without_zeroes(single_concatenation_df, single_point_df))
    df_conj, df_180, df_greater120, df_lesser120, df_greater90, df_lesser90, df_greater60, df_lesser60, df_greater150 = ir_con_graph_df[0], ir_con_graph_df[1], ir_con_graph_df[2], ir_con_graph_df[3], ir_con_graph_df[4], ir_con_graph_df[5], ir_con_graph_df[6], ir_con_graph_df[7], ir_con_graph_df[8]
    df_conj_graph = ir_hoz_graph(df_conj)
    df_conj_conca = df_conj_graph[0]
    df_conj_dis = df_conj_graph[1]
    df_180_graph = ir_hoz_graph(df_180)
    df_180_conca = df_180_graph[0]
    df_180_dis = df_180_graph[1]
    df_greater120_graph = ir_hoz_graph(df_greater120)
    df_lesser120_graph = ir_hoz_graph(df_lesser120)
    df_greater90_graph = ir_hoz_graph(df_greater90)
    df_lesser90_graph = ir_hoz_graph(df_lesser90)
    df_greater60_graph = ir_hoz_graph(df_greater60)
    df_lesser60_graph = ir_hoz_graph(df_lesser60)
    df_greater150_graph = ir_hoz_graph(df_greater150)
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
                "df_lesser60": df_lesser60, "df_greater150": df_greater150, "df_conj_conca": df_conj_conca, "df_conj_dis":df_conj_dis,
                "df_180_conca": df_180_conca, "df_180_dis": df_180_dis, "df_greater120_graph": df_greater120_graph,
                "df_lesser120_graph": df_lesser120_graph, "df_greater90_graph": df_greater90_graph,
                "df_lesser90_graph": df_lesser90_graph, "df_greater60_graph": df_greater60_graph,
                "df_lesser60_graph":df_lesser60_graph, "df_greater150_graph": df_greater150_graph}
    return main_dic


def adding_aspects(eve_person_one, point_planet_aspects_df):
    df = point_planet_aspects_df.copy()
    df1= pd.DataFrame()
    df1["rplanet"] = ["Su", "Mo", "Me", "Ma", "Ju", "Ve", "Sa", "Ra", "Ke", "As"]
    df1["planet"] = eve_person_one["sign_name"].tolist()
    df1["compl"] = df1["rplanet"] + df1["planet"] 
    rcpointsLis = [] 
    for index, row in df1.iterrows():
        rcpointsLis.append((compTable.loc[compTable.com == row.compl].points).iat[0]*10)
    df1['resultpoint'] = rcpointsLis
    confusedPoints=[50.0, -25.0, 70.0, 50.0, 55.0, 85.0, -45.0, 0, 0, 0]
    df1['confusedPoints'] = confusedPoints
    df1['finalResult']= df1["resultpoint"]+ df1["confusedPoints"]
    df["sign"] = df1['finalResult'].tolist()
    df["aspectsign"] = (df["total"]/3+ df["sign"])/2
    # print(df)
    return df


def add_p1form():
    degrees = GlobalDegree.objects.get(id=1)
    constants_start_and_end_limit = constants_limit_for_sign()
    eve_person_one = event_person(constants_start_and_end_limit, degrees.suDegree,degrees.moDegree,degrees.meDegree,degrees.maDegree,degrees.juDegree,degrees.veDegree,degrees.saDegree,degrees.raDegree,degrees.keDegree,degrees.asDegree)
    house_df = house_table(eve_person_one)
    house_sign_df = house_and_sign(house_df)
    sign_house_df = sign_and_house(house_sign_df)
    sign_planet_house_df = sign_planet_and_house(eve_person_one, sign_house_df)
    single_concatenation_df = single_concatenation_table(sign_planet_house_df)
    single_point_df = single_points_table(single_concatenation_df)
    point_planet_aspects_df = point_planets_planet_aspects(single_point_df)
    point_planet_aspects_df = adding_aspects(eve_person_one, point_planet_aspects_df)
    planetLis = ["Su", "Mo", "Me", "Ma", "Ju", "Ve", "Sa", "Ra", "Ke", "As"]
    aspectsign = point_planet_aspects_df["aspectsign"].tolist()
    point_planet_aspects_df = dataframe_to_dict(point_planet_aspects_df)
    main_dic = {"point_planet_aspects_df": point_planet_aspects_df, "planetLis": planetLis, "aspectsign": aspectsign }
    return main_dic    