from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template.loader import render_to_string

weeks = {
    'monday': "Welcome to Monday",
    "tuesday": 'Welcome to Tuesday',
    "wednesday": 'Welcome to Wednesday'
    }
def index(request):
    week_list = list(weeks.keys())
    return render(request, 'first_app/index.html', {
        'week_list':week_list
    })


def monday(request, week):
    try:
        response_txt = weeks[week]
        return HttpResponse(response_txt)
    except:
        return Http404()
    

def tue(request):
    return render(request,'firstapp/tuesday.html')
   