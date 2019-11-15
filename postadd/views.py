from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,'input.html')
def add(request):
    try:
        v1=request.POST['t1']
        v2=request.POST['t1']
        i=int(v1)
        j=int(v2)
        k=i+j
        return HttpResponse("""<html><body bgcolor=green>sum is:"""+str(k)+"""</body></html>""")
    except:
        return render(request,'input.html')
