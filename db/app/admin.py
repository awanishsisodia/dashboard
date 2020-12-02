from django.contrib import admin
from .models import Customer,Feedback,CameraDashboard
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.contrib.auth.models import Group


# Register your models here.
admin.site.site_header ="Admin Dashboard"
admin.site.unregister(Group)
admin.site.register(Feedback)
admin.site.register(Customer)


class SnipetAdmin(ImportExportModelAdmin):
    list_display=('nvr_dvr','location','sum_total_days_rec','sum_of_baseline_days_rec','sum_of_storage_warning')
    pass




#admin.site.register(CameraDashboard,ViewAdmin)
admin.site.register(CameraDashboard,SnipetAdmin)
