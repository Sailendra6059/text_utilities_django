from django.http import HttpResponse
from django.shortcuts import render
def home(request):

    li={"data":[1,2,3,4,5,6],
        "name":"Sailendra"} # Here the data that which we gonna post to html should be dictionary
    return render(request,"index.html",li)
    #return HttpResponse("Hello,World!")
def textanalyzer(request):
    inputdata=request.GET.get("text")
    print(inputdata)
    selected=request.GET.get("analyze")
    capitalize=request.GET.get("capitalize")
    if(selected=="on"):
        analyzed=""
        special="~!@#$%^&*~|/+?{}()></-*"
        for i in inputdata:
            if(i in special):
                continue
            else:
                analyzed+=i
        if(capitalize=="on"):
            analyzed=analyzed.title();
        return render(request,'analyzed_text.html',{"res":analyzed})
    else:
        return render(request,'analyzed_text.html',{"res":inputdata})


