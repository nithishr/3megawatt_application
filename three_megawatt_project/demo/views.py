from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from demo.models import Site,SiteDetail
from django.db.models import Avg,Sum

def sites(request):
    site_list = Site.objects.all()
    context_dict = {'sites':site_list}
    context_dict['class1']='active'
    context_dict['class2']='unactive'
    return render(request, "demo/sites.html", context_dict)

def site_detail(request, site_id):
    context_dict = {}
    site = Site.objects.get(id=site_id)
    context_dict['site_name'] = site.name

    site_details = SiteDetail.objects.filter(site=site)

    # Adds our results list to the template context under name pages.
    context_dict['site_details'] = site_details
    context_dict['site'] = site
    context_dict['class1']='active'
    context_dict['class2']='unactive'

    # Go render the response and return it to the client.
    return render(request, 'demo/details.html', context_dict)

def summary(request):
    context_dict = {}
    sum_list = []
    context_dict['Sums']=sum_list
    site_list = Site.objects.all()
    for site in site_list:
        site_details = SiteDetail.objects.filter(site=site)
        #Aggregation using SQL over Django API
        a_sum = SiteDetail.objects.filter(site=site).aggregate(Sum('a_value'))['a_value__sum']
        b_sum = SiteDetail.objects.filter(site=site).aggregate(Sum('b_value'))['b_value__sum']
        site_detailsp = SiteDetail.objects.filter(site=site)
        #Aggregation using Python
        a_sump,b_sump = python_aggregations(site_detailsp,'add')
        # print a_sump,b_sump
        site_name = site.name
        # site_avg={'site_name':site_name,'a_sum':a_sum,'b_sum':b_sum}
        # print site_avg
        site_sum=[site_name,a_sum,b_sum]
        context_dict['Sums'].append(site_sum)
        # print a_sum
    context_dict['class1']='unactive'
    context_dict['class2']='active'
    # print context_dict
    # print site_list
    return render(request,'demo/summary.html', context_dict)

def summary_avg(request):
    context_dict = {}
    avg_list = []
    context_dict['Averages']=avg_list
    site_list = Site.objects.all()
    for site in site_list:
        site_details = SiteDetail.objects.filter(site=site)
        #Aggregation using SQL over Django API
        a_avg = SiteDetail.objects.filter(site=site).aggregate(Avg('a_value'))['a_value__avg']
        b_avg = SiteDetail.objects.filter(site=site).aggregate(Avg('b_value'))['b_value__avg']
        site_detailsp = SiteDetail.objects.filter(site=site)
        #Aggregation using Python
        a_avgp,b_avgp = python_aggregations(site_detailsp,'avg')
        # print a_avgp,b_avgp
        site_name = site.name
        # site_avg={'site_name':site_name,'a_avg':a_avg,'b_avg':b_avg}
        # print site_avg
        site_avg=[site_name,a_avg,b_avg]
        context_dict['Averages'].append(site_avg)
        context_dict['class1']='unactive'
        context_dict['class2']='active'
        # print a_avg
    # print context_dict
    # print site_list
    return render(request,'demo/average.html', context_dict)

def python_aggregations(site_detailsp, operate):
    a_res = 0
    b_res = 0
    count = 0
    for site_detailp in site_detailsp:
        a_res += site_detailp.a_value
        b_res += site_detailp.b_value
        count += 1
    if operate == 'avg':
        a_res = a_res/count
        b_res = b_res/count
    return a_res,b_res
