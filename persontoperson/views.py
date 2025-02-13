from django.shortcuts import render, redirect
from .p1conp2 import p1vsp2_main
from .personone import p1main
from .p1xp2exact import p1xp2ex_main
from .ax_report import graph_main
from .integrated_report import integrated_report_main
from .irpdf import integrated_report_pdf_main
from django.http import JsonResponse
from .natalchart import natal_main
from .models import birthchartdb, PersonDegree, GlobalDegree
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .singledegree import onematch
from django.contrib.auth.decorators import login_required
from .excelex import readex


def globalpersondb():
    degree_dic = {"p1_su_degree": 0, "p1_mo_degree": 0, "p1_me_degree": 0, "p1_ma_degree": 0, "p1_ju_degree": 0,
                  "p1_ve_degree": 0, "p1_sa_degree": 0, "p1_ra_degree": 0, "p1_ke_degree": 0, "p1_as_degree": 0,
                  "p2_su_degree": 0, "p2_mo_degree": 0, "p2_me_degree": 0, "p2_ma_degree": 0, "p2_ju_degree": 0,
                  "p2_ve_degree": 0, "p2_sa_degree": 0, "p2_ra_degree": 0, "p2_ke_degree": 0, "p2_as_degree": 0,
                  }
    gplist = GlobalDegree.objects.filter(**{"id": 1})
    for i in gplist:
        degree_dic["p1_su_degree"] = i.suDegree
        degree_dic["p1_mo_degree"] = i.moDegree
        degree_dic["p1_me_degree"] = i.meDegree
        degree_dic["p1_ma_degree"] = i.maDegree
        degree_dic["p1_ju_degree"] = i.juDegree
        degree_dic["p1_ve_degree"] = i.veDegree
        degree_dic["p1_sa_degree"] = i.saDegree
        degree_dic["p1_ra_degree"] = i.raDegree
        degree_dic["p1_ke_degree"] = i.keDegree
        degree_dic["p1_as_degree"] = i.asDegree
    gplist = GlobalDegree.objects.filter(**{"id": 2})
    for i in gplist:
        degree_dic["p2_su_degree"] = i.suDegree
        degree_dic["p2_mo_degree"] = i.moDegree
        degree_dic["p2_me_degree"] = i.meDegree
        degree_dic["p2_ma_degree"] = i.maDegree
        degree_dic["p2_ju_degree"] = i.juDegree
        degree_dic["p2_ve_degree"] = i.veDegree
        degree_dic["p2_sa_degree"] = i.saDegree
        degree_dic["p2_ra_degree"] = i.raDegree
        degree_dic["p2_ke_degree"] = i.keDegree
        degree_dic["p2_as_degree"] = i.asDegree
    return degree_dic



@login_required(login_url='/users/login/')  
def p2pform(request):
    degree_dic = globalpersondb()
    main_dic = p1vsp2_main(degree_dic["p1_su_degree"], degree_dic["p1_mo_degree"], degree_dic["p1_me_degree"], degree_dic["p1_ma_degree"], degree_dic["p1_ju_degree"], degree_dic["p1_ve_degree"], degree_dic["p1_sa_degree"], degree_dic["p1_ra_degree"], degree_dic["p1_ke_degree"], degree_dic["p1_as_degree"], degree_dic["p2_su_degree"], degree_dic["p2_mo_degree"], degree_dic["p2_me_degree"], degree_dic["p2_ma_degree"], degree_dic["p2_ju_degree"], degree_dic["p2_ve_degree"], degree_dic["p2_sa_degree"], degree_dic["p2_ra_degree"], degree_dic["p2_ke_degree"], degree_dic["p2_as_degree"])
    main_dic.update(degree_dic)
    return render(request, "p2p/p2phome.html", main_dic)
 
    
@login_required(login_url='/users/login/')  
def p1form(request):
    degree_dic = globalpersondb()
    main_dic = p1main(degree_dic["p1_su_degree"], degree_dic["p1_mo_degree"], degree_dic["p1_me_degree"], degree_dic["p1_ma_degree"], degree_dic["p1_ju_degree"], degree_dic["p1_ve_degree"], degree_dic["p1_sa_degree"], degree_dic["p1_ra_degree"], degree_dic["p1_ke_degree"], degree_dic["p1_as_degree"])
    return render(request, "p2p/p1home.html", main_dic)


@login_required(login_url='/users/login/')  
def p1xp2exactform(request):
    degree_dic = globalpersondb()
    main_dic = p1xp2ex_main(degree_dic["p1_su_degree"], degree_dic["p1_mo_degree"], degree_dic["p1_me_degree"], degree_dic["p1_ma_degree"], degree_dic["p1_ju_degree"], degree_dic["p1_ve_degree"], degree_dic["p1_sa_degree"], degree_dic["p1_ra_degree"], degree_dic["p1_ke_degree"], degree_dic["p1_as_degree"], degree_dic["p2_su_degree"], degree_dic["p2_mo_degree"], degree_dic["p2_me_degree"], degree_dic["p2_ma_degree"], degree_dic["p2_ju_degree"], degree_dic["p2_ve_degree"], degree_dic["p2_sa_degree"], degree_dic["p2_ra_degree"], degree_dic["p2_ke_degree"], degree_dic["p2_as_degree"])
    return render(request, "p2p/p1xp2exacthome.html", main_dic)


@login_required(login_url='/users/login/')  
def ax_report_form(request):
    degree_dic = globalpersondb()
    order_planets_df = [{"planet": "SUN"}, {"planet": "MOON"},{"planet": "MECURY"}, {"planet": "MARTE"}, {"planet": "JUPITER"},{"planet": "VENUS"}, {"planet": "SATURN"}, {"planet": "RAHU"}, {"planet": "KETU"}]
    order_deg_df = [{"deg": "All"}, {"deg": "Conj"}, {"deg": "180"}, {"deg": "120<"}, {"deg": ">120"}, {"deg": "90<"}, {"deg": ">90"}, {"deg": "60<"}, {"deg": ">60"}]
    main_dic= {"order_planets":order_planets_df, "order_deg": order_deg_df}
    if request.method == "POST":
        graph_planets = request.POST['g_planet']
        graph_degree = request.POST['g_degree']
        main_dic = graph_main(graph_planets, graph_degree, degree_dic["p1_su_degree"], degree_dic["p1_mo_degree"], degree_dic["p1_me_degree"], degree_dic["p1_ma_degree"], degree_dic["p1_ju_degree"], degree_dic["p1_ve_degree"], degree_dic["p1_sa_degree"], degree_dic["p1_ra_degree"], degree_dic["p1_ke_degree"], degree_dic["p1_as_degree"], degree_dic["p2_su_degree"], degree_dic["p2_mo_degree"], degree_dic["p2_me_degree"], degree_dic["p2_ma_degree"], degree_dic["p2_ju_degree"], degree_dic["p2_ve_degree"], degree_dic["p2_sa_degree"], degree_dic["p2_ra_degree"], degree_dic["p2_ke_degree"], degree_dic["p2_as_degree"])
        return render(request, "p2p/axhome.html", main_dic)
    return render(request, "p2p/axhome.html", main_dic)


@login_required(login_url='/users/login/')  
def ir_form(request):
    degree_dic = globalpersondb()
    # if you want output
    main_dic = integrated_report_main(degree_dic["p1_su_degree"], degree_dic["p1_mo_degree"], degree_dic["p1_me_degree"], degree_dic["p1_ma_degree"], degree_dic["p1_ju_degree"], degree_dic["p1_ve_degree"], degree_dic["p1_sa_degree"], degree_dic["p1_ra_degree"], degree_dic["p1_ke_degree"], degree_dic["p1_as_degree"], degree_dic["p2_su_degree"], degree_dic["p2_mo_degree"], degree_dic["p2_me_degree"], degree_dic["p2_ma_degree"], degree_dic["p2_ju_degree"], degree_dic["p2_ve_degree"], degree_dic["p2_sa_degree"], degree_dic["p2_ra_degree"], degree_dic["p2_ke_degree"], degree_dic["p2_as_degree"])
    return render(request, "p2p/ir_home.html", main_dic)


def donation_receipt(request):
    return render(request, 'p2p/pdf1.html', {})


def natalform(request):
    if "term" in request.GET:
        qs = birthchartdb.objects.filter(fullname__istartswith= request.GET.get("term"))
        local_source = [{"id": 1, "value": "c++"}, {id: 2, "value": "cobal"}, {id: 3, "value": "cibil"}
                        ]
        return JsonResponse(local_source)
    if request.method == "POST":
        full_name = request.POST["fname"]
        birthdaydate = request.POST["birthdaydate"]
        birthdaytime = request.POST["birthdaytime"]
        location = request.POST["location"]
        loc_lat = request.POST["loc_lat"]
        loc_long = request.POST["loc_long"]
        p1full_name = request.POST["p1fname"]
        p1birthdaydate = request.POST["p1bd"]
        p1birthdaytime = request.POST["p1bt"]
        p1location = request.POST["p1search_input"]
        p1loc_lat = request.POST["p1loc_lat"]
        p1loc_long = request.POST["p1loc_long"]
        natal_main(full_name, birthdaydate, birthdaytime, location, loc_lat, loc_long, p1full_name, p1birthdaydate, p1birthdaytime, p1location, p1loc_lat, p1loc_long)
        return render(request, "p2p/nataldegrees.html", {})
    return render(request, "p2p/natalhome.html",{})


def maps_home(request):
    if "fname" in request.POST:
        fname = request.POST["fname"]
        plocation = request.POST["p1location"]
        plat = request.POST["p1lat"]
        plon = request.POST["p1lon"]
        pdate = request.POST["p1date"]
        ptime = request.POST["p1time"]
        p1su = request.POST["p1su"]
        p1mo = request.POST["p1mo"]
        p1me = request.POST["p1me"]
        p1ma = request.POST["p1ma"]
        p1ju = request.POST["p1ju"]
        p1ve = request.POST["p1ve"]
        p1sa = request.POST["p1sa"]
        p1ra = request.POST["p1ra"]
        p1ke = request.POST["p1ke"]
        p1as = request.POST["p1as"]
        gp = GlobalDegree(id= 1, suDegree = p1su, moDegree = p1mo, meDegree = p1me, maDegree = p1ma, juDegree = p1ju, veDegree = p1ve, saDegree = p1sa, raDegree = p1ra, keDegree = p1ke, asDegree = p1as)
        gp.save()
        pdlist = PersonDegree.objects.filter(**{"personName": fname})
        if pdlist:
            for i in pdlist:
                s = PersonDegree(id = i.id, personName = i.personName, suDegree = p1su, moDegree = p1mo, meDegree = p1me, maDegree = p1ma,
                                 juDegree = p1ju, veDegree =p1ve ,saDegree = p1sa ,raDegree = p1ra,keDegree = p1ke, asDegree =p1as)

                s.save()
        else:
            s = PersonDegree(personName = fname, suDegree = p1su, moDegree = p1mo, meDegree = p1me, maDegree = p1ma,
                             juDegree = p1ju, veDegree =p1ve ,saDegree = p1sa ,raDegree = p1ra,keDegree = p1ke, asDegree =p1as)
            s.save()
        bdlist = birthchartdb.objects.filter(**{"fullname": fname})
        if bdlist:
            for i in bdlist:
                s = birthchartdb(id=i.id, fullname=i.fullname, date_of_birth=pdate, time_of_birth=ptime,
                                 place_of_birth=plocation,
                                 coordinates_lan=plat, coordinates_lon=plon, time_zone=0, timeZoneId=0,
                                 timeZoneName=0)
                s.save()
        else:
            s = birthchartdb(fullname=fname, date_of_birth=pdate, time_of_birth=ptime, place_of_birth=plocation,
                             coordinates_lan=plat, coordinates_lon=plon, time_zone= 0, timeZoneId= 0,
                             timeZoneName= 0)
            s.save()
    return render(request, "p2p/maphome.html", {})



def maps_home1(request):
    global degree_dic
    if "fname" in request.POST:
        fname = request.POST["fname"]
        plocation = request.POST["p1location"]
        plat = request.POST["p1lat"]
        plon = request.POST["p1lon"]
        pdate = request.POST["p1date"]
        ptime = request.POST["p1time"]
        p1su = request.POST["p1su"]
        p1mo = request.POST["p1mo"]
        p1me = request.POST["p1me"]
        p1ma = request.POST["p1ma"]
        p1ju = request.POST["p1ju"]
        p1ve = request.POST["p1ve"]
        p1sa = request.POST["p1sa"]
        p1ra = request.POST["p1ra"]
        p1ke = request.POST["p1ke"]
        p1as = request.POST["p1as"]
        gp = GlobalDegree(id=2, suDegree=p1su, moDegree=p1mo, meDegree=p1me, maDegree=p1ma, juDegree=p1ju,
                          veDegree=p1ve, saDegree=p1sa, raDegree=p1ra, keDegree=p1ke, asDegree=p1as)
        gp.save()
        pdlist = PersonDegree.objects.filter(**{"personName": fname})
        if pdlist:
            for i in pdlist:
                s = PersonDegree(id = i.id, personName = i.personName, suDegree = p1su, moDegree = p1mo, meDegree = p1me, maDegree = p1ma,
                                 juDegree = p1ju, veDegree =p1ve ,saDegree = p1sa ,raDegree = p1ra,keDegree = p1ke, asDegree =p1as)

                s.save()
        else:
            s = PersonDegree(personName = fname, suDegree = p1su, moDegree = p1mo, meDegree = p1me, maDegree = p1ma,
                             juDegree = p1ju, veDegree =p1ve ,saDegree = p1sa ,raDegree = p1ra,keDegree = p1ke, asDegree =p1as)

            s.save()
        bdlist = birthchartdb.objects.filter(**{"fullname": fname})
        if bdlist:
            for i in bdlist:
                s = birthchartdb(id=i.id, fullname=i.fullname, date_of_birth=pdate, time_of_birth=ptime,
                                 place_of_birth=plocation,
                                 coordinates_lan=plat, coordinates_lon=plon, time_zone=0, timeZoneId=0,
                                 timeZoneName=0)
                s.save()
        else:
            s = birthchartdb(fullname=fname, date_of_birth=pdate, time_of_birth=ptime, place_of_birth=plocation,
                             coordinates_lan=plat, coordinates_lon=plon, time_zone= 0, timeZoneId= 0,
                             timeZoneName= 0)
            s.save()
    return render(request, "p2p/maphome.html", {})


def home_degree(request):
    global degree_dic
    if "pfname" in request.GET:
        fname = request.GET["pfname"]
        qs = PersonDegree.objects.filter(**{"personName": fname})
        if qs:
            data = []
            for i in qs:
                data.append(
                    {"sudegree": i.suDegree, "modegree": i.moDegree, "medegree": i.meDegree,
                     "madegree": i.maDegree,
                     "judegree": i.juDegree, "vedegree": i.veDegree, "sadegree": i.saDegree,
                     "radegree": i.raDegree,
                     "kedegree": i.keDegree, "asdegree": i.asDegree })
                gp = GlobalDegree(id=1, suDegree=data[0]["sudegree"], moDegree=data[0]["modegree"], meDegree=data[0]["medegree"],
                                  maDegree=data[0]["madegree"], juDegree= data[0]["judegree"], veDegree=data[0]["vedegree"],
                                  saDegree=data[0]["sadegree"], raDegree=data[0]["radegree"], keDegree=data[0]["kedegree"], asDegree=data[0]["asdegree"])
                gp.save()
            return JsonResponse(data, safe=False)
        else:
            pfname = request.GET["pfname"]
            plocation = request.GET["plocation"]
            plat = request.GET["plat"]
            plon = request.GET["plon"]
            pdate = request.GET["pdate"]
            ptime = request.GET["ptime"]
            p1datelist = []
            p1date = pdate.split('-')
            p1datelist.append(p1date[2])
            p1datelist.append(p1date[1])
            p1datelist.append(p1date[0])
            p1date = '.'.join(p1datelist)
            degree_result = onematch(p1date, ptime, plocation)
            data = []
            data.append(
                {"sudegree": degree_result[0], "modegree": degree_result[1], "medegree": degree_result[2], "madegree": degree_result[3],
                 "judegree": degree_result[4], "vedegree": degree_result[5], "sadegree": degree_result[6], "radegree": degree_result[7],
                 "kedegree": degree_result[8], "asdegree": degree_result[9],})
            gp = GlobalDegree(id=1, suDegree=data[0]["sudegree"], moDegree=data[0]["modegree"],
                              meDegree=data[0]["medegree"],
                              maDegree=data[0]["madegree"], juDegree=data[0]["judegree"], veDegree=data[0]["vedegree"],
                              saDegree=data[0]["sadegree"], raDegree=data[0]["radegree"], keDegree=data[0]["kedegree"],
                              asDegree=data[0]["asdegree"])
            gp.save()
            return JsonResponse(data, safe=False)

    return render(request, "p2p/maphome.html", {})


def home_degree1(request):
    global degree_dic
    if "pfname" in request.GET:
        fname = request.GET["pfname"]
        qs = PersonDegree.objects.filter(**{"personName": fname})
        if qs:
            data = []
            for i in qs:
                data.append(
                    {"sudegree": i.suDegree, "modegree": i.moDegree, "medegree": i.meDegree,
                     "madegree": i.maDegree,
                     "judegree": i.juDegree, "vedegree": i.veDegree, "sadegree": i.saDegree,
                     "radegree": i.raDegree,
                     "kedegree": i.keDegree, "asdegree": i.asDegree, })
                gp = GlobalDegree(id=2, suDegree=data[0]["sudegree"], moDegree=data[0]["modegree"],
                                  meDegree=data[0]["medegree"],
                                  maDegree=data[0]["madegree"], juDegree=data[0]["judegree"],
                                  veDegree=data[0]["vedegree"],
                                  saDegree=data[0]["sadegree"], raDegree=data[0]["radegree"],
                                  keDegree=data[0]["kedegree"], asDegree=data[0]["asdegree"])
                gp.save()

            return JsonResponse(data, safe=False)
        else:
            pfname = request.GET["pfname"]
            plocation = request.GET["plocation"]
            plat = request.GET["plat"]
            plon = request.GET["plon"]
            pdate = request.GET["pdate"]
            ptime = request.GET["ptime"]
            p1datelist = []
            p1date = pdate.split('-')
            p1datelist.append(p1date[2])
            p1datelist.append(p1date[1])
            p1datelist.append(p1date[0])
            p1date = '.'.join(p1datelist)
            degree_result = onematch(p1date, ptime, plocation)
            data = []
            data.append(
                {"sudegree": degree_result[0], "modegree": degree_result[1], "medegree": degree_result[2], "madegree": degree_result[3],
                 "judegree": degree_result[4], "vedegree": degree_result[5], "sadegree": degree_result[6], "radegree": degree_result[7],
                 "kedegree": degree_result[8], "asdegree": degree_result[9]})
            gp = GlobalDegree(id=2, suDegree=data[0]["sudegree"], moDegree=data[0]["modegree"],
                              meDegree=data[0]["medegree"],
                              maDegree=data[0]["madegree"], juDegree=data[0]["judegree"], veDegree=data[0]["vedegree"],
                              saDegree=data[0]["sadegree"], raDegree=data[0]["radegree"], keDegree=data[0]["kedegree"],
                              asDegree=data[0]["asdegree"])
            gp.save()
            return JsonResponse(data, safe=False)

    return render(request, "p2p/maphome.html", {})


def nchartlink(request):
    if "term" in request.GET and len(request.GET.get("term")) > 3:
        qs = birthchartdb.objects.filter(fullname__istartswith=request.GET.get("term"))
        data = []
        for i in qs:
            data.append({"value": i.fullname, "date_of_birth": str(i.date_of_birth), "time_of_birth": str(i.time_of_birth), "place_of_birth": i.place_of_birth, "coordinates_lan": i.coordinates_lan, "coordinates_lon": i.coordinates_lon, "time_zone": i.time_zone})
        return JsonResponse(data, safe=False)

    else:
        local_source = []
        return JsonResponse(local_source, safe=False)


@login_required(login_url='/users/login/')  
def impeople(request):
    if request.method == "GET":
        pass
    if request.method =="POST":
        fname = request.POST["fname"]
        users = birthchartdb.objects.filter(fullname=fname)
        return render(request, "p2p/impeoplehome.html", {'users':users })
    user_list = birthchartdb.objects.all().order_by('id')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request,  "p2p/impeoplehome.html", {'users': users})


def impeopleedit(request, id):
    imPeopleData = birthchartdb.objects.get(id=id)
    if request.method == "POST":
        id = request.POST['id']
        fname = request.POST["fname"]
        dob = request.POST["birthdaydate"]
        tob = request.POST["birthdaytime"]
        pob = request.POST["location"]
        clan = request.POST["loc_lat"]
        clon = request.POST["loc_long"]
        tzid = request.POST["tzid"]
        tzname = request.POST["tzname"]
        tztime = request.POST["tztime"]
        s = birthchartdb(id = id,fullname=fname, date_of_birth=dob, time_of_birth=tob, place_of_birth=pob, coordinates_lan=clan,
                         coordinates_lon=clon, time_zone=tzid, timeZoneId= tzname, timeZoneName= tztime)
        s.save()
        return redirect('/impeoples')
    return render(request,'p2p/impersonedit.html', {'imPeopleData':imPeopleData})



def destroy(request, id):
    imPeopleData = birthchartdb.objects.get(id=id)
    imPeopleData.delete()
    return redirect('/impeoples')

@login_required(login_url='/users/login/')  
def home_main(request):
    global degree_dic
    if "term" in request.GET and len(request.GET.get("term")) > 3:
        qs = birthchartdb.objects.filter(fullname__istartswith= request.GET.get("term"))
        local_source = [{"id": 1, "value": "c++"}, {id: 2, "value": "cobal"}, {id: 3, "value": "cibil"}
                        ]
        return JsonResponse(local_source)
    return render(request, "p2p/home.html", {})

