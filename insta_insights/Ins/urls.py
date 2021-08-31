from django.urls import path
from . import views

urlpatterns=[
    path('',views.dashboard,name='Home'),
    path('account',views.erreichte_Konten,name='Account'),
    path('content',views.content_Interaktionen,name='Content'),
    path('group',views.zielGruppe,name='Group')
]
