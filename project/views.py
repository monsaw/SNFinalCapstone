from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,DeleteView,UpdateView,CreateView
from project.models import Blog,Category
from project.forms import BaseUserForm,RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def origin(request):
    cats = Category.objects.all()
    context = {'cats':cats}
    return render(request,'base.html', context)
# class Cats(ListView):
#     template_name = 'base.html'
#     model = Category
#     context_object_name = 'cat_list'

class CatDetails(LoginRequiredMixin,DetailView):
    template_name = "catdetail.html"
    model = Category
    context_object_name = 'catdel'

class Home(ListView):
    template_name = 'home.html'
    model = Blog
    context_object_name = 'blogs'

class Detail(DetailView):
    
    template_name ='detail.html'
    model = Blog
    context_object_name = 'blog'

class CatCreate(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'home.html'
    model = Category
    fields = "__all__"
    template_name = 'catcreate.html'

class BlogCreate(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'home.html'
    model = Blog
    fields = "__all__"
    template_name = 'blogcreate.html'

class BlogUpdate(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'home.html'
    model = Blog
    fields = "__all__"
    template_name = 'blogupdate.html'

class BlogDelete(LoginRequiredMixin,DeleteView):
    login_url = '/login/'
    redirect_field_name = 'home.html'
    model = Blog
    template_name = 'blogdelete.html'
    success_url = reverse_lazy('project:home')

def index(request):
    return render(request,'index.html',{})

def registration(request):
    registered = False

    if request.method == 'POST':
        baseuser = BaseUserForm(request.POST)
        register = RegistrationForm(request.POST)

        if baseuser.is_valid() and register.is_valid():
            user = baseuser.save(commit = False)
            user.set_password(user.password)
            user.save()


            profile = register.save(commit = False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(baseuser.errors,register.errors)

    else:
        baseuser = BaseUserForm()
        register = RegistrationForm()
    return render(request, 'registration.html', {
    'registered':registered,
    'baseuser':baseuser,
    'register':register
    })

#  Sign view for everyone that visit the website (function)
def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request,user)
                return redirect('project:home')
            else:
                return HttpResponse('Account not Active ! ')
        else:
            return HttpResponse(f'Invalid Login Parameters, Either {username} or {password} is not correct !')
    else:
        return render(request,'login.html',{})


#  Signout view for everyone that visit the website this required sign in first(function)
@login_required
def sign_out(request):
    logout(request)
    return redirect('project:login')
