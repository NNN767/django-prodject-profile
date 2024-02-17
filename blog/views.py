from django.shortcuts import render , get_object_or_404
from .models import blog as bd_blog
from .models import person_img
from portfolio.models import Project





# Create your views here.


def blog(request):
    test = bd_blog.objects.all()
    img = person_img.objects.all()
    img_lent = Project.objects.all()

    return render(request,'blog/home.html', {'test' : test, 'img':img,'img_lent':img_lent})

def detail(request, blog_id ):
    date = get_object_or_404(bd_blog,pk = blog_id )
    return render(request,'blog/detail.html',{'id':date})