from controlpanel.exaspect import interaccion
from django.http.response import JsonResponse
from datetime import date, datetime, timedelta
from .models import MultiDateLisDB
from persontoperson.singledegree import onematch
from .pmultiple import peek_main, all_calculation_multiple_two
from persontoperson.models import GlobalDegree
import dateutil.parser
import pandas as pd


def findDays(year, wname):
    d = date(year, 1, 1)                    
    d += timedelta(days = wname - d.weekday())  
    while d.year == year:
        yield d
        d += timedelta(days = 7)
def remove_extra_quotes(sinter):
    a = sinter.replace("(p1)<", "")
    a = a.replace("(p2)", "")
    return a

def mnatalOperation(date_lst, ttime, p1place, p2place, p2date, p2time):
    date_time_obj = datetime.strptime(p2date, '%Y-%m-%d').date()
    date_time_obj = date_time_obj.strftime('%d.%m.%Y')
    p2date = date_time_obj
    interaccionDf = pd.DataFrame() 
    for dst in date_lst:
        p1datelist = []
        p1date = dst.split('-')
        p1datelist.append(p1date[2])
        p1datelist.append(p1date[1])
        p1datelist.append(p1date[0])
        p1date = '.'.join(p1datelist)
        one_degree_result = onematch(p1date, ttime, p1place)
        two_degree_result = onematch(p2date, p2time, p2place)
        interResult = all_calculation_multiple_two(one_degree_result[0], one_degree_result[1], one_degree_result[2], one_degree_result[3], one_degree_result[4], one_degree_result[5], one_degree_result[6], one_degree_result[7], one_degree_result[8], one_degree_result[9], two_degree_result[0], two_degree_result[1], two_degree_result[2], two_degree_result[3], two_degree_result[4], two_degree_result[5], two_degree_result[6], two_degree_result[7], two_degree_result[8], two_degree_result[9])
        interResult = interResult.rename(columns={"puntaje": dst})  
        interResult.set_index("INTERACCION", inplace=True)
        interaccionDf = pd.concat([interaccionDf, interResult], axis=1)
    interaccionDf = interaccionDf.reset_index()
    interaccionDf['INTERACCION'] = interaccionDf['INTERACCION'].apply(remove_extra_quotes)
    interaccionDf.set_index("INTERACCION", inplace=True)
    return (interaccionDf.columns.tolist()), (interaccionDf.T.to_dict('list'))
    


        


def multiple_rangeft(request):
    date_list = []
    if request.method == "GET":
        user_id = 1
        if (request.GET.get('fdate')):
            fdate = (request.GET.get('fdate'))
            tdate = (request.GET.get('tdate'))
            fdate = (datetime.strptime(fdate, '%Y-%m-%d')).date()
            tdate = (datetime.strptime(tdate, '%Y-%m-%d')).date()
            sdate = fdate  
            edate = tdate
            delta = edate - sdate   
            firstfetch = MultiDateLisDB.objects.filter(id__in=[user_id])  
            firstFetchResult = []  
            if firstfetch:
                for i in firstfetch:
                    firstFetchResult.append(i.datelis)
                for i in range(delta.days + 1):
                    day = sdate + timedelta(days=i)
                    firstFetchResult.append(str(day))
                save_date_lis = ','.join(firstFetchResult)
                s = MultiDateLisDB(id=user_id, datelis = save_date_lis)
                s.save()                
            else:
                for i in range(delta.days + 1):
                    day = sdate + timedelta(days=i)
                    firstFetchResult.append(str(day))
                save_date_lis = ','.join(firstFetchResult)
                s = MultiDateLisDB(id=user_id, datelis = save_date_lis)
                s.save()                
    return JsonResponse(data = {}, safe=False) 

def multiple_sdate(request):
    user_id =1
    str1 = MultiDateLisDB.objects.filter(id__in=[user_id])
    if str1:
        for i in str1:
            str1 = i.datelis   
        date_list = str1.split(",")
        date_list.append(request.GET.get('addsdate'))
        save_date_lis = ','.join(date_list)
        s = MultiDateLisDB(id=user_id, datelis = save_date_lis)
        s.save() 
    else:
        sdt = str(request.GET.get('addsdate'))
        s = MultiDateLisDB(id=user_id, datelis = sdt)
        s.save() 
    return JsonResponse(data = {}, safe=False)


def multiple_weekdays(request):
    processYear = request.GET.get('fyear')
    if request.GET.get('monvalue') == "True":
        d_lis = []
        a =  findDays(int(processYear), 7)
        for i in a:
            d_lis.append(str(i))
        user_id =1
        str1 = MultiDateLisDB.objects.filter(id__in=[user_id])
        if str1:
            for i in str1:
                str1 = i.datelis   
            date_list = str1.split(",")
            save_date_lis = ','.join(date_list)
            d_lis = ','.join(d_lis)
            save_date_lis = save_date_lis + ","+ d_lis
            s = MultiDateLisDB(id=user_id, datelis = save_date_lis)
            s.save() 
        else:
            d_lis = ','.join(d_lis)
            s = MultiDateLisDB(id=user_id, datelis = d_lis)
            s.save() 
    if request.GET.get('tuevalue') == "True":
        d_lis = []
        a =  findDays(int(processYear), 8)
        for i in a:
            d_lis.append(str(i))
        user_id =1  
        str1 = MultiDateLisDB.objects.filter(id__in=[user_id])
        if str1:
            for i in str1:
                str1 = i.datelis   
            date_list = str1.split(",")
            save_date_lis = ','.join(date_list)
            d_lis = ','.join(d_lis)
            save_date_lis = save_date_lis + ","+ d_lis
            s = MultiDateLisDB(id=user_id, datelis = save_date_lis)
            s.save() 
        else:
            d_lis = ','.join(d_lis)
            s = MultiDateLisDB(id=user_id, datelis = d_lis)
            s.save() 
    if request.GET.get('wedvalue') == "True":
        d_lis = []
        a =  findDays(int(processYear), 9)
        for i in a: 
            d_lis.append(str(i))
        user_id =1  
        str1 = MultiDateLisDB.objects.filter(id__in=[user_id])
        if str1:
            for i in str1:
                str1 = i.datelis   
            date_list = str1.split(",")
            save_date_lis = ','.join(date_list)
            d_lis = ','.join(d_lis)
            save_date_lis = save_date_lis + ","+ d_lis
            s = MultiDateLisDB(id=user_id, datelis = save_date_lis)
            s.save() 
        else:
            d_lis = ','.join(d_lis)
            s = MultiDateLisDB(id=user_id, datelis = d_lis)
            s.save() 
    if request.GET.get('thuvalue') == "True":
        d_lis = []
        a =  findDays(int(processYear), 10)
        for i in a: 
            d_lis.append(str(i))
        user_id =1  
        str1 = MultiDateLisDB.objects.filter(id__in=[user_id])
        if str1:
            for i in str1:
                str1 = i.datelis   
            date_list = str1.split(",")
            save_date_lis = ','.join(date_list)
            d_lis = ','.join(d_lis)
            save_date_lis = save_date_lis + ","+ d_lis
            s = MultiDateLisDB(id=user_id, datelis = save_date_lis)
            s.save() 
        else:
            d_lis = ','.join(d_lis)
            s = MultiDateLisDB(id=user_id, datelis = d_lis)
            s.save() 

    if request.GET.get('frivalue') == "True":
        d_lis = []
        a =  findDays(int(processYear), 4)
        for i in a: 
            d_lis.append(str(i))
        user_id =1  
        str1 = MultiDateLisDB.objects.filter(id__in=[user_id])
        if str1:
            for i in str1:
                str1 = i.datelis   
            date_list = str1.split(",")
            save_date_lis = ','.join(date_list)
            d_lis = ','.join(d_lis)
            save_date_lis = save_date_lis + ","+ d_lis
            s = MultiDateLisDB(id=user_id, datelis = save_date_lis)
            s.save() 
        else:
            d_lis = ','.join(d_lis)
            s = MultiDateLisDB(id=user_id, datelis = d_lis)
            s.save() 
    if request.GET.get('satvalue') == "True":
        d_lis = []
        a =  findDays(int(processYear), 5)
        for i in a: 
            d_lis.append(str(i))
        user_id =1  
        str1 = MultiDateLisDB.objects.filter(id__in=[user_id])
        if str1:
            for i in str1:
                str1 = i.datelis   
            date_list = str1.split(",")
            save_date_lis = ','.join(date_list)
            d_lis = ','.join(d_lis)
            save_date_lis = save_date_lis + ","+ d_lis
            s = MultiDateLisDB(id=user_id, datelis = save_date_lis)
            s.save() 
        else:
            d_lis = ','.join(d_lis)
            s = MultiDateLisDB(id=user_id, datelis = d_lis)
            s.save() 
    if request.GET.get('sunvalue') == "True":
        d_lis = []
        a =  findDays(int(processYear), 6)
        for i in a: 
            d_lis.append(str(i))
        user_id =1  
        str1 = MultiDateLisDB.objects.filter(id__in=[user_id])
        if str1:
            for i in str1:
                str1 = i.datelis   
            date_list = str1.split(",")
            save_date_lis = ','.join(date_list)
            d_lis = ','.join(d_lis)
            save_date_lis = save_date_lis + ","+ d_lis
            s = MultiDateLisDB(id=user_id, datelis = save_date_lis)
            s.save() 
        else:
            d_lis = ','.join(d_lis)
            s = MultiDateLisDB(id=user_id, datelis = d_lis)
            s.save() 
    if request.GET.get('s15') == "True":
        user_id = 1
        dls = []
        for i in range(1,13):
            dls.append("15-"+str(i)+"-"+str(processYear))
        str1 = MultiDateLisDB.objects.filter(id__in=[user_id])
        if str1:
            for i in str1:
                str1 = i.datelis   
                dls = ','.join(dls)
                result_dlis = str1 + ","+ dls 
                s = MultiDateLisDB(id=user_id, datelis = result_dlis)
                s.save() 
        else:
            dls = ','.join(dls)
            s = MultiDateLisDB(id=user_id, datelis = dls)
            s.save() 
    if request.GET.get('s115') == "True":
        user_id = 1
        dls = []
        for i in range(1,13):
            dls.append("1-"+str(i)+"-"+str(processYear))
            dls.append("15-"+str(i)+"-"+str(processYear))
        str1 = MultiDateLisDB.objects.filter(id__in=[user_id])
        if str1:
            for i in str1:
                str1 = i.datelis   
                dls = ','.join(dls)
                result_dlis = str1 + ","+ dls 
                s = MultiDateLisDB(id=user_id, datelis = result_dlis)
                s.save() 
        else:
            dls = ','.join(dls)
            s = MultiDateLisDB(id=user_id, datelis = dls)
            s.save() 
                
    if request.GET.get('s110') == "True":
        user_id = 1
        dls = []
        for i in range(1,13):
            dls.append("1-"+str(i)+"-"+str(processYear))
            dls.append("7-"+str(i)+"-"+str(processYear))
            dls.append("14-"+str(i)+"-"+str(processYear))
            dls.append("28-"+str(i)+"-"+str(processYear))
        str1 = MultiDateLisDB.objects.filter(id__in=[user_id])
        if str1:
            for i in str1:
                str1 = i.datelis   
                dls = ','.join(dls)
                result_dlis = str1 + ","+ dls 
                s = MultiDateLisDB(id=user_id, datelis = result_dlis)
                s.save() 
        else:
            dls = ','.join(dls)
            s = MultiDateLisDB(id=user_id, datelis = dls)
            s.save() 
                
    return JsonResponse(data = {}, safe=False)


def multiple_rangeyear(request):
    user_id = 1
    dl = []
    day = request.GET.get('sday')
    month = request.GET.get('smonth')
    fyear = request.GET.get('sfyear')
    tyear = request.GET.get('styear')
    for i in range(int(fyear), (int(tyear)+1)):
        dl.append(str(day)+"-"+str(month)+"-"+str(i))
    str1 = MultiDateLisDB.objects.filter(id__in=[user_id])
    if str1:
        for i in str1:
            str1 = i.datelis   
        dls = ','.join(dl)
        result_dlis = str1 + ","+ dls
        s = MultiDateLisDB(id=user_id, datelis = result_dlis)
        s.save() 
    else:
        dls = ','.join(dl)
        s = MultiDateLisDB(id=user_id, datelis = dls)
        s.save() 
    return JsonResponse(data = {}, safe=False)


def mclear(request):
    user_id = 1
    dfetch = MultiDateLisDB.objects.filter(id__in=[user_id]) 
    dfetch.delete()     
    return JsonResponse(data = {}, safe=False)

def m2_main(request):
    user_id =1
    date_list = []
    str1 = MultiDateLisDB.objects.filter(id__in=[user_id])
    if str1:
        for i in str1:
            str1 = i.datelis   
        date_list = str1.split(",")
    if (request.GET.get('p1place')):
        plt = (request.GET.get('p1place'))
        p1place = (request.GET.get('p1place'))
        p2place = (request.GET.get('p2place'))
        p2date = (request.GET.get('secdate'))
        p2time = (request.GET.get('sectime'))
        ttime = request.GET.get('ttime')
        date_re = mnatalOperation(date_list, ttime, p1place, p2place, str(p2date), str(p2time))
        return date_re

def mresult(request):
    data = m2_main(request)
    context = {
                "date_lis" :data[0],
                'data': data[1],
            }
    return JsonResponse(context, safe=False)   



