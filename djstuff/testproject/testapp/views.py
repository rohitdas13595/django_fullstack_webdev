from django.shortcuts import render

def index(request):
    mydict ={'Insert_content':'This from the testapp.'}
    return render(request,'testapp/index.html', context=mydict)
