from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render
from .multi4 import multi4_main
from .multi5 import p1_person_loop
from controlpanel.models import divisionName, MultiDateLisDB
from .models import CombinationGroupNames, CombinationGrouperChangers, Model1Charts, Model2Charts, TrendChart4, TrendChart1, TrendChart2, TrendChart3
from controlpanel.models import DateLisDB, PlanetGroupers
import csv
from django.http import HttpResponse
from persontoperson.models import concatenation_points
from controlpanel.models import modelNames
import pandas as pd


def multiple4_home(request):
    categoriesName = divisionName.objects.all()
    CombGrpNames = CombinationGroupNames.objects.all()
    return render(request, "multiple/multiple4Home.html", {"categoriesName": categoriesName, "CombGrpNames": CombGrpNames})


resultDic = ""


def multi4_data(request):
    if request.is_ajax():
        peopleCategory = request.GET.get('peopleCategory')
        fullName = request.GET.get('fullName')
        birthDate = request.GET.get('birthDate')
        birthTime = request.GET.get('birthTime')
        location = request.GET.get('location')
        nameLis, resultDic = multi4_main(peopleCategory, fullName, birthDate, birthTime, location)
        context = {
            "nameLis": nameLis,
            "resultDic": resultDic,
        }
        return JsonResponse(context, safe=False)

def add_combination_group_names(request):
    return render(request, "multiple/addCombinationGroupNames.html", {})


def add_combination_group_names_req(request):
    msg = ""
    groupName = request.GET.get('groupName')
    try:
        n = CombinationGroupNames.objects.get(groupName=groupName)
        # number already exists
        msg = groupName + " has already saved"
    except ObjectDoesNotExist:
        # number does not exist
        s = CombinationGroupNames(groupName=groupName)
        s.save()
        msg = groupName + " has successfully saved"
    context = {
        "message": msg,
    }
    return JsonResponse(context, safe=False)


def view_comb_group_name(request):
    data = CombinationGroupNames.objects.all().order_by('-id')
    return render(request, "multiple/viewCombGroupNames.html", {"data": data})


def update_comb_group_name(request):
    updateCombId = request.GET.get('updateCombId')
    updateGroupName = request.GET.get('updateGroupName')
    combObj = CombinationGroupNames(id=updateCombId, groupName=updateGroupName)
    combObj.save()
    context = {
    }
    return JsonResponse(context, safe=False)


def update_comb_group_name_req(request, ):
    objId = int(request.GET.get('objId'))
    combObj = CombinationGroupNames.objects.get(id=objId)
    context = {
        "grpId": objId,
        "grpName": combObj.groupName,
    }
    return JsonResponse(context, safe=False)


def delete_combination_group_name(request):
    updateCombId = request.GET.get('updateCombId')
    combObj = CombinationGroupNames.objects.get(id=int(updateCombId))
    combObj.delete()
    context = {
    }
    return JsonResponse(context, safe=False)


def add_combination_changer(request):
    data = CombinationGroupNames.objects.all().order_by('-id')
    return render(request, "multiple/addCombChanger.html", {"data": data})


def add_combination_changer_req(request):
    msg = ""
    groupName = request.GET.get('groupName')
    planetName = request.GET.get('planetName')
    planetChangedName = request.GET.get('planetChangedName')
    try:
        grpCategory = CombinationGroupNames.objects.get(groupName=groupName)
        s = CombinationGrouperChangers(groupName=grpCategory, planetName=planetName,
                                       planetChangedName=planetChangedName)
        s.save()
        # number already exists
        msg = planetName + " has successfully saved in group " + groupName
    except ObjectDoesNotExist:
        # number does not exist
        s = CombinationGroupNames(groupName=groupName)
        s.save()
        msg = groupName + " has successfully saved"
    context = {
        "message": msg,
    }
    return JsonResponse(context, safe=False)


def view_comb_changer(request):
    data = CombinationGrouperChangers.objects.all().order_by('-id')
    return render(request, "multiple/viewCombChanger.html", {"data": data})


def update_combination_changer(request):
    updateCombId = request.GET.get('updateCombId')
    updateGroupName = request.GET.get('updateGroupName')
    updateCombination = request.GET.get('updateCombination')
    updateCombinationChanger = request.GET.get('updateCombinationChanger')
    combObj = CombinationGroupNames.objects.get(groupName=updateGroupName)
    obj = CombinationGrouperChangers(id=updateCombId, groupName=combObj, planetName=updateCombination,
                                     planetChangedName=updateCombinationChanger)
    obj.save()
    context = {
    }
    return JsonResponse(context, safe=False)


def update_comb_changer_req(request):
    groupNamesLis = []
    groupNames = list(CombinationGroupNames.objects.all())
    for i in groupNames:
        groupNamesLis.append(i.groupName)
    objId = int(request.GET.get('objId'))
    n = CombinationGrouperChangers.objects.get(id=objId)
    groupNamesLis.remove(str(n.groupName))
    groupNamesLis.insert(0, str(n.groupName))
    context = {
        "grpNames": groupNamesLis,
        "pltName": n.planetName,
        "pltChgName": n.planetChangedName,
    }
    return JsonResponse(context, safe=False)


def delete_combination_changer(request):
    updateCombId = request.GET.get('updateCombId')
    combObj = CombinationGrouperChangers.objects.get(id=int(updateCombId))
    combObj.delete()
    context = {
    }
    return JsonResponse(context, safe=False)


def multiple1_chart_save(request):
    multi1ChartName = request.GET.get('multi1ChartName')
    date_lis = request.GET.get('date_lis')
    poverLst = request.GET.get('poverLst')
    graphData = (request.GET.get('graphData'))
    graphData = graphData.replace("false", "False")
    obj = TrendChart1(chartName= multi1ChartName, dateLis= date_lis, combinations= poverLst, data= graphData)
    obj.save()
    context = {
    }
    return JsonResponse(context, safe=False)


def m1charts_view(request):
    data = TrendChart1.objects.all().order_by('-id')
    return render(request, "multiple/m1ChartsView.html", {"data": data})


def m1charts_delete(request):
    m1ChartId = request.GET.get('m1ChartId')
    combObj = TrendChart1.objects.get(id=int(m1ChartId))
    combObj.delete()
    context = {
    }
    return JsonResponse(context, safe=False)


def m1charts_generate(request, id):
    chartObj = TrendChart1.objects.get(id=int(id))
    chartName = chartObj.chartName
    dateLis = (chartObj.dateLis).split(',')
    combinations = chartObj.combinations
    data = chartObj.data
    return render(request, "multiple/m1ChartGenerate.html", {"chartName": chartName, "dateLis": dateLis, "combinations": combinations, "data": data })


def multiple2_chart_save(request):
    chartName = (request.GET.get('chartName'))
    poverLst = (request.GET.get('poverLst'))
    graphData = (request.GET.get('graphData'))
    dateLis = (request.GET.get('dateLis'))
    obj = TrendChart2(chartName=chartName, dateLis=dateLis, combinations=poverLst, data=graphData)
    obj.save()

    context = {
    }
    return JsonResponse(context, safe=False)


def m2charts_view(request):
    data = TrendChart2.objects.all().order_by('-id')
    return render(request, "multiple/m2ChartsView.html", {"data": data})


def m2charts_delete(request):
    m1ChartId = request.GET.get('m1ChartId')
    combObj = TrendChart2.objects.get(id=int(m1ChartId))
    combObj.delete()
    context = {
    }
    return JsonResponse(context, safe=False)


def m2charts_generate(request, id):
    chartObj = TrendChart2.objects.get(id=int(id))
    chartName = chartObj.chartName
    dateLis = chartObj.dateLis.split(',')
    combinations = chartObj.combinations
    graphData = eval(chartObj.data)
    return render(request, "multiple/m2ChartGenerate.html", {"chartName": chartName, "dateLis": dateLis, "combinations": combinations, "graphData": graphData})

def multiple3_chart_save(request):
    chartName = (request.GET.get('chartName'))
    poverLst = (request.GET.get('poverLst'))
    graphData = (request.GET.get('graphData'))
    dateLis = (request.GET.get('dateLis'))
    obj = TrendChart3(chartName=chartName, dateLis=dateLis, combinations=poverLst, data=graphData)
    obj.save()

    context = {
    }
    return JsonResponse(context, safe=False)


def m3charts_view(request):
    data = TrendChart3.objects.all().order_by('-id')
    return render(request, "multiple/m3ChartsView.html", {"data": data})


def m3charts_delete(request):
    m1ChartId = request.GET.get('m1ChartId')
    combObj = TrendChart3.objects.get(id=int(m1ChartId))
    combObj.delete()
    context = {
    }
    return JsonResponse(context, safe=False)


def m3charts_generate(request, id):
    chartObj = TrendChart3.objects.get(id=int(id))
    chartName = chartObj.chartName
    dateLis = chartObj.dateLis.split(',')
    combinations = chartObj.combinations
    graphData = eval(chartObj.data)
    return render(request, "multiple/m3ChartGenerate.html", {"chartName": chartName, "dateLis": dateLis, "combinations": combinations, "graphData": graphData})


def downloadable_files(request):
    # data = concatenation_points.objects.all()
    return render(request, "multiple/downFiles.html", {})


def downloadable_comb_changer(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="CombinationChanger.csv"'
    combChangers = CombinationGrouperChangers.objects.all()
    writer = csv.writer(response)
    writer.writerow(["Group Name", "Combination", "Combination Changer"])
    for i in combChangers:
        writer.writerow([i.groupName, i.planetName, i.planetChangedName])
    return response


def downloadable_plt_changer(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="PlanetChangers.csv"'
    combChangers = PlanetGroupers.objects.all()
    writer = csv.writer(response)
    writer.writerow(["Group Name", "Combination", "Combination Changer"])
    for i in combChangers:
        writer.writerow([i.groupName, i.planetName, i.planetChangedName])
    return response

def downloadable_category(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Category.csv"'
    combChangers = modelNames.objects.all()
    writer = csv.writer(response)
    writer.writerow(["Model Category", "FullName", "Birth Datetime", "Birth Location"])
    for i in combChangers:
        writer.writerow([i.modelcategory, i.modelFullName, i.birthDateTime, i.modelLocation])
    return response

def downloadable_combination_points(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Points.csv"'
    combChangers = concatenation_points.objects.all()
    writer = csv.writer(response)
    writer.writerow(["Combination Type", "Combination Name", "Combination Points"])
    for i in combChangers:
        writer.writerow([i.con_type, i.con_name, i.con_points])
    return response

def combination_plt_req(request):
    endResult = []
    context = {}
    if request.is_ajax():
        q = request.GET.get('combValue')
        search_qs = concatenation_points.objects.filter(con_name__startswith=q)
        for i in search_qs:
            endResult.append(i.con_name)
        context = {"endResult": endResult}
    return JsonResponse(context, safe=False)


def multiple4_chart_save(request):
    chartName = (request.GET.get('chartName'))
    peopleCategory = (request.GET.get('peopleCategory'))
    fullName = (request.GET.get('fullName'))
    birthDate = (request.GET.get('birthDate'))
    birthTime = (request.GET.get('birthTime'))
    location = (request.GET.get('location'))
    combLis = (request.GET.get('combLis'))
    nameLis, resultDic = multi4_main(peopleCategory, fullName, birthDate, birthTime, location)
    combLis = combLis.split(",")

    chartDic = {}
    for i in combLis:
        chartDic[i] = resultDic[i]["pnt"]
    chartDic = ""+str(chartDic)+""
    s = TrendChart4(chartName =chartName, nameLis= nameLis, combinations =combLis, data = chartDic)
    s.save()
    context = {
    }
    return JsonResponse(context, safe=False)


def m4charts_view(request):
    data = TrendChart4.objects.all().order_by('-id')
    return render(request, "multiple/m4ChartsView.html", {"data": data})


def m4charts_generate(request, id):
    chartObj = TrendChart4.objects.get(id=int(id))
    nameLis = eval(chartObj.nameLis)
    combinations = eval(chartObj.combinations)
    data = eval(chartObj.data)
    return render(request, "multiple/m4ChartGenerate.html", {"nameLis": nameLis, "combinations": combinations, "data": data})

def m4charts_delete(request):
    m4ChartId = request.GET.get('m1ChartId')
    combObj = TrendChart4.objects.get(id=int(m4ChartId))
    combObj.delete()
    context = {
    }
    return JsonResponse(context, safe=False)

def applying_combination_changers(request):
    combDic = {}
    combinationApply = request.GET.get('combinationApply')
    combObj = CombinationGrouperChangers.objects.all()
    for i in combObj:
        if str(i.groupName) == combinationApply:
            combDic[i.planetName] = i.planetChangedName
    print(combDic)
    context = { "combDic" : combDic}
    return JsonResponse(context, safe=False)

def saving_combiantion_points(request):
    file = ('ex.ods')
    df = pd.read_excel(file)
    df1 = df.iloc[:, 0:2]
    print(df1)
    print("CONCATENATION", "Conj")
    df1.columns = ["CONCATENATION", "Conj"]
    for index, row in df1.iterrows():
        type = "Conj"
        name = row.CONCATENATION
        points = row.Conj
        s = concatenation_points(con_type=type, con_name=name, con_points=points)
        s.save()
    df1 = df.iloc[:, 2:4]
    print(df1)
    print("CONCATENATION", "60°<")
    df1.columns = ["CONCATENATION", "Conj"]
    for index, row in df1.iterrows():
        type = "60<"
        name = row.CONCATENATION
        points = row.Conj
        s = concatenation_points(con_type=type, con_name=name, con_points=points)
        s.save()
    df1 = df.iloc[:, 4:6]
    print(df1)
    print("CONCATENATION", ">60°")
    df1.columns = ["CONCATENATION", "Conj"]
    for index, row in df1.iterrows():
        type = ">60"
        name = row.CONCATENATION
        points = row.Conj
        s = concatenation_points(con_type=type, con_name=name, con_points=points)
        s.save()
    df1 = df.iloc[:, 6:8]
    print(df1)
    print("CONCATENATION", "90<")
    df1.columns = ["CONCATENATION", "Conj"]
    for index, row in df1.iterrows():
        type = "90<"
        name = row.CONCATENATION
        points = row.Conj
        s = concatenation_points(con_type=type, con_name=name, con_points=points)
        s.save()
    df1 = df.iloc[:, 8:10]
    print(df1)
    print("CONCATENATION", ">90")
    df1.columns = ["CONCATENATION", "Conj"]
    for index, row in df1.iterrows():
        type = ">90"
        name = row.CONCATENATION
        points = row.Conj
        s = concatenation_points(con_type=type, con_name=name, con_points=points)
        s.save()
    df1 = df.iloc[:, 10:12]
    print(df1)
    print("CONCATENATION", "120<")
    df1.columns = ["CONCATENATION", "Conj"]
    for index, row in df1.iterrows():
        type = "120<"
        name = row.CONCATENATION
        points = row.Conj
        s = concatenation_points(con_type=type, con_name=name, con_points=points)
        s.save()
    df1 = df.iloc[:, 12:14]
    print(df1)
    print("CONCATENATION", ">120")
    df1.columns = ["CONCATENATION", "Conj"]
    for index, row in df1.iterrows():
        type = ">120"
        name = row.CONCATENATION
        points = row.Conj
        s = concatenation_points(con_type=type, con_name=name, con_points=points)
        s.save()
    df1 = df.iloc[:, 14:16]
    print(df1)
    print("CONCATENATION", ">150")
    df1.columns = ["CONCATENATION", "Conj"]
    for index, row in df1.iterrows():
        type = ">150"
        name = row.CONCATENATION
        points = row.Conj
        s = concatenation_points(con_type=type, con_name=name, con_points=points)
        s.save()
    df1 = df.iloc[:, 16:18]
    print(df1)
    print("CONCATENATION", "180")
    df1.columns = ["CONCATENATION", "Conj"]
    for index, row in df1.iterrows():
        type = "180"
        name = row.CONCATENATION
        points = row.Conj
        s = concatenation_points(con_type=type, con_name=name, con_points=points)
        s.save()
    return render(request, "savecompoint.html", {})

def delete_combiantion_points(request):
    data = concatenation_points.objects.all().delete()
    return render(request, "savecompoint.html", {})

def multiple5_home(request):
    categoriesName = divisionName.objects.all()
    CombGrpNames = CombinationGroupNames.objects.all()
    return render(request, "multiple/multi5Home.html", {"categoriesName": categoriesName, "CombGrpNames": CombGrpNames})

def multi5_data(request):
    if request.is_ajax():
        peopleCategory = request.GET.get('peopleCategory')
        nameLis, resultDic = p1_person_loop(peopleCategory)
        context = {
            "nameLis": nameLis,
            "resultDic": resultDic,
        }
        return JsonResponse(context, safe=False)