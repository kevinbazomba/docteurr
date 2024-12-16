from django.urls import path
from appli.views import*

urlpatterns = [
   
    path('', index ,name='index'),
    path('about', About.about ,name='about'),
    path('blog', FAQView.as_view(),name='blog'),
    path('blog_detail', Blog_detail.as_view(),name='blog_detail'),
    path('connexion', connex.connexion, name='connexion'),
    path('inscription', connex.inscription, name='inscription'),
    path('deconnexion', connex.deconnexion, name='deconnexion'), 
]
