from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/CustomerProfilePic/',blank=True)
    email = models.EmailField(max_length=40,blank=False)
    mobile = models.CharField(max_length=20,blank=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name

class Feedback(models.Model):
    name=models.CharField(max_length=40)
    feedback=models.CharField(max_length=500)
    date= models.DateField(auto_now_add=True,blank=False)
    def __str__(self):
        return self.name

class Location2CameraDashboard(models.Model):
    nvr_dvr=models.CharField(max_length=50,blank=True)
    location=models.CharField(max_length=50, blank=True)
    sum_total_days_rec=models.CharField(max_length=50,blank=True)
    sum_of_baseline_days_rec=models.CharField(max_length=50,blank=True)
    sum_of_storage_warning=models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.nvr_dvr
class Location2RowLabel(models.Model):
    row_labels=models.CharField(max_length=100,null=True)
    sum_of_no_of_channels=models.CharField(max_length=20)
    sum_of_total_cameras=models.CharField(max_length=20)

    def __str__(self):
        return self.row_labels


class Location1CameraDashboard(models.Model):
    nvr_dvr=models.CharField(max_length=50,blank=True)
    location=models.CharField(max_length=50, blank=True)
    sum_total_days_rec=models.CharField(max_length=50,blank=True)
    sum_of_baseline_days_rec=models.CharField(max_length=50,blank=True)
    sum_of_storage_warning=models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.nvr_dvr
class Location1RowLabel(models.Model):
    row_labels=models.CharField(max_length=100,null=True)
    sum_of_no_of_channels=models.CharField(max_length=20)
    sum_of_total_cameras=models.CharField(max_length=20)

    def __str__(self):
        return self.row_labels
class Location3CameraDashboard(models.Model):
    nvr_dvr=models.CharField(max_length=50,blank=True)
    location=models.CharField(max_length=50, blank=True)
    sum_total_days_rec=models.CharField(max_length=50,blank=True)
    sum_of_baseline_days_rec=models.CharField(max_length=50,blank=True)
    sum_of_storage_warning=models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.nvr_dvr
class Location3RowLabel(models.Model):
    row_labels=models.CharField(max_length=100,null=True)
    sum_of_no_of_channels=models.CharField(max_length=20)
    sum_of_total_cameras=models.CharField(max_length=20)

    def __str__(self):
        return self.row_labels
class Location4CameraDashboard(models.Model):
    nvr_dvr=models.CharField(max_length=50,blank=True)
    location=models.CharField(max_length=50, blank=True)
    sum_total_days_rec=models.CharField(max_length=50,blank=True)
    sum_of_baseline_days_rec=models.CharField(max_length=50,blank=True)
    sum_of_storage_warning=models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.nvr_dvr
class Location4RowLabel(models.Model):
    row_labels=models.CharField(max_length=100,null=True)
    sum_of_no_of_channels=models.CharField(max_length=20)
    sum_of_total_cameras=models.CharField(max_length=20)

    def __str__(self):
        return self.row_labels
class Location5CameraDashboard(models.Model):
    nvr_dvr=models.CharField(max_length=50,blank=True)
    location=models.CharField(max_length=50, blank=True)
    sum_total_days_rec=models.CharField(max_length=50,blank=True)
    sum_of_baseline_days_rec=models.CharField(max_length=50,blank=True)
    sum_of_storage_warning=models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.nvr_dvr
class Location5RowLabel(models.Model):
    row_labels=models.CharField(max_length=100,null=True)
    sum_of_no_of_channels=models.CharField(max_length=20)
    sum_of_total_cameras=models.CharField(max_length=20)

    def __str__(self):
        return self.row_labels
class Location6CameraDashboard(models.Model):
    nvr_dvr=models.CharField(max_length=50,blank=True)
    location=models.CharField(max_length=50, blank=True)
    sum_total_days_rec=models.CharField(max_length=50,blank=True)
    sum_of_baseline_days_rec=models.CharField(max_length=50,blank=True)
    sum_of_storage_warning=models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.nvr_dvr
class Location6RowLabel(models.Model):
    row_labels=models.CharField(max_length=100,null=True)
    sum_of_no_of_channels=models.CharField(max_length=20)
    sum_of_total_cameras=models.CharField(max_length=20)

    def __str__(self):
        return self.row_labels
