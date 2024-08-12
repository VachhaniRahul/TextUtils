from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def removepunc(request):
    # get the text from home page
    djtext = request.POST.get('text','default')
    # print(djtext)
    
    # we checked which method user choose
    removepunc1 = request.POST.get('removepunc','off')
    capfirst1 = request.POST.get('Capitalize','off')
    Lowercase = request.POST.get('LowerCase','off')
    count = request.POST.get('count','off')
    space = request.POST.get('space','off')

    print(removepunc1)
    if removepunc1!='off':
        punc = '''.,?!:;'"-—()[]{}.../\&*@#$%^_|~<>=+'''
        Result = ''
        for ele in djtext:
            if ele not in punc:
                Result = Result+ele
        content = {'name':'Remove Puctuations',
                   'Result':Result}
        djtext = Result
        # print(djtext)
        
    
    if capfirst1!='off':
        Result = djtext.upper()
        content = {'name':'Capitalize Text',
                    'Result':Result}
        djtext = Result
        # print(djtext)
       
    
    if Lowercase!='off':
        Result = djtext.lower()
        content = {'name':'LowerCase Text',
                    'Result':Result}
        djtext = Result
        # print(djtext)
        
    
    if count!='off':
        Result = len(djtext)
        content = {'name':'Count Alphabets',
                    'Result':Result}
        djtext = Result
      
    
    if space!='off':
        Result =''
        for i,j in enumerate(djtext):
            if djtext[i] == " " and djtext[i+1]==" ":
                pass
            else:
                Result = Result + j
        
        content = {'name':'Remove Extra Space',
                    'Result':Result}
        
    if removepunc1=='off' and Lowercase =='off' and count=='off' and space == 'off' and capfirst1 == 'off':
        return render(request,'index.html')        


    return render(request,'removepunc.html',content)
    

    
    



