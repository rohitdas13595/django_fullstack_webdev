from django.shortcuts import render
from django.http import HttpResponse
import codecs



    #f=open('G:/django/dform.html','r')
    #s=f.read()

def help(request):
    helpdict ={'help_insert':'HELP PAGE'}
    return render(request,'second_app/help.html',context=helpdict)
