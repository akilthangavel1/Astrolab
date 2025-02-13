from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .exaspect import exaspect_main
from persontoperson.views import globalpersondb
from .pmultiple import peekmultiple_main, pk_main, pclear, peeksingle, checkmakers, processSpecificDay
import json 
from .multiple2 import m2_main
from .models import divisionName, modelNames, TrendCharts, PlanetGroupNames, PlanetGroupers
from persontoperson.models import concatenation_points
from .multiple3 import mnatalOperation

def exaspecthome(request):  
    if request.method == "POST":
        degree_dic = globalpersondb()
        main_dic = exaspect_main(degree_dic["p1_su_degree"], degree_dic["p1_mo_degree"], degree_dic["p1_me_degree"], degree_dic["p1_ma_degree"], degree_dic["p1_ju_degree"], degree_dic["p1_ve_degree"], degree_dic["p1_sa_degree"], degree_dic["p1_ra_degree"], degree_dic["p1_ke_degree"], degree_dic["p1_as_degree"], degree_dic["p2_su_degree"], degree_dic["p2_mo_degree"], degree_dic["p2_me_degree"], degree_dic["p2_ma_degree"], degree_dic["p2_ju_degree"], degree_dic["p2_ve_degree"], degree_dic["p2_sa_degree"], degree_dic["p2_ra_degree"], degree_dic["p2_ke_degree"], degree_dic["p2_as_degree"], request)
        return render(request, "cp/exaspect.html", main_dic)
    return render(request, "cp/exaspect.html", {})



def peekmultipledays(request):
    peekmultiple_main(request)
    gList = PlanetGroupNames.objects.all()
    return render(request, "cp/multipledays.html", {"gList": gList})


def peekmultipleplanets(request):
    data = pk_main(request)
    context = {
        "date_lis" :data[0],
        'data': data[1],
            }
    return JsonResponse(context, safe=False)   


def peeker(request):
    return render(request, "peekers.html", {})
    

def peekclearfun(request):
    pclear()
    return JsonResponse(data = {}, safe=False) 


def addsingledate(request):
    peeksingle(request)
    return JsonResponse(data = {}, safe=False) 


def weekcheckers(request):
    checkmakers(request)
    return JsonResponse(data = {}, safe=False) 

def specificdyears(request):
    processSpecificDay(request)
    return JsonResponse(data = {}, safe=False) 

def multiple2home(request):
    m2_main(request)
    gList = PlanetGroupNames.objects.all()
    return render(request, "cp/multiple2.html", {"gList": gList})
    
def pointsHome(request):
    if request.method =="POST":
        fname = request.POST["comname"]
        users = concatenation_points.objects.filter(con_name__startswith=fname)
        return render(request, "cp/psearch.html", {'tbData':users })
    user_list = concatenation_points.objects.all().order_by('id')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, "cp/psearch.html", {"tbData": users})

def pointsEdit(request, id):
    cpdata = concatenation_points.objects.filter(id__in=[id])
    if request.method == "POST":
        id = request.POST['id']
        ctype = request.POST["comtype"]
        cname = request.POST["comname"]
        cpoint = request.POST["compoint"]
        s = concatenation_points(id = id,con_type=ctype, con_name=cname, con_points=cpoint)
        s.save()
        return redirect('/controlpanel/pointsHome/')
    return render(request,'cp/pedit.html', {'cpdata':cpdata})


def pointsDelete(request, id):
    imPeopleData = concatenation_points.objects.get(id=id)
    imPeopleData.delete()
    return redirect('/controlpanel/pointsHome/')


def cpTest(request):
    imPeopleData = concatenation_points.objects.all()
    for i in imPeopleData:
        if i.con_type == "150<":
            concatenation_points.objects.filter(id=i.id).delete()
    return render(request, "cp/cptest.html", {})

def wchanger(request):
    pname = request.GET.get('pname')
    result_dic = {}
    context = {
            "rword" : result_dic,
    }
    return JsonResponse(context, safe=False)   
    
def multiple_categories(request):
    categoryNames = divisionName.objects.all()
    return render(request, "cp/addcategories.html", {"categoryNames": categoryNames})
 
def add_people_category(request):
    if request.method == "GET":
        peopleCategory = request.GET.get('peopleCategory')
        fullName = request.GET.get('fullName')
        birthDTime = request.GET.get('birthDateTime')
        birthLocation = request.GET.get('birthLocation')
        category_obj = divisionName.objects.get(divName=peopleCategory)
        s = modelNames(modelcategory = category_obj, modelFullName = fullName, birthDateTime = birthDTime, modelLocation= birthLocation)
        s.save()
        msg = fullName + " has successfully added to the category "+ peopleCategory
        context = {
            "message" : msg,
        }
        return JsonResponse(context, safe=False)   

def add_category(request):
    if request.method == "GET":
        categoryName = request.GET.get('categoryName')
        s = divisionName(divName = categoryName)
        s.save()
        msg = ""
        context = {
            "message" : msg,
        }
        return JsonResponse(context, safe=False)   
        

def add_multiple_category_division(request):
    return render(request, "cp/multiplecategorydivision.html", {})

def multiple_category_home(request):
    categoriesName = divisionName.objects.all()
    gList = PlanetGroupNames.objects.all()
    return render(request, "cp/multiplecategory.html", {"categoriesName": categoriesName, "gList": gList})

def multiple_category_list(request):
    if request.method == "POST":
        searchBar = request.POST["searchBar"]
        categoriesName = modelNames.objects.filter(modelFullName__startswith= searchBar)
        return render(request, "cp/multiplecategorylist.html", {"categoriesName": categoriesName})
    categoriesName = modelNames.objects.all()
    return render(request, "cp/multiplecategorylist.html", {"categoriesName": categoriesName})

def multiple_category_edit(request, id):
    cpdata = modelNames.objects.get(id=id)
    categoryNames = divisionName.objects.all()
    if request.method == "POST":
        id = request.POST['id']
        modelcategory = request.POST["modelcategory"]
        modelFullName = request.POST["modelFullName"]
        birthDateTime = request.POST["birthDateTime"]
        modelLocation = request.POST["modelLocation"]
        category_obj = divisionName.objects.get(divName=modelcategory)
        s = modelNames(id = id,modelcategory=category_obj, modelFullName=modelFullName, birthDateTime=birthDateTime, modelLocation= modelLocation)
        s.save()
        return redirect('/controlpanel/multiplecategorylist/')
    return render(request,'cp/multiplecategoryedit.html', {'cpdata':cpdata, "categoryNames": categoryNames})

def multiple_category_delete(request, id):
    imPeopleData = modelNames.objects.get(id=id)
    imPeopleData.delete()
    return redirect('/controlpanel/multiplecategorylist/')

def trend_charts_home(request):
    chartName = request.GET.get('chartName')
    catselect = request.GET.get('catselect')
    p2place = request.GET.get('p2place')
    secdate = request.GET.get('secdate')
    sectime = request.GET.get('sectime')
    s = TrendCharts(category = catselect, cName = chartName, cPlace= p2place, cDate= secdate, cTime= sectime)
    s.save()
    context = {
        "message": "msgmsgmsg",
    }
    return JsonResponse(context, safe=False)


def trend_chart_view(request):
    chartDetails = TrendCharts.objects.all()
    return render(request, "cp/trendChartView.html", {"chartDetails": chartDetails})

def trend_chart_edit(request, id):
    cpdata = TrendCharts.objects.get(id=id)
    data = mnatalOperation(cpdata.category, cpdata.cPlace, cpdata.cDate, cpdata.cTime)
    context = {
        "date_lis": data[0],
        'data': data[1],
    }
    return render(request, 'cp/trendcharts.html', context)

def trend_chart_delete(request, id):
    D = TrendCharts.objects.get(id=id)
    D.delete()
    return redirect('/controlpanel/trendchartsview/')

def getgc_home(request):
    gcDic = {}
    glist = request.GET.get('glist')
    data = PlanetGroupers.objects.all()
    for i in data:
        if str(i.groupName) == glist:
            gcDic[i.planetName] = i.planetChangedName
    context = {
        "gcDic": gcDic,
    }
    return JsonResponse(context, safe=False)


def planet_grouper_view(request):
    if request.method =="POST":
        fname = request.POST["fname"]
        users = birthchartdb.objects.filter(fullname=fname)
        return render(request, "p2p/impeoplehome.html", {'users':users })
    gcList = PlanetGroupers.objects.all().order_by('id')
    return render(request,  "cp/planetGrouperView.html", {'gcList': gcList})

def planet_grouper_add(request):
    gpNameList = PlanetGroupNames.objects.all()
    if request.method == "POST":
        groupName = request.POST["groupName"]
        planetName = request.POST["planetName"]
        planetChangedName = request.POST["planetChangedName"]
        obj = PlanetGroupNames.objects.get(groupName=groupName)
        s = PlanetGroupers(groupName = obj, planetName= planetName, planetChangedName= planetChangedName)
        s.save()
        return redirect("/controlpanel/planetgrouperview")
    return render(request, "cp/planetGrouperAdd.html", {"gpNameList": gpNameList})




def planet_grouper_update(request, id):
    gpNameList = PlanetGroupNames.objects.all()
    gpList = PlanetGroupers.objects.get(id=id)
    if request.method == "POST":
        groupName = request.POST["groupName"]
        planetName = request.POST["planetName"]
        planetChangedName = request.POST["planetChangedName"]
        obj = PlanetGroupNames.objects.get(groupName=groupName)
        s = PlanetGroupers(id= id,groupName=obj, planetName=planetName, planetChangedName=planetChangedName)
        s.save()
        return redirect("/controlpanel/planetgrouperview")
    return render(request,'cp/planetGrouperUpdate.html', {"gpNameList": gpNameList, "gpList": gpList})



def planet_grouper_delete(request, id):
    imPeopleData = PlanetGroupers.objects.get(id=id)
    imPeopleData.delete()
    return redirect('/controlpanel/planetgrouperview')


def planet_grouper_name_add(request):
    if request.method == "POST":
        groupName = request.POST["groupName"]
        s = PlanetGroupNames(groupName = groupName)
        s.save()
        return redirect("/controlpanel/planetgrouperview")
    return render(request, "cp/planetGrouperNameAdd.html", {})