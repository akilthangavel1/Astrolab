from django.http.response import JsonResponse
from controlpanel.exaspect import interaccion
from django.http.response import JsonResponse
from datetime import date, datetime, timedelta
from .models import MultiDateLisDB, modelNames, divisionName, PlanetGroupNames, PlanetGroupers
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

def mnatalOperation(categoryName, personTwoBirthPlace, personTwoBirthDate, personTwoBirthTime):
    category_obj = divisionName.objects.get(divName=categoryName)
    listOfModelNames = modelNames.objects.filter(modelcategory = category_obj)
    interaccionDf = pd.DataFrame() 
    personTwoBirthDate = personTwoBirthDate.replace("-", ".")
    for i in listOfModelNames:
        datetime_obj = i.birthDateTime
        datetime_obj = datetime_obj.replace("T", " ")
        personOneBirthDate = (datetime.strptime(datetime_obj, '%Y-%m-%d %H:%M').date()).strftime('%d.%m.%Y')
        personOneBirthTime = (datetime.strptime(datetime_obj, '%Y-%m-%d %H:%M').time()).strftime('%H:%M')
        personOneDegrees = onematch(personOneBirthDate, personOneBirthTime, i.modelLocation)
        personTwoDegrees = onematch(personTwoBirthDate, personTwoBirthTime, personTwoBirthPlace)
        interaccionResult = all_calculation_multiple_two(personOneDegrees[0], personOneDegrees[1], personOneDegrees[2], personOneDegrees[3], personOneDegrees[4], personOneDegrees[5], personOneDegrees[6], personOneDegrees[7], personOneDegrees[8], personOneDegrees[9], personTwoDegrees[0], personTwoDegrees[1], personTwoDegrees[2], personTwoDegrees[3], personTwoDegrees[4], personTwoDegrees[5], personTwoDegrees[6], personTwoDegrees[7], personTwoDegrees[8], personTwoDegrees[9])
        interaccionResult = interaccionResult.rename(columns={"puntaje": i.modelFullName})  
        interaccionResult.set_index("INTERACCION", inplace=True)
        interaccionDf = pd.concat([interaccionDf, interaccionResult], axis=1)
    interaccionDf = interaccionDf.reset_index()
    interaccionDf['INTERACCION'] = interaccionDf['INTERACCION'].apply(remove_extra_quotes)
    interaccionDf.set_index("INTERACCION", inplace=True)
    return (interaccionDf.columns.tolist()), (interaccionDf.T.to_dict('list'))

def add_colorcode():
    pass

def m2_main(request):
    if (request.GET.get('p2place')):
        categoryName = (request.GET.get('catselect'))
        # glist = (request.GET.get('glist'))
        birthPlace = (request.GET.get('p2place'))
        birthDate = (request.GET.get('secdate'))
        birthTime = (request.GET.get('sectime'))
        # gcObj = PlanetGroupNames.objects.get(groupName=glist)
        # gLisDic = PlanetGroupers.objects.get(groupName = gcObj)
        date_re = mnatalOperation(categoryName, birthPlace, str(birthDate), str(birthTime))
        return date_re


def result_category_graph(request):
    df_dic = m2_main(request)
    context = {
                "date_lis" :df_dic[0],
                'data': df_dic[1],
            }
    return JsonResponse(context, safe=False)   