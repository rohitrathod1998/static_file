from django.shortcuts import render


# Create your views here.
def system(request):
    return render(request,'system.html')