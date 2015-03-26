from django.shortcuts import render_to_response , redirect,get_object_or_404
from blog.form import Login,RegisterForm
from django.template import RequestContext
from django.core.context_processors import request
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate , logout, login
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.models import Permission, User
from django.contrib.auth import authenticate , logout, login


# Create your views here.
def out(request): 
    login = Login()
    logout(request)
    return render_to_response("blog/cp.html",{"form":login},RequestContext(request))

@csrf_exempt
def logins(request):
    
        usern = request.POST.get('login')
        passw = request.POST.get('password')
        user = authenticate(username=usern, password=passw)
        if  request.user.is_authenticated():
            return redirect('/blog/user')
        if user is not None:
            if user.is_active:
#                 power = get_object_or_404(User, pk=2)
#                 permission = Permission.objects.get(codename='can_publish')
#                 power.user_permissions.add(permission)
                
                login(request, user)
                return redirect('/blog/user')
        else:
            return redirect('/blog/logout')

@csrf_exempt
def signup(request):   
    form = RegisterForm()
    if request.POST:
        data = request.POST.copy()
        form = RegisterForm(request.POST)
       
                
        if form.is_valid():
            pass
            user =User.objects.create_user(data['login'],data['mail'],data['password'])
            user.is_active = True
            user.save()

            return redirect('/index')
        else:
            return render_to_response('blog/register.html',{'form':form},RequestContext(request))
    else:
            return render_to_response('blog/register.html',{'form':form},RequestContext(request)) 
        
    
def usercp(request):
    user =request.user
    power = get_object_or_404(User, pk=1)

    return render_to_response("blog/user.html",{"user":user},RequestContext(request))

def lostpassword(request):
    pass

def activesend(request):
    pass
    

