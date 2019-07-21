from django import forms
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from saferdb.forms import HomeForm, QueryForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.forms.models import model_to_dict
from django.views import generic
from django.views.generic import TemplateView
from .models import Question, Query, CaliIns_FK, Dot_Contacts
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import  logging
import csv
from django.core.management.base import BaseCommand
import datetime

from django.db.models import Q
import operator
from functools import reduce
from itertools import chain


def export_csv2(q):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'
    # print("$"*50)
    writer = csv.writer(response)
    writer.writerow([
    'DOT Number',
    'Legal Name','Address','Phone','Entity Type','Units','Drivers',
    'For Hire', 'Exempt For Hire', 'Private Property', 'Priv Pass', 'Priv Pass Non',
    'Migrant', 'US Mail', 'Fed Gov', 'State Gov', 'Local Gov', 'Indian Nation', 'Interstate',
    'Intrastate Only HM', 'Intrastate NonHM', 'General Freight', 'Household Goods',
    'Metal sheets coils rolls', 'Motor Vehicles', 'DriveTow away',
    'Logs Poles Beams Lumber', 'Building Materials', 'Mobile Homes',
    'Machinery Large Objects', 'Fresh Produce', 'LiquidsGases', 'Intermodal Cont',
    'Passengers', 'Oilfield Equipment', 'Livestock', 'Grain Feed Hay', 'CoalCoke',
    'Meat', 'GarbageRefuse', 'Us Mail', 'Chemicals', 'Commodities Dry Bulk',
    'Refrigerated Food', 'Beverages', 'Paper Products', 'Utilities', 'AgriculturalFarm Supplies',
    'Construction', 'Water Well',

    # "tb_optimized",

    'Fax', 'Email', 'Insurance', 'Date'])

    qlist = q.values_list(
    'DOT_Number', 'Legal_Name', 'Physical_adress', 'Phone', 'Entity_Type', 'Units', 'Drivers',
    'Auth_For_Hire', 'Exempt_For_Hire', 'Private_Property', 'Priv_Pass_Business',
    'Priv_Pass_Non_Business', 'Migrant', 'US_Mail', 'Fed_Gov', 'State_Gov', 'Local_Gov',
    'Indian_Nation', 'Interstate', 'Intrastate_Only_HM', 'Intrastate_NonHM', 'General_Freight',
    'Household_Goods', 'Metal_sheets_coils_rolls', 'Motor_Vehicles', 'DriveTow_away', 'Logs_Poles_Beams_Lumber',
    'Building_Materials', 'Mobile_Homes', 'Machinery_Large_Objects', 'Fresh_Produce',
    'LiquidsGases', 'Intermodal_Cont', 'Passengers', 'Oilfield_Equipment', 'Livestock',
    'Grain_Feed_Hay', 'CoalCoke', 'Meat', 'GarbageRefuse', 'US_Mail', 'Chemicals', 'Commodities_Dry_Bulk',
    'Refrigerated_Food', 'Beverages', 'Paper_Products', 'Utilities', 'AgriculturalFarm_Supplies',
    'Construction', 'Water_Well', 'contacts__fax', 'contacts__email', 'calins__insCo', 'calins__dateEffective'
    )

    for entry in qlist:
        # writer.writerow([entry])
        writer.writerow(entry)
    writer.writerow(['This list has not been screened or scrubbed or checked against any do not call registrars.'])

    return response

def paginated_search_results(request, c):
    # form = QueryForm(request.POST)
    or_filter = {}
    or_carrier_opp = {}

    q = Question.objects.all()

    l = len(c)
    for i in range(l):
        print("*"*50)
        print(c[i])
        print("*"*50)

        if i == 0:
            if c [i] != 'ZipCode' and c[i] != '' and c[i] != 'enter value':
                q = q.filter(ZipCode__istartswith = c[i])
        if i == 1:
            if c [i] != 'City' and c[i] != '' and c[i] != 'enter value':
                q = q.filter(City__istartswith = c[i])
        if i == 2:
            if c [i] != 'State' and c[i] != '' and c[i] != 'enter value':
                q = q.filter(State__istartswith = c[i])
        else:
            if c[i] == 'interstate':
                or_carrier_opp.update({'Interstate':'X'})
            if c[i] == 'intrastate_hm':
                or_carrier_opp.update({'Intrastate_Only_HM':'X'})
            if c[i] == 'intrastate_non_hm':
                or_carrier_opp.update({'Intrastate_NonHM':'X'})


            if c[i] == 'auth_for_hire':
                or_filter.update({'Auth_For_Hire':'X'})
            if c[i] == 'exempt_for_hire':
                or_filter.update({"Exempt_For_Hire":'X'})
            if c[i] == 'privprop':
                or_filter.update({"Private_Property":'X'})
            if c[i] == 'privpass_buis':
                or_filter.update({"Priv_Pass_Business":'X'})
            if c[i] == 'pripass_non_buis':
                or_filter.update({"Priv_Pass_Non_Business":'X'})
            if c[i] == 'migrant':
                or_filter.update({"Migrant":'X'})
            if c[i] == 'us_mail':
                or_filter.update({"US_Mail":'X'})
            if c[i] == 'fed_gov':
                or_filter.update({"Fed_Gov":'X'})
            if c[i] == 'state_gov':
                or_filter.update({"State_Gov":'X'})
            if c[i] == 'local_gov':
                or_filter.update({"Local_Gov":'X'})
            if c[i] == 'indian_nation':
                or_filter.update({'Indian_Nation':'X'})



            if c[i] == 'gen_freight':
                or_filter.update({'General_Freight':'X'})
            if c[i] == 'houshold_goods':
                or_filter.update({'Household_Goods':'X'})
            if c[i] == 'metal':
                or_filter.update({'Metal_sheets_coils_rolls':'X'})
            if c[i] == 'motor_veh':
                or_filter.update({'Motor_Vehicles':'X'})
            if c[i] == 'log_poles_lumber':
                or_filter.update({'Logs_Poles_Beams_Lumber':'X'})
            if c[i] == 'BuildingMat':
                or_filter.update({'Building_Materials':'X'})
            if c[i] == 'MobileHome':
                or_filter.update({ 'Mobile_Homes' :'X'})
            if c[i] == 'Machinery':
                or_filter.update({'Machinery_Large_Objects':'X'})
            if c[i] == 'Produce':
                or_filter.update({'Fresh_Produce':'X'})
            if c[i] == 'LiquidGases':
                or_filter.update({'LiquidsGases':'X'})
            if c[i] == 'Intermodal':
                or_filter.update({'Intermodal_Cont':'X'})
            if c[i] == 'Passengers':
                or_filter.update({'Passengers':'X'})
            if c[i] == 'Oilfield Equipment':
                or_filter.update({'Oilfield_Equipment':'X'})
            if c[i] == 'Livestock':
                or_filter.update({'Livestock':'X'})
            if c[i] == 'grain':
                or_filter.update({'Grain_Feed_Hay':'X'})
            if c[i] == 'Coal':
                or_filter.update({'CoalCoke':'X'})
            if c[i] == 'Meat':
                or_filter.update({'Meat':'X'})
            if c[i] == 'Garbage':
                or_filter.update({'GarbageRefuse':'X'})
            if c[i] == 'UsMail':
                or_filter.update({ 'US_Mail' :'X'})
            if c[i] == 'Chemicals':
                or_filter.update({'Chemicals':'X'})
            if c[i] == 'Commodities':
                or_filter.update({'Commodities_Dry_Bulk':'X'})
            if c[i] == 'Refrigerated':
                or_filter.update({'Refrigerated_Food':'X'})
            if c[i] == 'Beverages':
                or_filter.update({'Beverages':'X'})
            if c[i] == 'paper':
                or_filter.update({'Paper_Products':'X'})
            if c[i] == 'Utilities':
                or_filter.update({'Utilities':'X'})
            if c[i] == 'Agricultural':
                or_filter.update({'AgriculturalFarm_Supplies':'X'})
            if c[i] == 'Construction':
                or_filter.update({'Construction':'X'})
            if c[i] == 'Water Well':
                or_filter.update({'Water_Well':'X'})
            if c[i] == 'tow_away':
                or_filter.update({'DriveTow_away':'X'})

            if c[i] == 'auth_for_hire_exclude':
                q= q.exclude(Auth_For_Hire='X')
            if c[i] == 'exempt_for_hire_exclude':
                q= q.exclude(Exempt_For_Hire='X')
            if c[i] == 'privprop_exclude':
                q = q.exclude( Private_Property ='X')
            if c[i] == 'privpass_buis_exclude':
                q = q.exclude( Priv_Pass_Business ='X')
            if c[i] == 'pripass_non_buis_exclude':
                q = q.exclude( Priv_Pass_Non_Business ='X')
            if c[i] == 'migrant_exclude':
                q = q.exclude( Migrant ='X')
            if c[i] == 'us_mail_exclude':
                q = q.exclude( US_Mail ='X')
            if c[i] == 'fed_gov_exclude':
                q = q.exclude( Fed_Gov ='X')
            if c[i] == 'state_gov_exclude':
                q = q.exclude( State_Gov ='X')
            if c[i] == 'local_gov_exclude':
                q = q.exclude( Local_Gov ='X')
            if c[i] == 'indian_nation_exclude':
                q = q.exclude( Indian_Nation ='X')
            if c[i] == 'interstate_exclude':
                q = q.exclude( Interstate ='X')
            if c[i] == 'intrastate_hm_exclude':
                q = q.exclude( Intrastate_NonHM ='X')
            if c[i] == 'intrastate_non_hm_exclude':
                q = q.exclude( Intrastate_NonHM ='X')
            if c[i] == 'gen_freight_exclude':
                q = q.exclude( General_Freight ='X')
            if c[i] == 'houshold_goods_exclude':
                q = q.exclude( Household_Goods ='X')
            if c[i] == 'metal_exclude':
                q = q.exclude( Metal_sheets_coils_rolls ='X')
            if c[i] == 'motor_veh_exclude':
                q = q.exclude( Motor_Vehicles ='X')
            if c[i] == 'log_poles_lumber_exclude':
                q = q.exclude( Logs_Poles_Beams_Lumber ='X')
            if c[i] == 'BuildingMat_exclude':
                q = q.exclude( Building_Materials ='X')
            if c[i] == 'MobileHome_exclude':
                q = q.exclude( Mobile_Homes ='X')
            if c[i] == 'Machinery_exclude':
                q = q.exclude(Machinery_Large_Objects='X')
            if c[i] == 'Produce_exclude':
                q = q.exclude(Fresh_Produce='X')
            if c[i] == 'LiquidGases_exclude':
                q = q.exclude(LiquidsGases='X')
            if c[i] == 'Intermodal_exclude':
                q = q.exclude(Intermodal_Cont='X')
            if c[i] == 'Passengers_exclude':
                q = q.exclude(Passengers='X')
            if c[i] == 'Oilfield Equipment_exclude':
                q = q.exclude(Oilfield_Equipment='X')
            if c[i] == 'Livestock_exclude':
                q = q.exclude(Livestock='X')
            if c[i] == 'grain_exclude':
                q = q.exclude(Grain_Feed_Hay='X')
            if c[i] == 'Coal_exclude':
                q = q.exclude(CoalCoke='X')
            if c[i] == 'Meat_exclude':
                q = q.exclude(Meat='X')
            if c[i] == 'Garbage_exclude':
                q = q.exclude(GarbageRefuse='X')
            if c[i] == 'UsMail_exclude':
                q = q.exclude( US_Mail ='X')
            if c[i] == 'Chemicals_exclude':
                q = q.exclude(Chemicals='X')
            if c[i] == 'Commodities_exclude':
                q = q.exclude(Commodities_Dry_Bulk='X')
            if c[i] == 'Refrigerated_exclude':
                q = q.exclude(Refrigerated_Food='X')
            if c[i] == 'Beverages_exclude':
                q = q.exclude(Beverages='X')
            if c[i] == 'paper_exclude':
                q = q.exclude(Paper_Products='X')
            if c[i] == 'Utilities_exclude':
                q = q.exclude(Utilities='X')
            if c[i] == 'Agricultural_exclude':
                q = q.exclude(AgriculturalFarm_Supplies='X')
            if c[i] == 'Construction_exclude':
                q = q.exclude(Construction='X')
            if c[i] == 'Water Well_exclude':
                q = q.exclude(Water_Well='X_exclude')
            if c[i] == 'tow_away_exclude':
                q = q.exclude(DriveTow_away='X')

    if bool(or_carrier_opp): #check if dict is empty
        q = q.filter(reduce(operator.or_,(Q(**d) for d in [dict([i]) for i in or_carrier_opp.items()])))
    if bool(or_filter): # check if dict is empty
        q = q.filter(reduce(operator.or_,(Q(**d) for d in [dict([i]) for i in or_filter.items()])))
    if c[i] == 'to_csv':
        return export_csv2(q)




    dbcount = q.count()
    return render(request, 'saferdb/list.html', {'text':dbcount , 'truckers': q })

def demo(request, c):
    or_filter = {}
    or_carrier_opp = {}

    if c[2]== 'CA':
        q = Question.objects.filter(calins__isnull=False)
    else:
        q = Question.objects.all()
    if True:
        for i in range(len(c)):
            if i == 0:
                if c [i] != 'ZipCode' and c[i] != '' and c[i] != 'enter value':
                    q = q.filter(ZipCode__istartswith = c[i])
            if i == 1:
                if c [i] != 'City' and c[i] != '' and c[i] != 'enter value':
                    q = q.filter(City__istartswith = c[i])
            if i == 2:
                if c [i] != 'State' and c[i] != '' and c[i] != 'enter value':
                    q = q.filter(State__istartswith = c[i])
            else:
                if c[i] == 'interstate':
                    or_carrier_opp.update({'Interstate':'X'})
                if c[i] == 'intrastate_hm':
                    or_carrier_opp.update({'Intrastate_Only_HM':'X'})
                if c[i] == 'intrastate_non_hm':
                    or_carrier_opp.update({'Intrastate_NonHM':'X'})

                if c[i] == 'auth_for_hire':
                    or_filter.update({'Auth_For_Hire':'X'})
                if c[i] == 'exempt_for_hire':
                    or_filter.update({"Exempt_For_Hire":'X'})
                if c[i] == 'privprop':
                    or_filter.update({"Private_Property":'X'})
                if c[i] == 'privpass_buis':
                    or_filter.update({"Priv_Pass_Business":'X'})
                if c[i] == 'pripass_non_buis':
                    or_filter.update({"Priv_Pass_Non_Business":'X'})
                if c[i] == 'migrant':
                    or_filter.update({"Migrant":'X'})
                if c[i] == 'us_mail':
                    or_filter.update({"US_Mail":'X'})
                if c[i] == 'fed_gov':
                    or_filter.update({"Fed_Gov":'X'})
                if c[i] == 'state_gov':
                    or_filter.update({"State_Gov":'X'})
                if c[i] == 'local_gov':
                    or_filter.update({"Local_Gov":'X'})
                if c[i] == 'indian_nation':
                    or_filter.update({'Indian_Nation':'X'})

                if c[i] == 'gen_freight':
                    or_filter.update({'General_Freight':'X'})
                if c[i] == 'houshold_goods':
                    or_filter.update({'Household_Goods':'X'})
                if c[i] == 'metal':
                    or_filter.update({'Metal_sheets_coils_rolls':'X'})
                if c[i] == 'motor_veh':
                    or_filter.update({'Motor_Vehicles':'X'})
                if c[i] == 'log_poles_lumber':
                    or_filter.update({'Logs_Poles_Beams_Lumber':'X'})
                if c[i] == 'BuildingMat':
                    or_filter.update({'Building_Materials':'X'})
                if c[i] == 'MobileHome':
                    or_filter.update({ 'Mobile_Homes' :'X'})
                if c[i] == 'Machinery':
                    or_filter.update({'Machinery_Large_Objects':'X'})
                if c[i] == 'Produce':
                    or_filter.update({'Fresh_Produce':'X'})
                if c[i] == 'LiquidGases':
                    or_filter.update({'LiquidsGases':'X'})
                if c[i] == 'Intermodal':
                    or_filter.update({'Intermodal_Cont':'X'})
                if c[i] == 'Passengers':
                    or_filter.update({'Passengers':'X'})
                if c[i] == 'Oilfield Equipment':
                    or_filter.update({'Oilfield_Equipment':'X'})
                if c[i] == 'Livestock':
                    or_filter.update({'Livestock':'X'})
                if c[i] == 'grain':
                    or_filter.update({'Grain_Feed_Hay':'X'})
                if c[i] == 'Coal':
                    or_filter.update({'CoalCoke':'X'})
                if c[i] == 'Meat':
                    or_filter.update({'Meat':'X'})
                if c[i] == 'Garbage':
                    or_filter.update({'GarbageRefuse':'X'})
                if c[i] == 'UsMail':
                    or_filter.update({ 'US_Mail' :'X'})
                if c[i] == 'Chemicals':
                    or_filter.update({'Chemicals':'X'})
                if c[i] == 'Commodities':
                    or_filter.update({'Commodities_Dry_Bulk':'X'})
                if c[i] == 'Refrigerated':
                    or_filter.update({'Refrigerated_Food':'X'})
                if c[i] == 'Beverages':
                    or_filter.update({'Beverages':'X'})
                if c[i] == 'paper':
                    or_filter.update({'Paper_Products':'X'})
                if c[i] == 'Utilities':
                    or_filter.update({'Utilities':'X'})
                if c[i] == 'Agricultural':
                    or_filter.update({'AgriculturalFarm_Supplies':'X'})
                if c[i] == 'Construction':
                    or_filter.update({'Construction':'X'})
                if c[i] == 'Water Well':
                    or_filter.update({'Water_Well':'X'})
                if c[i] == 'tow_away':
                    or_filter.update({'DriveTow_away':'X'})

                if c[i] == 'auth_for_hire_exclude':
                    q= q.exclude(Auth_For_Hire='X')
                if c[i] == 'exempt_for_hire_exclude':
                    q= q.exclude(Exempt_For_Hire='X')
                if c[i] == 'privprop_exclude':
                    q = q.exclude( Private_Property ='X')
                if c[i] == 'privpass_buis_exclude':
                    q = q.exclude( Priv_Pass_Business ='X')
                if c[i] == 'pripass_non_buis_exclude':
                    q = q.exclude( Priv_Pass_Non_Business ='X')
                if c[i] == 'migrant_exclude':
                    q = q.exclude( Migrant ='X')
                if c[i] == 'us_mail_exclude':
                    q = q.exclude( US_Mail ='X')
                if c[i] == 'fed_gov_exclude':
                    q = q.exclude( Fed_Gov ='X')
                if c[i] == 'state_gov_exclude':
                    q = q.exclude( State_Gov ='X')
                if c[i] == 'local_gov_exclude':
                    q = q.exclude( Local_Gov ='X')
                if c[i] == 'indian_nation_exclude':
                    q = q.exclude( Indian_Nation ='X')
                if c[i] == 'interstate_exclude':
                    q = q.exclude( Interstate ='X')
                if c[i] == 'intrastate_hm_exclude':
                    q = q.exclude( Intrastate_NonHM ='X')
                if c[i] == 'intrastate_non_hm_exclude':
                    q = q.exclude( Intrastate_NonHM ='X')
                if c[i] == 'gen_freight_exclude':
                    q = q.exclude( General_Freight ='X')
                if c[i] == 'houshold_goods_exclude':
                    q = q.exclude( Household_Goods ='X')
                if c[i] == 'metal_exclude':
                    q = q.exclude( Metal_sheets_coils_rolls ='X')
                if c[i] == 'motor_veh_exclude':
                    q = q.exclude( Motor_Vehicles ='X')
                if c[i] == 'log_poles_lumber_exclude':
                    q = q.exclude( Logs_Poles_Beams_Lumber ='X')
                if c[i] == 'BuildingMat_exclude':
                    q = q.exclude( Building_Materials ='X')
                if c[i] == 'MobileHome_exclude':
                    q = q.exclude( Mobile_Homes ='X')
                if c[i] == 'Machinery_exclude':
                    q = q.exclude(Machinery_Large_Objects='X')
                if c[i] == 'Produce_exclude':
                    q = q.exclude(Fresh_Produce='X')
                if c[i] == 'LiquidGases_exclude':
                    q = q.exclude(LiquidsGases='X')
                if c[i] == 'Intermodal_exclude':
                    q = q.exclude(Intermodal_Cont='X')
                if c[i] == 'Passengers_exclude':
                    q = q.exclude(Passengers='X')
                if c[i] == 'Oilfield Equipment_exclude':
                    q = q.exclude(Oilfield_Equipment='X')
                if c[i] == 'Livestock_exclude':
                    q = q.exclude(Livestock='X')
                if c[i] == 'grain_exclude':
                    q = q.exclude(Grain_Feed_Hay='X')
                if c[i] == 'Coal_exclude':
                    q = q.exclude(CoalCoke='X')
                if c[i] == 'Meat_exclude':
                    q = q.exclude(Meat='X')
                if c[i] == 'Garbage_exclude':
                    q = q.exclude(GarbageRefuse='X')
                if c[i] == 'UsMail_exclude':
                    q = q.exclude( US_Mail ='X')
                if c[i] == 'Chemicals_exclude':
                    q = q.exclude(Chemicals='X')
                if c[i] == 'Commodities_exclude':
                    q = q.exclude(Commodities_Dry_Bulk='X')
                if c[i] == 'Refrigerated_exclude':
                    q = q.exclude(Refrigerated_Food='X')
                if c[i] == 'Beverages_exclude':
                    q = q.exclude(Beverages='X')
                if c[i] == 'paper_exclude':
                    q = q.exclude(Paper_Products='X')
                if c[i] == 'Utilities_exclude':
                    q = q.exclude(Utilities='X')
                if c[i] == 'Agricultural_exclude':
                    q = q.exclude(AgriculturalFarm_Supplies='X')
                if c[i] == 'Construction_exclude':
                    q = q.exclude(Construction='X')
                if c[i] == 'Water Well_exclude':
                    q = q.exclude(Water_Well='X_exclude')
                if c[i] == 'tow_away_exclude':
                    q = q.exclude(DriveTow_away='X')

    if bool(or_carrier_opp): #check if dict is empty
        print(or_carrier_opp.items())
        q = q.filter(reduce(operator.and_,(Q(**d) for d in [dict([i]) for i in or_carrier_opp.items()])))
    if bool(or_filter): # check if dict is empty
        print(or_filter.items())
        q = q.filter(reduce(operator.or_,(Q(**d) for d in [dict([i]) for i in or_filter.items()])))


    if c[2]== 'CA':
        start = datetime.date.today().month
        middle = (start + 2) % 12
        end = (start + 3)%12
        q = q.filter(Q(calins__dateEffective__month=start) | Q(calins__dateEffective__month=middle) |
        Q(calins__renewalMonth=end))

    if c[-1] == 'to_csv':
        if request.user.is_authenticated:
            return export_csv2(q)
        else:
            return export_csv2(q[:5])

    if c[2]== 'CA':
        if request.user.is_authenticated:
            return render(request, 'saferdb/calilist.html', {'truckers': q})
        else:
            return render(request, 'saferdb/calilist.html', {'truckers': q[:5] })
    else:
        if request.user.is_authenticated:
            return render(request, 'saferdb/list.html', {'truckers': q})
        else:
            return render(request, 'saferdb/list.html', {'truckers': q[:5] })




@method_decorator(login_required, name='post')
class AdvancedSearch(ListView):
    template_name= 'saferdb/AdvancedQuery.html'
    global e

    def get(self, request):
        global e
        if request.GET.get('page'):
            return paginated_search_results(request, e)
        form = QueryForm()
        return render(request, self.template_name , {'form': form})

    def post(self, request):
        global e
        e = None
        e = request.POST.getlist('opeclass')
        return paginated_search_results(request, e)

@method_decorator(login_required, name='post')
class QueryView(ListView):
    template_name= 'saferdb/query.html'
    global d

    def get(self, request):
        global d
        if request.GET.get('page'):
            return paginated_search_results(request, d)
        form = QueryForm()
        return render(request, self.template_name , {'form': form})

    def post(self, request):
        global d
        d = None
        d = request.POST.getlist('opeclass')
        return paginated_search_results(request, d)

# @method_decorator(login_required, name='post')
class CalsearchDemo(ListView):
    template_name= 'saferdb/caliquery.html'
    global d

    def get(self, request):
        global d
        if request.GET.get('page'):
            return paginated_search_results(request, d)
        form = QueryForm()
        return render(request, self.template_name , {'form': form})

    def post(self, request):
        global d
        d = None
        d = request.POST.getlist('opeclass')
        return demo(request, d)

# STATIC Pages
def help(request):
    return render(request, 'saferdb/help.html')
def about(request):
    return render(request, 'saferdb/about.html')
def faq(request):
    return render(request, 'saferdb/faq.html')
