from django.http import HttpResponse
from django.shortcuts import render
import joblib
#python .\manage.py runserver
def home(request):
    return render(request,"home.html")

def res(request):
    cls=joblib.load('final_model.sav') 
    lis=[]
    lis.append(request.POST.get('gender'))
    lis.append(int(request.POST.get('ssc_p')))
    lis.append(request.POST.get('ssc_b'))
    lis.append(int(request.POST.get('hss_p')))
    lis.append(request.POST.get('hss'))
    lis.append(request.POST.get('hsc'))
    lis.append(int(request.POST.get('degree_p')))
    lis.append(request.POST.get('Degree'))
    lis.append(request.POST.get('workex'))
    lis.append(int(request.POST.get('etest_p')))
    lis.append(request.POST.get('spec'))
    lis.append(int(request.POST.get('mba_p')))

    print(lis)

    ans=cls.predict([lis])
    print(ans)
    return render(request,"result.html",{'ans':ans})