from django.shortcuts import render

# Create your views here.
def carousel_specific(request):
    return render(request,'carousel_specific.html')