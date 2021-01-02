from django.contrib import admin
from .models import Customer,Feedback,Location1RowLabel,Location2RowLabel,Location3RowLabel,Location4RowLabel,Location5RowLabel,Location6RowLabel
from .models import Location1CameraDashboard,Location2CameraDashboard,Location3CameraDashboard,Location4CameraDashboard,Location5CameraDashboard,Location6CameraDashboard
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.contrib.auth.models import Group,User
from django.contrib.admin import AdminSite



# Register your models here.
admin.site.site_header ="Admin Dashboard"
#admin.site.unregister(User)
admin.site.register(Feedback)
class UserSort(ImportExportModelAdmin):
    list_display = ('user','mobile','email')
    ordering=["id"]
admin.site.register(Customer,UserSort)



class SnipetAdmin(ImportExportModelAdmin):
    list_display=('nvr_dvr','location','sum_total_days_rec','sum_of_baseline_days_rec','sum_of_storage_warning')
    ordering = ['id']
    pass
admin.site.register(Location2CameraDashboard,SnipetAdmin)

class BangaloreSnipetAdmin(ImportExportModelAdmin):
    list_display=('nvr_dvr','location','sum_total_days_rec','sum_of_baseline_days_rec','sum_of_storage_warning')
    ordering = ['id']
    pass
admin.site.register(Location1CameraDashboard,BangaloreSnipetAdmin)



#admin.site.register(CameraDashboard,ViewAdmin)
class RowAdmin(ImportExportModelAdmin):
    list_display=('row_labels','sum_of_no_of_channels','sum_of_total_cameras')
    ordering = ['id']
    pass
admin.site.register(Location2RowLabel,RowAdmin)
class BangaloreRowAdmin(ImportExportModelAdmin):
    list_display=('row_labels','sum_of_no_of_channels','sum_of_total_cameras')
    ordering = ['id']
    pass
admin.site.register(Location1RowLabel,BangaloreRowAdmin)

######################################################
class Snipet1Admin(ImportExportModelAdmin):
    list_display=('nvr_dvr','location','sum_total_days_rec','sum_of_baseline_days_rec','sum_of_storage_warning')
    ordering = ['id']
    pass
admin.site.register(Location3CameraDashboard,Snipet1Admin)
class Snipet2Admin(ImportExportModelAdmin):
    list_display=('nvr_dvr','location','sum_total_days_rec','sum_of_baseline_days_rec','sum_of_storage_warning')
    ordering = ['id']
    pass
admin.site.register(Location4CameraDashboard,Snipet2Admin)
class Snipet3Admin(ImportExportModelAdmin):
    list_display=('nvr_dvr','location','sum_total_days_rec','sum_of_baseline_days_rec','sum_of_storage_warning')
    ordering = ['id']
    pass
admin.site.register(Location5CameraDashboard,Snipet3Admin)
class Snipet4Admin(ImportExportModelAdmin):
    list_display=('nvr_dvr','location','sum_total_days_rec','sum_of_baseline_days_rec','sum_of_storage_warning')
    ordering = ['id']
    pass
admin.site.register(Location6CameraDashboard,Snipet4Admin)
###_-------------------------------------------------------------------------################
class Row1Admin(ImportExportModelAdmin):
    list_display=('row_labels','sum_of_no_of_channels','sum_of_total_cameras')
    ordering = ['id']
    pass
admin.site.register(Location3RowLabel,Row1Admin)
class Row2Admin(ImportExportModelAdmin):
    list_display=('row_labels','sum_of_no_of_channels','sum_of_total_cameras')
    ordering = ['id']
    pass
admin.site.register(Location4RowLabel,Row2Admin)
class Row3Admin(ImportExportModelAdmin):
    list_display=('row_labels','sum_of_no_of_channels','sum_of_total_cameras')
    ordering = ['id']
    pass
admin.site.register(Location5RowLabel,Row3Admin)
class Row4Admin(ImportExportModelAdmin):
    list_display=('row_labels','sum_of_no_of_channels','sum_of_total_cameras')
    ordering = ['id']
    pass
admin.site.register(Location6RowLabel,Row4Admin)
#####################################################################################################
