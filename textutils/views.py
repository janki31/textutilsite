from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    utxt=request.POST.get('text','')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charactercount=request.POST.get('charactercount','off')

    p = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
    if removepunc=="on":
        analyzetext = ""
        for t in utxt:
            if t not in p:
                analyzetext=analyzetext+t
        utxt=analyzetext

    if fullcaps=="on":
        analyzetext = ""
        for t in utxt:
            analyzetext=analyzetext+t.upper()
        utxt = analyzetext


    if newlineremover=="on":
        analyzetext = ""
        for t in utxt:
            if t !='\n' and t!='\r':
                analyzetext=analyzetext+t
        utxt = analyzetext


    if extraspaceremover=="on":
        for t in utxt:
            if t!=' ':
                analyzetext=analyzetext+t
        utxt = analyzetext

    if charactercount=="on":
        analyzetext = ""
        count=0
        for t in utxt:
            if t.isdigit()!=True and t!=' ' and t not in p and t !='\n' and t!='\r':
                count+=1
        analyzetext=utxt+"\n Total Character :- "+str(count)

    if removepunc=="off" and fullcaps=="off" and newlineremover=="off" \
            and extraspaceremover=="off"and charactercount=="off":
        analyzetext="Please Select Proper Utilization option"

    params = {'analyzetext': analyzetext}


    return render(request,'Analyze.html',params)

def about(request):
    return render(request,'about.html')