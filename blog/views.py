from django.shortcuts import render

from portfolio.models import Project





# Create your views here.


def blog(request):
    test = Project.objects.all()

    return render(request,'blog/home.html', {'test' : test})