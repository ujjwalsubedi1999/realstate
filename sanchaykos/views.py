from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from sanchaykos.models import *
# Create your views here.


def home(request):
    chair = Chairman.objects.all()
    abs = Abstract.objects.all()
    slid = Slider.objects.filter(is_archived=False)
    proj = Projects.objects.all()
    abtfooter = AboutUs.objects.all()
    data = {
        'chair': chair,
        'abs': abs,
        'slid': slid,
        'abtfooter': abtfooter,
        'proj': proj,
    }
    return render(request, 'index.html', data)


def contact(request):
    abtfooter = AboutUs.objects.all()
    comcon = CompanyContacts.objects.all()
    data = {
        'abtfooter': abtfooter,
        'comcon': comcon,
    }
    return render(request, 'contact.html',data)


def add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        cont = Contacts(name=name, email=email, phone=phone, message=message)
        cont.save()

        return redirect('contact')

    return render(request, 'contact.html')


def about(request):
    abtfooter = AboutUs.objects.all()
    data = {
        'abtfooter': abtfooter,
    }
    return render(request, 'about.html', data)


def blog(request):
    abtfooter = AboutUs.objects.all()
    data = {
        'abtfooter': abtfooter,
    }
    return render(request, 'blog-grid.html',data)

# foreign key concept


def projects(request):
    proj = Projects.objects.all()
    abtfooter = AboutUs.objects.all()
    data = {
        'proj': proj,
        'abtfooter': abtfooter,
    }
    return render(request, 'projects.html', data)


def projectsImage(request, id):
    projectimg = get_object_or_404(Projects, id=id)
    photos = ProjectsImage.objects.filter(projectimg=projectimg)
    abtfooter = AboutUs.objects.all()
    data = {
        'projectimg': projectimg,
        'photos': photos,
        'abtfooter': abtfooter,
    }
    return render(request, 'projectsimage.html', data)


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/admin")
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')
    abtfooter = AboutUs.objects.all()        
    data = {
        'abtfooter': abtfooter,
    }
    return render(request, 'login.html',data)


def logoutUser(request):
    logout(request)
    return redirect("/login")


def addNewsletter(request):
    if request.method == "POST":
        email = request.POST.get('email')
        news = Newsletter(email=email)
        news.save()

        return redirect('home')
    return render(request, 'index.html')


def companyVision(request):
    abt = Vision.objects.all()
    abtfooter = AboutUs.objects.all()
    data = {
        'abt': abt,
        'abtfooter': abtfooter,
    }
    return render(request, "company-vision.html", data)


def companyValues(request):
    abt = CoreValues.objects.all()
    abtfooter = AboutUs.objects.all()
    data = {
        'abt': abt,
        'abtfooter': abtfooter,
    }
    return render(request, "company-values.html", data)


def companyBoard(request):
    bord = Board.objects.all()
    abtfooter = AboutUs.objects.all()
    data = {
        'bord': bord,
        'abtfooter': abtfooter,
    }
    return render(request, "company-board.html", data)


def companyTeam(request):
    abt = OurTeam.objects.all()
    abtfooter = AboutUs.objects.all()
    data = {
        'abt': abt,
        'abtfooter': abtfooter,
    }
    return render(request, "company-team.html", data)


def companyChairman(request):
    chair = Chairman.objects.all()
    abtfooter = AboutUs.objects.all()
    data = {
        'chair': chair,
        'abtfooter': abtfooter,
    }
    return render(request, "company-chairman.html", data)


def companyNews(request):
    cnews = CompanyNews.objects.all().order_by('-id')
    abtfooter = AboutUs.objects.all()
    data = {
        'cnews': cnews,
        'abtfooter': abtfooter,
    }
    return render(request, "company-news.html", data)


def generalNotices(request):
    gnot = GeneralNotice.objects.all().order_by('-id')
    abtfooter = AboutUs.objects.all()
    data = {
        'gnot': gnot,
        'abtfooter': abtfooter,
    }
    return render(request, "general-notices.html", data)


def tenderNotices(request):
    tnot = TenderNotice.objects.all().order_by('-id')
    abtfooter = AboutUs.objects.all()
    data = {
        'tnot': tnot,
        'abtfooter': abtfooter,
    }
    return render(request, "tender-notices.html", data)


def hrNotices(request):
    hnot = HrNotice.objects.all().order_by('-id')
    abtfooter = AboutUs.objects.all()
    data = {
    'hnot': hnot,
    'abtfooter': abtfooter,
    }
    return render(request, "hr-notices.html", data)


def pressRelease(request):
    prel = PressRelease.objects.all().order_by('-id')
    abtfooter = AboutUs.objects.all()
    data = {
        'prel': prel,
        'abtfooter': abtfooter,
    }
    return render(request, "press-release.html", data)
