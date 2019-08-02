from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'default')
    fullcaps = request.POST.get('fullcaps', 'default')
    newlineremover = request.POST.get('newlineremover', 'default')
    spaceremover = request.POST.get('spaceremover', 'default')
    if removepunc=='on':
        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed+=char
        params = {'purpose': 'Remove Punctuation', 'analyzed_text': analyzed}
        djtext=analyzed
       # return render(request, 'analyze.html', params)
    if(fullcaps=='on'):
        analyzed = ""
        for char in djtext:
            analyzed+=char.upper()
        params = {'purpose': 'Change to Upper', 'analyzed_text': analyzed}
        djtext = analyzed
       # return render(request, 'analyze.html', params)
    if(newlineremover=='on'):
        analyzed = ""
        for char in djtext:
            if char!='\n' and char!='\r':
                analyzed += char
        params = {'purpose': 'Remove new line', 'analyzed_text': analyzed}
        djtext = analyzed
       # return render(request, 'analyze.html', params)
    if (spaceremover == 'on'):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed+=char
        params = {'purpose': 'Remove Space', 'analyzed_text': analyzed}
        djtext = analyzed
       # return render(request, 'analyze.html', params)
    if(removepunc=='on' or spaceremover=='on' or  newlineremover=='on' or fullcaps=='on'):
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")
'''if djtext[index] == " " and djtext[index+1]==" ":
                pass
            else:
                analyzed += char'''