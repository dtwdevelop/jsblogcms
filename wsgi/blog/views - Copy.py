from django.shortcuts import render_to_response , redirect,get_object_or_404
# Create your views here.
from django.core.context_processors import request
from blog.models import Category,Page,Item ,Gallery
#from blog.user import User
from blog.form import  Contact,FileUpload
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from django.core.paginator import Paginator,  EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib import messages
from django.utils.translation import  activate, ugettext as _
from django.template import RequestContext
from django.core import serializers
from django.http import HttpResponse
#sort post by time

def index(request,orderby='-pub_date'):

    site=_('site')
#     activate('ru')
    
    categories = Category.objects.all()
    if(request.GET.get('q')):
        s=request.GET.get('q')
        categories= categories.filter(title_category__istartswith=s)
    if(request.GET.get('tag')):
        tag=request.GET.get('tag')
        categories= categories.filter(title_category__icontains=tag) 
    if(request.GET.get('category')):
        category=request.GET.get('category')       
        categories= categories.filter(title_category__icontains=category)
    if  request.GET.get('filter'):
        cat =request.GET.get('filter')
        categories=categories.filter(title_category__icontains=cat)
    if  request.GET.get('orderby') =='name':
        categories=categories.order_by('title_category')
        
    elif  request.GET.get('orderby') =='date':
        categories=categories.order_by('pub_date')
    else:
        categories=categories.order_by(orderby)
        
   
        
    paginator = Paginator(categories , 2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render_to_response("blog/index.html",
                              {"lists":contacts,'site':site},RequestContext(request))

def handle_uploaded_file(f):
    with open('web/media/upload/name.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            
@login_required(login_url='/blog/login/')
def list(request):
    
    msg = messages.get_messages(request)
    form = FileUpload()
    if request.method == 'POST':
        form = FileUpload(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            messages.success(request, 'Welcome to security page.')
            return redirect('/index/')
        else:
            return redirect('/blog/list')
    else:
        return render_to_response("blog/page.html",{"post":"Secound",'messages':msg,'file':form}
                                    ,RequestContext(request))
def viewpage(request,pid):
    try:
        post =Page.objects.get(id=pid)
    except Page.DoesNotExist:
        raise Http404("Not found")
        
    return render_to_response("blog/view.html",{'data':post},RequestContext(request))

@csrf_exempt
def video(request):
    pass

    return render_to_response("blog/video.html",{'data':video},RequestContext(request))

def gallery(request):
    
    foto = Gallery.objects.all()
    paginator = Paginator(foto , 2)
    page = request.GET.get('page')
    try:
        pthotos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pthotos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pthotos = paginator.page(paginator.num_pages)
    return render_to_response("blog/gallery.html",{'fotos':pthotos},RequestContext(request))
        
    

@permission_required('blog.can_publish',login_url='/index/')


def manager(request): 
    
    
    return render_to_response("blog/manager.html",{"data":"Hello manager"},RequestContext(request))  

def menu(request): 
    data = serializers.serialize("json", Item.objects.all()) 
    return HttpResponse(data)

@csrf_exempt
def contact(request,**r):
    form = Contact()
    if request.POST:
        data =request.POST
        form = Contact(data)
        if form.is_valid:
            pass
            #data= send_mail('Thanks you', 'Contact from', 'from@example.com',['to@example.com'], fail_silently=False)
            return render_to_response("blog/contact.html",{"form":form,"data":data},RequestContext(request))
        else:
            raise Http404("Not found")
    else:
        return render_to_response("blog/contact.html",{"form":form},RequestContext(request))
    