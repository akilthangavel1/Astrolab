from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from persontoperson.models import birthchartdb
import logging
import googlemaps
from django.forms import Form, ValidationError
from .astro_helpers import bdate_time_place_to_degs
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from match.models import Label, MapSession
from persontoperson.models import birthchartdb
import googlemaps
from match.my_scripts.match3 import match3


logger = logging.getLogger(__name__)

class RelocationMap3dInputView(LoginRequiredMixin, TemplateView):
    login_url = '/users/login/'
    template_name = 'maplatest/relocation_map_input.html'  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sessions'] = []  
        return context

 


def get_degrees(name, bdate, btime, bplace):
    
    bdate = bdate.replace('-', '.')
    def decdeg2dms(dd):
        mnt, sec = divmod(dd * 3600, 60)
        deg, mnt = divmod(mnt, 60)
        deg = abs(deg) 
        return deg, mnt
    
   
    person = birthchartdb.objects.filter(fullname=name, place_of_birth=bplace).first()

    if person and person.Su:
        context = {attr: getattr(person, attr) for attr in ['Su', 'Mo', 'Me', 'Ma', 'Ju', 'Ve', 'Sa', 'Ra', 'Ke', 'As']}
    else:
        KEY = 'AIzaSyDpksPTT2PW4ZOSlzltN0QLV4zxT6U09pA'
        api = googlemaps.Client(key=KEY)
        degs, latitude, longitude = bdate_time_place_to_degs(api, bdate, btime, bplace)
        context = {}
        for i, planet in enumerate(['Su', 'Mo', 'Me', 'Ma', 'Ju', 'Ve', 'Sa', 'Ra', 'Ke', 'As']):
            d, m = decdeg2dms(round(degs[i], 4))
            context[planet] = f"{int(d)}° {int(m)}'"
        context["latitude"] = latitude
        context["longitude"] = longitude
    return (context)


@require_POST
def maplatest_add_person(request):  
    name = request.POST.get('name', '').strip()
    bdate = request.POST.get('bdate', '').strip()
    btime = request.POST.get('btime', '').strip()
    bplace = request.POST.get('bplace', '').strip()
    gender = request.POST.get('gender', '').strip() 

    if not all([name, bdate, btime, bplace, gender]):
        return JsonResponse({'state': '0', 'error': 'All fields are required.'}, status=400)


    existing_person = birthchartdb.objects.filter(
        fullname=name,
    ).first()

    if existing_person:
        logger.error(f"Person already exists: {name}, {bdate}, {btime}, {bplace}")
        return JsonResponse({'state': '0', 'error': 'Person already exists.'})

    try:    
        degree = get_degrees(name, bdate, btime, bplace)
        person = birthchartdb(fullname=name, date_of_birth=bdate, time_of_birth=btime, place_of_birth=bplace, coordinates_lan=degree['latitude'], coordinates_lon=degree['longitude'], Su = degree['Su'], Mo = degree['Mo'], Me= degree['Me'],
        Ma= degree['Ma'],
        Ju= degree['Ju'],
        Ve= degree['Ve'],
        Sa= degree['Sa'],
        Ra= degree['Ra'],
        Ke= degree['Ke'],
        As= degree['As'])

        person.save()
        response_data = {
            'state': '1',
            'degree': degree,
            'coordinates': {
                'latitude': degree['latitude'],
                'longitude': degree['longitude']
            }
        }
        
        return JsonResponse(response_data)

    except Exception as e:
        logger.error(f"Error saving person: {e}")
        return JsonResponse({'state': '0', 'error': 'Failed to save person.'}, status=500)


# views.py
from django.http import JsonResponse
# from .models import birthchartdb

def autocomplete_names(request):
    if 'term' in request.GET:
        qs = birthchartdb.objects.filter(fullname__icontains=request.GET.get('term'))
        names = list(qs.values('fullname', 'date_of_birth', 'time_of_birth', 'place_of_birth', 'coordinates_lan', 'coordinates_lon', 'Su', 'Mo', 'Me', 'Ma', 'Ju', 'Ve', 'Sa', 'Ra', 'Ke', 'As'))
        return JsonResponse(names, safe=False)
    return JsonResponse([], safe=False)





class RelocationMap3dView(TemplateView):
    def get(self, request, **kwargs):
        all_params = request.GET
        labelName = request.GET['name']
        label_db = Label.objects.filter(**{"user": labelName})
        
        if 1 == 1:
            context = {
                "polygons": "",
                
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
                    if 1==1:
                        name = request.GET['name']
                        ttime = request.GET['birth_time']
                        ddate = request.GET['birth_date'].replace('-', '.')
                        pplace = request.GET['place_of_birth']
                        #
                        KEY = 'AIzaSyDpksPTT2PW4ZOSlzltN0QLV4zxT6U09pA'
                        api = googlemaps.Client(key=KEY)
                        person = birthchartdb.objects.filter(fullname=name, place_of_birth=pplace)[0]
                        person.Su = request.GET['symbol_su']
                        person.Mo = request.GET['symbol_mo']
                        person.Me = request.GET['symbol_me']
                        person.Ma = request.GET['symbol_ma']
                        person.Ju = request.GET['symbol_ju']
                        person.Ve = request.GET['symbol_ve']
                        person.Sa = request.GET['symbol_sa']
                        person.Ra = request.GET['symbol_ra']
                        person.Ke = request.GET['symbol_ke']
                        person.As = request.GET['symbol_as']
                        person.save()
                        #
                        degs = []
                        degs.append(request.GET['symbol_su'])
                        degs.append(request.GET['symbol_mo'])
                        degs.append(request.GET['symbol_me'])
                        degs.append(request.GET['symbol_ma'])
                        degs.append(request.GET['symbol_ju'])
                        degs.append(request.GET['symbol_ve'])
                        degs.append(request.GET['symbol_sa'])
                        degs.append(request.GET['symbol_ra'])
                        degs.append(request.GET['symbol_ke'])
                        degs.append(request.GET['symbol_as'])

                        degs = [dmstodeg(i) for i in degs]

                        place_lat_lon = api.geocode(pplace)
                        lati, long = place_lat_lon[0]['geometry']['location']['lat'], place_lat_lon[0]['geometry']['location']['lng']
                        #
                        if request.GET['latitude'] and request.GET['longitude']:
                            lati, long = request.GET['latitude'], request.GET['longitude']
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
                        #
                        planets = ['Su', 'Mo', 'Me', 'Ma', 'Ju', 'Ve', 'Sa', 'Ra', 'Ke', 'As']
                        signs = ['Ar', 'Ta', 'Ge', 'Ca', 'Le', 'Vg', 'Li', 'Sc', 'Sg', 'Cp', 'Aq', 'Pi']
                        #
                        # degs = bdate_time_place_to_degs(api, ddate, ttime, pplace)
                        # degs = match3(ddate, '2000.01.01', ttime, '12:00', pplace, 'Russia, Krasnodar')[4]
                        #
                        degs_signs = []
                        for i in range(len(degs)):
                            deg = degs[i]
                            planet = planets[i]
                            deg = deg + 60 if deg + 60 <= 360 else deg + 60 - 360
                            degs_signs.append([deg, planet])
                        #
                        polygons = """var cla = {};
                        var clo = {};
                        var planets = [""".format(lati, long)
                        #
                        for i in degs_signs:
                            polygons += '[{}, "{}"],'.format(str(i[0]), i[1])
                        polygons = polygons[:-1]
                        polygons += '];'

                        context["polygons"] = polygons
                        #context["sublines"] = sublines
                        #

                        # Code for natal charts
                        name = request.GET['name']
                        #
                        if request.GET['symbol_su'] != '':
                            degs = []
                            degs.append(request.GET['symbol_su'])
                            degs.append(request.GET['symbol_mo'])
                            degs.append(request.GET['symbol_me'])
                            degs.append(request.GET['symbol_ma'])
                            degs.append(request.GET['symbol_ju'])
                            degs.append(request.GET['symbol_ve'])
                            degs.append(request.GET['symbol_sa'])
                            degs.append(request.GET['symbol_ra'])
                            degs.append(request.GET['symbol_ke'])
                            degs.append(request.GET['symbol_as'])
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
                        # For P1 (main person)
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

                            # Layout generation
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
                        return render(request, 'maplatest/re9.html', context=context)
                    else:
                        return render(request, 'jyotish/map_add_labels.html', context=context)
        else:
            return redirect('/login')


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def ajax_save_labels_map(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            labels = data.get('labels', [])
            username = data.get('user')
            label_name = data.get('labelname')

            if not username or not label_name:
                return JsonResponse({'error': 'Missing user or labelname'}, status=400)

            label_db = Label.objects.filter(user=label_name)
            label_db.delete()  # Clear existing labels for this user

            for label_data in labels:
                try:
                    text, lat, lon = label_data.split("_____")
                    label = Label(session="1", text=text, lat=lat, lon=lon, user=label_name)
                    label.save()
                except ValueError:
                    return JsonResponse({'error': f'Invalid label format: {label_data}'}, status=400)

            return JsonResponse({'message': 'Labels saved successfully!'}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON payload'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
