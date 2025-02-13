from django.shortcuts import render
from .models import Label
import googlemaps
from urllib.parse import unquote
from .my_scripts.logic import match_all, bdate_time_place_to_degs
from .my_scripts.match3 import match3
from .models import Person, Label, MapSession, UserVideoLink
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.forms import Form, ValidationError
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.utils.html import escape
from django.http import JsonResponse

# Create your views here.
def jyotishmatch(request):
    def get(self, request, **kwargs):
        labelName = request.GET['inputName1']
        label_db = Label.objects.filter(**{"user": labelName})
        
        if request.user.is_authenticated:
            context = {
                "polygons": "",
                "user_name": request.user.username
            }

            def dmstodeg(dm):
                d = dm.split(' ')[0][:-1]
                m = dm.split(' ')[1][:-1]
                deg = float(d) + float(m) / 60
                return deg

            if request.method == 'GET':
                form = Form(request.GET)
                if form.is_valid():
                    ses = request.GET['inputSession'].split('    ')
                    if len(ses) == 3:
                        session = MapSession.objects.get(id=int(ses[2]))
                        if session:
                            labels = []
                            for i in Label.objects.filter(session=str(session.id)):
                                labels.append([i.text, i.lat, i.lon])
                            context['labels'] = labels
                            if len(labels) == 0:
                                context['already_yes'] = 'yes'
                            else:
                                context['already_yes'] = ''
                        else:
                            context['labels'] = []
                    #
                    if request.user.is_superuser:
                        name = request.GET['inputName1']
                        ttime = request.GET['time']
                        ddate = request.GET['date'].replace('-', '.')
                        pplace = request.GET['autocomplete1']
                        #
                        KEY = 'AIzaSyASsKRcBk1D1J_oWy7teTjodHQ5N1uOl1M'
                        api = googlemaps.Client(key=KEY)
                        person = Person.objects.filter(name=name, bplace=pplace)[0]
                        person.Su = request.GET['CD_Su']
                        person.Mo = request.GET['CD_Mo']
                        person.Me = request.GET['CD_Me']
                        person.Ma = request.GET['CD_Ma']
                        person.Ju = request.GET['CD_Ju']
                        person.Ve = request.GET['CD_Ve']
                        person.Sa = request.GET['CD_Sa']
                        person.Ra = request.GET['CD_Ra']
                        person.Ke = request.GET['CD_Ke']
                        person.As = request.GET['CD_As']
                        person.save()
                        #
                        degs = []
                        degs.append(request.GET['CD_Su'])
                        degs.append(request.GET['CD_Mo'])
                        degs.append(request.GET['CD_Me'])
                        degs.append(request.GET['CD_Ma'])
                        degs.append(request.GET['CD_Ju'])
                        degs.append(request.GET['CD_Ve'])
                        degs.append(request.GET['CD_Sa'])
                        degs.append(request.GET['CD_Ra'])
                        degs.append(request.GET['CD_Ke'])
                        degs.append(request.GET['CD_As'])

                        degs = [dmstodeg(i) for i in degs]

                        place_lat_lon = api.geocode(pplace)
                        lati, long = place_lat_lon[0]['geometry']['location']['lat'], place_lat_lon[0]['geometry']['location']['lng']
                        #
                        if request.GET['reloc_lat'] and request.GET['reloc_lon']:
                            lati, long = request.GET['reloc_lat'], request.GET['reloc_lon']
                            if '°' in lati:
                                if 'n' in lati.lower():
                                    lati = float(lati.split('°')[0])
                                else:
                                    lati = -float(lati.split('°')[0])
                            else:
                                lati = float(lati)
                            if '°' in long:
                                if 'e' in long.lower():
                                    long = float(long.split('°')[0])
                                else:
                                    long = -float(long.split('°')[0])
                            else:
                                long = float(long)
                        planets = ['Su', 'Mo', 'Me', 'Ma', 'Ju', 'Ve', 'Sa', 'Ra', 'Ke', 'As']
                        signs = ['Ar', 'Ta', 'Ge', 'Ca', 'Le', 'Vg', 'Li', 'Sc', 'Sg', 'Cp', 'Aq', 'Pi']
                        degs_signs = []
                        for i in range(len(degs)):
                            deg = degs[i]
                            planet = planets[i]
                            deg = deg + 60 if deg + 60 <= 360 else deg + 60 - 360
                            degs_signs.append([deg, planet])
                        polygons = """var cla = {};
                        var clo = {};
                        var planets = [""".format(lati, long)
                        for i in degs_signs:
                            polygons += '[{}, "{}"],'.format(str(i[0]), i[1])
                        polygons = polygons[:-1]
                        polygons += '];'
                        context["polygons"] = polygons
                        name = request.GET['inputName1']
                        if request.GET['CD_Su'] != '':
                            degs = []
                            degs.append(request.GET['CD_Su'])
                            degs.append(request.GET['CD_Mo'])
                            degs.append(request.GET['CD_Me'])
                            degs.append(request.GET['CD_Ma'])
                            degs.append(request.GET['CD_Ju'])
                            degs.append(request.GET['CD_Ve'])
                            degs.append(request.GET['CD_Sa'])
                            degs.append(request.GET['CD_Ra'])
                            degs.append(request.GET['CD_Ke'])
                            degs.append(request.GET['CD_As'])
                            degs = [dmstodeg(i) for i in degs]
                            result = match3(ddate, ddate, ttime, ttime, pplace, pplace, degs)
                        else:
                            result = match3(ddate, ddate, ttime, ttime, pplace, pplace)
                        report_btns, report_txts = '', ''
                        p_asp_p, p_asp_h = '', ''
                        signs = ['Pi', 'Ar', 'Ta', 'Ge', 'Aq', 'Ca', 'Cp', 'Le', 'Sg', 'Sc', 'Li', 'Vg']
                            #
                        def decdeg2dms(dd):
                            mnt, sec = divmod(dd*3600,60)
                            deg, mnt = divmod(mnt,60)
                            if deg < 0:
                                deg = -deg
                            return deg, mnt

                        sign_nums = {['Ar', 'Ta', 'Ge', 'Ca', 'Le', 'Vg', 'Li', 'Sc', 'Sg', 'Cp', 'Aq', 'Pi'][i]: i+1 for i in range(12)}
                        c = []
                        t4, t5 = result[3][0], result[3][1]
                        t4vk = {v: k for k,v in t4.items()}
                        t5vk = {v: [i for i in t5 if t5[i] == v] for v in list(set(list(t5.values())))}
                        degs = result[4]
                        degs = {['Su', 'Mo', 'Me', 'Ma', 'Ju', 'Ve', 'Sa', 'Ra', 'Ke', 'As'][i]: degs[i] for i in range(10)}

                        for i in range(12):
                            sign = signs[i]
                            house = t4[sign]
                            sign_num = sign_nums[sign]
                            s = ['', '', '', '']
                            try:
                                planets = t5vk[house]
                                for j in range(4):
                                    try:
                                        d = degs[planets[j]] - (sign_num - 1) * 30
                                        deg, min = decdeg2dms(d)
                                        s[j] = planets[j] + ' ' + str(int(deg)) + '°' + str(int(min)) + "'"
                                    except:
                                        pass
                            except:
                                pass
                            c.append("""
                                    <div class="d-flex p-1 justify-content-center mr-2" style="height: 38%">
                                        <div class="col mt-auto mb-auto" style="width: 25px">{}</div>
                                        <div class="col mt-auto mb-auto" style="width: 25px">{}</div>
                                    </div>
                                    <div class="d-flex p-1 justify-content-center mr-2" style="height: 38%">
                                        <div class="col" style="width: 25px">{}</div>
                                        <div class="col" style="width: 25px">{}</div>
                                    </div>
                                    <b class="bg-warning border border-dark rounded ml-1 pl-1 pr-1">{}</b>
                            """.format(s[0], s[1], s[2], s[3], str(house) + ' ' + sign))

                        report_txts += """
                                <div class="row">
                                    <div class="container-fluid">
                                        <div class="row">
                                            <div class="col ml-2 pt-2" style="font-size: 9pt">
                                                <div class="row">
                                                    <div class="bg-white border border-dark border-right-0 border-bottom-0" style="width: 110px; height: 110px; border-top-left-radius: 10px;">{}</div>
                                                    <div class="bg-white border border-dark border-right-0" style="width: 110px; height: 110px">{}</div>
                                                    <div class="bg-white border border-dark border-right-0" style="width: 110px; height: 110px">{}</div>
                                                    <div class="bg-white border border-dark border-bottom-0" style="width: 110px; height: 110px; border-top-right-radius: 10px;">{}</div>
                                                </div>
                                                <div class="row">
                                                    <div class="bg-white border border-dark border-bottom-0" style="width: 110px; height: 110px">{}</div>
                                                    <div class="bg-white" style="width: 110px; height: 110px"></div>
                                                    <div class="bg-white" style="width: 110px; height: 110px"></div>
                                                    <div class="bg-white border border-dark border-bottom-0" style="width: 110px; height: 110px">{}</div>
                                                </div>
                                                <div class="row">
                                                    <div class="bg-white border border-dark border-bottom-0" style="width: 110px; height: 110px">{}</div>
                                                    <div class="bg-white" style="width: 110px; height: 110px"></div>
                                                    <div class="bg-white" style="width: 110px; height: 110px"></div>
                                                    <div class="bg-white border border-dark border-bottom-0" style="width: 110px; height: 110px">{}</div>
                                                </div>
                                                <div class="row">
                                                    <div class="bg-white border border-dark border-right-0" style="width: 110px; height: 110px; border-bottom-left-radius: 10px;">{}</div>
                                                    <div class="bg-white border border-dark border-right-0" style="width: 110px; height: 110px">{}</div>
                                                    <div class="bg-white border border-dark border-right-0" style="width: 110px; height: 110px">{}</div>
                                                    <div class="bg-white border border-dark" style="width: 110px; height: 110px; border-bottom-right-radius: 10px;">{}</div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                        """.format(c[0], c[1], c[2], c[3], c[4], c[5], c[6], c[7], c[8], c[9], c[10], c[11])
                        #
                        context['label_db'] = label_db
                        context["report_txts"] = report_txts
                        context["labelName"] = labelName
                        #
                        return render(request, 'relocation_map3d.html', context=context)
                    else:
                        return render(request, 'map_add_labels.html', context=context)
        else:
            return redirect('relocation_map3d.html')
    return render(request, "jyotish/jyotishmatch.html", {})



def ajax_add_person(request):  
    name = request.GET.get('name', None)
    bdate = request.GET.get('bdate', None)
    btime = request.GET.get('btime', None)
    bplace = request.GET.get('bplace', None)
    gender = request.GET.get('gender', None)
    print(gender)
    data = {
        'state': '1'
    }

    if Person.objects.filter(name=name).count() > 0:
        if Person.objects.filter(name=name, bdate=bdate, btime=btime, bplace=bplace, gender=gender).count() > 0:
            data['state'] = ''

    if data['state'] == '1':
        person = Person()
        person.name = name
        person.bdate = bdate
        person.btime = btime
        person.bplace = bplace
        person.gender = gender
        person.save()
    return JsonResponse(data)

# AJAX based functions
def ajax_validate_person_name(request):  # finds persons with <name> like provided (for autocomplete of names)

    name = request.GET.get('name', None)
    persons = ''
    for p in Person.objects.filter(name__contains=name)[:80]:
        persons += '<option>{} | {} | {} | {} | {}</p>'.format(p.name, p.bdate, p.btime, p.bplace, p.gender)
    data = {
        'persons': persons
    }
    print(data)
    return JsonResponse(data)

def ajax_validate_person_name_admin(request):
    data = {
        'sessions': ''
    }

    name = request.GET.get('name', None)
    q = Person.objects.get(name=name)
    if q:
        for i in MapSession.objects.filter(user=q.user):
            d = str(i.date).split('.')[0] + str(i.date)[-5:]
            data['sessions'] += '<option value="{}    {}    {}"></option>'.format(i.name, d, i.id)
    return JsonResponse(data)