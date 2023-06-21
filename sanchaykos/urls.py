from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('add', views.add, name='add'),
    path('about', views.about, name='about'),
    path('company-vision', views.companyVision, name='company-vision'),

    path('projects', views.projects, name='projects'),
    path('projectsimg/<int:id>/', views.projectsImage, name='projectsimg'),

    path('login', views.loginUser, name='login'),
    path('logout',views.logoutUser,name="logout"),
    path('addnewsletter',views.addNewsletter,name="addnewsletter"),
    path('company-values', views.companyValues, name='company-values'),
    path('company-team', views.companyTeam, name='company-team'),
    path('company-chairman', views.companyChairman, name='company-chairman'),
    path('company-board', views.companyBoard, name='company-board'),
    path('companynews', views.companyNews, name='companynews'),
    path('generalnotices', views.generalNotices, name='generalnotices'),
    path('tendernotices', views.tenderNotices, name='tendernotices'),
    path('hrnotices', views.hrNotices, name='hrnotices'),
    path('pressrelease', views.pressRelease, name='pressrelease'),
]