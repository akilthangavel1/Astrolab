from django.http import JsonResponse
from django.shortcuts import render
from .persononecharts import person_one_chart_main, add_p1form
from .astrogeneration import astrogen


# Create your views here.
def display_one(request):
    
    return render(request, "displayers/displayone.html", {})

def display_two(request):
    main_dic = person_one_chart_main()
    return render(request, "displayers/ir_home.html", main_dic)
    
def display_three(request):
    main_dic = add_p1form()
    return render(request, "displayers/displaythree.html", main_dic)


def display_houses(request):
    return render(request, "displayers/displayHouses.html", {})


def astro_tables(request):
    if request.is_ajax():
        personName = request.GET.get('personname')
        resultDic = astrogen(personName)
        context = {
            "resultDic": resultDic,
        }
        return JsonResponse(context, safe=False)