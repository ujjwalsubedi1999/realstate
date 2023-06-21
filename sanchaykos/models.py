from distutils.command.upload import upload
import email
from pyexpat import model
from django.db import models


# Create your models here.

    # def __str__(self):
    #     return "%s %s" % (self.first_name, self.last_name)


class CompanyContacts(models.Model):
    email = models.EmailField(max_length=50, null=True,blank=True)
    phone = models.CharField(max_length=100,blank=True,null=True)
    address = models.CharField(max_length=100,blank=True,null=True)
    city = models.CharField(max_length=100,blank=True,null=True)
    facebook = models.CharField(max_length=200,blank=True,null=True)
    instagram = models.CharField(max_length=200,blank=True,null=True)
    twitter = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return ('Company Contacts')
    

class Contacts(models.Model):
    name = models.CharField(max_length=50, null=True)
    email  = models.EmailField(max_length=50, null=True)
    phone = models.CharField(null=True,max_length=15)
    message = models.TextField(null=True)

    def __str__(self):
        return self.name

class Chairman(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(null=True)
    detailed_description = models.TextField(null=True)   
    image = models.ImageField(upload_to='static',null=True)

    def __str__(self):
        return self.name




class Abstract(models.Model):
    title1 = models.CharField(max_length=20)
    desc1 = models.TextField()
    title2 = models.CharField(max_length=20)
    desc2 = models.TextField()
    title3 = models.CharField(max_length=20)
    desc3 = models.TextField()
    title4 = models.CharField(max_length=20)
    desc4 = models.TextField()




# class Properties(models.Model):
#     title1 = models.CharField(max_length=25,null=True)
#     location1 = models.CharField(max_length=40,null=True)
#     pic1 = models.ImageField(upload_to='static/propertiesimg',null=True)
#     title2 = models.CharField(max_length=25,null=True)
#     location2 = models.CharField(max_length=40,null=True)
#     pic2 = models.ImageField(upload_to='static/propertiesimg',null=True)
#     title3 = models.CharField(max_length=25,null=True)
#     location3 = models.CharField(max_length=40,null=True)
#     pic3 = models.ImageField(upload_to='static/propertiesimg',null=True)



class Slider(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    desc = models.TextField(null=True)
    image = models.ImageField(upload_to='static/sliderimg',null=True)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    




class Newsletter(models.Model):
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.email
        




class Board(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    img = models.ImageField(upload_to='static/boardimg')
    
    def __str__(self):
        return self.name


#foreign key concept

class Projects(models.Model):
    name = models.CharField(max_length=25,null=True)
    location = models.CharField(max_length=40,null=True)
    image = models.ImageField(upload_to='static/projectsimg',null=True, blank=True)

    def __str__(self):
        return self.name

class ProjectsImage(models.Model):
    projectimg = models.ForeignKey(Projects, null=True , on_delete=models.CASCADE)
    images = models.ImageField(upload_to='static/projectsimg',null=True, blank=True)

    def __str__(self):
        return self.projectimg.name




class CompanyNews(models.Model):
    title = models.CharField(max_length=250,null=True)
    description = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='static/companynewsfile',null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class GeneralNotice(models.Model):
    title = models.CharField(max_length=250,null=True)
    description = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='static/generalnoticefile',null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class TenderNotice(models.Model):
    title = models.CharField(max_length=250,null=True)
    description = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='static/tendernoticefile',null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class HrNotice(models.Model):
    title = models.CharField(max_length=250,null=True)
    description = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='static/hrnoticefile',null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class PressRelease(models.Model):
    title = models.CharField(max_length=250,null=True)
    description = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='static/pressreleasefile',null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title



class AboutUs(models.Model):
    footer_about = models.TextField(null=True,blank=True)
    content = models.TextField(null=True,blank=True)


class Vision(models.Model):
    content = models.TextField(null=True,blank=True)


class CoreValues(models.Model):
    content = models.TextField(null=True,blank=True)


class OurTeam(models.Model):
    content = models.TextField(null=True,blank=True)


