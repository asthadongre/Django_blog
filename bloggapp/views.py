from django.core import paginator
from django.shortcuts import redirect, render
from django.views.generic import DetailView
from django.core.paginator import Paginator
from django.core.exceptions import ValidationError
from bloggapp.models import Blog
from bloggapp.form import BlogF

# Create your views here.



def bloghome(request):
    return render(request,"home.html")


def createblog(request):
    form = BlogF()
    if request.method == "POST":
        try:
        
            title=request.POST.get('title')
    
            name=request.POST.get('name')
        
            description=request.POST.get('description')
            created_on=request.POST.get('created_on')

            b=Blog(title=title,name=name,description=description,created_on=created_on)
            b.save()
            return redirect('/blogView')
        except ValidationError as e:
            return redirect('/create')
    
        
    return render(request,"createblog.html")
    

def blogView(request):
    blog=Blog.objects.all()
    p=Paginator(blog,2)
    page_number=request.GET.get('page')
    blog_obj=p.get_page(page_number)

    return render(request,"bloghome.html",{"blog_obj":blog_obj})



class DisplayOneData(DetailView):    
    model = Blog