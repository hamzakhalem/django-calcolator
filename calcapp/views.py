from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def submitquery(request):
    q = request.GET['query']
    print(q)
    # result = eval(q)
    # print(result)
    try:
        result = eval(q)
        context = {
            "q" : q,
            "result" : result,
            "error" : False
        }
        return render(request, "index.html", context = context)
    except:
       context = {
            "error" : True
        }
       return render(request, "index.html", context = context)
    