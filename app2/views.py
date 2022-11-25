from django.shortcuts import render

# Create your views here.
def a2_first(request):
    d={'a':234,'b':567,'c':890}
    return render(request,'a2_first.html',d)
def a2_second(request):
    d={'name':'MAHI'}
    return render(request,'a2_second.html',d)
