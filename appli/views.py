
from time import sleep
from django.views.generic import TemplateView,ListView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate,get_user_model
from appli.models import *
from univ.settings import AUTH_USER_MODEL       

''''
Mes codes de connexion
inscription
et deconnexion
'''
User= get_user_model()
class connex:
    def __init__(self) -> None:
        pass  
    # Table de connexion
    def connexion(request):
        if request.method =='POST':
            nom = request.POST.get('name')
            passe = request.POST.get('password')
            user=authenticate(username=nom,
                             password=passe)
            if user:
                login(request,user)
                return redirect('index')
        return render(request, 'connexion.html')
    
    # Table d'inscription
    def inscription(request):
        
        if request.method =='POST':
            nom = request.POST.get('name')
            passe = request.POST.get('password')
            try:
                    user = User.objects.create_user(
                        username=nom,
                        password=passe
                    )
                    login(request,user)
                    return redirect('index')
            except:
                a = True

                return render(request, 'inscription.html',{'a':a})
        return render(request, 'inscription.html')
    
    # Table deconnexion
    def deconnexion(request):
        logout(request)
        return redirect('index')




# Create your views here.
def index(request):
   
    return render(request, 'index.html')

class About:
    def about(request):
        return render(request, 'about.html')

class FAQView(TemplateView):
    template_name = "blog.html" 
class Blog_detail(TemplateView):
    template_name = "blog_details.html"    