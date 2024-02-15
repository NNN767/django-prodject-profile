from django.shortcuts import render
from .models import blog as bd_blog
from .models import person_img
from portfolio.models import Project





# Create your views here.


def blog(request):
    test = bd_blog.objects.all()
    img = person_img.objects.all()
    img_lent = Project.objects.all()

    return render(request,'blog/home.html', {'test' : test, 'img':img,'img_lent':img_lent})