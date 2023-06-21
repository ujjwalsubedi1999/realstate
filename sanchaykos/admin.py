from django.contrib import admin
from .models import *
from tinymce.widgets import TinyMCE


class TmceAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField : {'widget' : TinyMCE()},
    }

# Register your models here.


admin.site.register(Contacts,TmceAdmin)
admin.site.register(CompanyContacts,TmceAdmin)


admin.site.register(AboutUs,TmceAdmin)
admin.site.register(Chairman,TmceAdmin)
admin.site.register(Vision,TmceAdmin)
admin.site.register(CoreValues,TmceAdmin)
admin.site.register(OurTeam,TmceAdmin)

admin.site.register(Abstract,TmceAdmin)
# admin.site.register(Properties,TmceAdmin)
admin.site.register(Slider,TmceAdmin)
admin.site.register(Newsletter,TmceAdmin)
admin.site.register(Board,TmceAdmin)


# admin.site.register(Projects,TmceAdmin)
# admin.site.register(ProjectsImage,TmceAdmin)

admin.site.register(CompanyNews,TmceAdmin)
admin.site.register(GeneralNotice,TmceAdmin)
admin.site.register(TenderNotice,TmceAdmin)
admin.site.register(HrNotice,TmceAdmin)
admin.site.register(PressRelease,TmceAdmin)

class ProjectsImageAdmin(admin.StackedInline):
    model = ProjectsImage

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    inlines = [ProjectsImageAdmin]

    class Meta:
        model = Projects

@admin.register(ProjectsImage)
class ProjectsImageAdmin(admin.ModelAdmin):
    pass