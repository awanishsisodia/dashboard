from . import forms,models
import pandas as pd
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response

def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'db/index.html')


#for showing login button for admin
def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return HttpResponseRedirect('adminlogin')


def customer_signup_view(request):
    userForm=forms.CustomerUserForm()
    customerForm=forms.CustomerForm()
    mydict={'userForm':userForm,'customerForm':customerForm}
    if request.method=='POST':
        userForm=forms.CustomerUserForm(request.POST)
        customerForm=forms.CustomerForm(request.POST,request.FILES)
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            customer=customerForm.save(commit=False)
            customer.user=user
            customer.save()
            my_customer_group = Group.objects.get_or_create(name='NEW_USER')
            my_customer_group[0].user_set.add(user)
        return HttpResponseRedirect('customerlogin')
    return render(request,'db/customersignup.html',context=mydict)
###############################################################################################
#-----------for checking user iscustomer
def is_customer(user):
    return user.groups.filter(name='LOCATION2').exists()
def is_cust1(user):
    return user.groups.filter(name='LOCATION1').exists()
def is_location3(user):
    return user.groups.filter(name='LOCATION3').exists()
def is_location4(user):
    return user.groups.filter(name='LOCATION4').exists()
def is_location5(user):
    return user.groups.filter(name='LOCATION5').exists()
def is_location6(user):
    return user.groups.filter(name='LOCATION6').exists()
def is_newuser(user):
    return user.groups.filter(name="NEW_USER").exists()
#---------AFTER ENTERING CREDENTIALS WE CHECK WHETHER USERNAME AND PASSWORD IS OF which Group
def afterlogin_view(request):
    if is_customer(request.user):
        return redirect('/customer-home')
    elif is_cust1(request.user):
        return redirect('/cust-home')
    elif is_location3(request.user):
        return redirect('/loc-three')
    elif is_location4(request.user):
        return redirect('/loc-four')
    elif is_location5(request.user):
        return redirect('/loc-five')
    elif is_location6(request.user):
        return redirect('/loc-six')
    elif is_newuser(request.user):
        return redirect('/new-user')
    else:
        return redirect('/admin')

############################## NEW USER VIEWS ############################################################
@login_required(login_url='customerlogin')
@user_passes_test(is_newuser)
def new_user(request):
    return render(request,'db/new_user.html')

@login_required(login_url='customerlogin')
@user_passes_test(is_newuser)
def wait(request):
    return render(request,'db/wait.html')

##################################  LOCATION 3 VIEWS  ########################################################
@login_required(login_url='customerlogin')
@user_passes_test(is_location3)
def location3(request):
    return render(request,'db/location3.html')


@login_required(login_url='customerlogin')
@user_passes_test(is_location3)
def location3cameradashveiw(request):
    cameradash=models.Location3CameraDashboard.objects.all()
    rowlabel=models.Location3RowLabel.objects.all()

    labels = []
    DefaultData = []
    DefaultData1=[]
    DefaultData2=[]

    for item in cameradash:
        labels.append(item.location)
        DefaultData.append(item.sum_total_days_rec)
        DefaultData1.append(item.sum_of_baseline_days_rec)
        DefaultData2.append(item.sum_of_storage_warning)

    labels_r =[]
    DefaultData_r=[]
    DefaultData_r_1=[]
    for item in rowlabel:
        labels_r.append(item.row_labels)
        DefaultData_r.append(item.sum_of_no_of_channels)
        DefaultData_r_1.append(item.sum_of_total_cameras)

    return render(request,'db/location3cameradash.html',{'cameradash':cameradash,'rowlabel':rowlabel,'labels':labels,'DefaultData':DefaultData,'DefaultData1':DefaultData1,'DefaultData2':DefaultData2,'labels_r':labels_r,'DefaultData_r':DefaultData_r,'DefaultData_r_1':DefaultData_r_1})
##################################  LOCATION 4 VIEWS  ########################################################
@login_required(login_url='customerlogin')
@user_passes_test(is_location4)
def location4(request):
    return render(request,'db/location4.html')


@login_required(login_url='customerlogin')
@user_passes_test(is_location4)
def location4cameradashveiw(request):
    cameradash=models.Location4CameraDashboard.objects.all()
    rowlabel=models.Location4RowLabel.objects.all()

    labels = []
    DefaultData = []
    DefaultData1=[]
    DefaultData2=[]

    for item in cameradash:
        labels.append(item.location)
        DefaultData.append(item.sum_total_days_rec)
        DefaultData1.append(item.sum_of_baseline_days_rec)
        DefaultData2.append(item.sum_of_storage_warning)

    labels_r =[]
    DefaultData_r=[]
    DefaultData_r_1=[]
    for item in rowlabel:
        labels_r.append(item.row_labels)
        DefaultData_r.append(item.sum_of_no_of_channels)
        DefaultData_r_1.append(item.sum_of_total_cameras)

    return render(request,'db/location4cameradash.html',{'cameradash':cameradash,'rowlabel':rowlabel,'labels':labels,'DefaultData':DefaultData,'DefaultData1':DefaultData1,'DefaultData2':DefaultData2,'labels_r':labels_r,'DefaultData_r':DefaultData_r,'DefaultData_r_1':DefaultData_r_1})
##################################  LOCATION 5 VIEWS  ########################################################
@login_required(login_url='customerlogin')
@user_passes_test(is_location5)
def location5(request):
    return render(request,'db/location5.html')
@login_required(login_url='customerlogin')
@user_passes_test(is_location5)
def location5cameradashveiw(request):
    cameradash=models.Location5CameraDashboard.objects.all()
    rowlabel=models.Location5RowLabel.objects.all()

    labels = []
    DefaultData = []
    DefaultData1=[]
    DefaultData2=[]

    for item in cameradash:
        labels.append(item.location)
        DefaultData.append(item.sum_total_days_rec)
        DefaultData1.append(item.sum_of_baseline_days_rec)
        DefaultData2.append(item.sum_of_storage_warning)

    labels_r =[]
    DefaultData_r=[]
    DefaultData_r_1=[]
    for item in rowlabel:
        labels_r.append(item.row_labels)
        DefaultData_r.append(item.sum_of_no_of_channels)
        DefaultData_r_1.append(item.sum_of_total_cameras)

    return render(request,'db/location5cameradash.html',{'cameradash':cameradash,'rowlabel':rowlabel,'labels':labels,'DefaultData':DefaultData,'DefaultData1':DefaultData1,'DefaultData2':DefaultData2,'labels_r':labels_r,'DefaultData_r':DefaultData_r,'DefaultData_r_1':DefaultData_r_1})
##################################  LOCATION 6 VIEWS  ########################################################
@login_required(login_url='customerlogin')
@user_passes_test(is_location6)
def location6(request):
    return render(request,'db/location6.html')
@login_required(login_url='customerlogin')
@user_passes_test(is_location6)
def location6cameradashveiw(request):
    cameradash=models.Location6CameraDashboard.objects.all()
    rowlabel=models.Location6RowLabel.objects.all()

    labels = []
    DefaultData = []
    DefaultData1=[]
    DefaultData2=[]

    for item in cameradash:
        labels.append(item.location)
        DefaultData.append(item.sum_total_days_rec)
        DefaultData1.append(item.sum_of_baseline_days_rec)
        DefaultData2.append(item.sum_of_storage_warning)

    labels_r =[]
    DefaultData_r=[]
    DefaultData_r_1=[]
    for item in rowlabel:
        labels_r.append(item.row_labels)
        DefaultData_r.append(item.sum_of_no_of_channels)
        DefaultData_r_1.append(item.sum_of_total_cameras)

    return render(request,'db/location6cameradash.html',{'cameradash':cameradash,'rowlabel':rowlabel,'labels':labels,'DefaultData':DefaultData,'DefaultData1':DefaultData1,'DefaultData2':DefaultData2,'labels_r':labels_r,'DefaultData_r':DefaultData_r,'DefaultData_r_1':DefaultData_r_1})

@login_required(login_url='customerlogin')
@user_passes_test(is_cust1)
def cust_home_view(request):
    return render(request,'db/cust_home.html')

#---------------------------------------------------------------------------------
#------------------------ ADMIN RELATED VIEWS START ------------------------------
#---------------------------------------------------------------------------------
@login_required(login_url='adminlogin')
def admin_dashboard_view(request):
    # for cards on dashboard
    customercount=models.Customer.objects.all().count()
    mydict={
    'customercount':customercount,

    }
    return render(request,'db/admin_dashboard.html',context=mydict)



# admin view customer table
@login_required(login_url='adminlogin')
def view_customer_view(request):
    customers=models.Customer.objects.all()
    return render(request,'db/view_customer.html',{'customers':customers})

# admin delete customer
@login_required(login_url='adminlogin')
def delete_customer_view(request,pk):
    customer=models.Customer.objects.get(id=pk)
    user=models.User.objects.get(id=customer.user_id)
    user.delete()
    customer.delete()
    return redirect('view-customer')


@login_required(login_url='adminlogin')
def update_customer_view(request,pk):
    customer=models.Customer.objects.get(id=pk)
    user=models.User.objects.get(id=customer.user_id)
    userForm=forms.CustomerUserForm(instance=user)
    customerForm=forms.CustomerForm(request.FILES,instance=customer)
    mydict={'userForm':userForm,'customerForm':customerForm}
    if request.method=='POST':
        userForm=forms.CustomerUserForm(request.POST,instance=user)
        customerForm=forms.CustomerForm(request.POST,instance=customer)
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            customerForm.save()
            return redirect('view-customer')
    return render(request,'db/admin_update_customer.html',context=mydict)




# admin view the feedback
@login_required(login_url='adminlogin')
def view_feedback_view(request):
    feedbacks=models.Feedback.objects.all().order_by('-id')
    return render(request,'db/view_feedback.html',{'feedbacks':feedbacks})



#---------------------------------------------------------------------------------
#------------------------ PUBLIC CUSTOMER RELATED VIEWS START ---------------------

def send_feedback_view(request):
    feedbackForm=forms.FeedbackForm()
    if request.method == 'POST':
        feedbackForm = forms.FeedbackForm(request.POST)
        if feedbackForm.is_valid():
            feedbackForm.save()
            return render(request, 'db/feedback_sent.html')
    return render(request, 'db/send_feedback.html', {'feedbackForm':feedbackForm})


#---------------------------------------------------------------------------------
#------------------------ CUSTOMER RELATED VIEWS START ------------------------------
#---------------------------------------------------------------------------------
@login_required(login_url='customerlogin')

def customer_home_view(request):
    return render(request,'db/customer_home.html')




@login_required(login_url='customerlogin')

def my_profile_view(request):
    customer=models.Customer.objects.get(user_id=request.user.id)
    return render(request,'db/my_profile.html',{'customer':customer})


@login_required(login_url='customerlogin')

def edit_profile_view(request):
    customer=models.Customer.objects.get(user_id=request.user.id)
    user=models.User.objects.get(id=customer.user_id)
    userForm=forms.CustomerUserForm(instance=user)
    customerForm=forms.CustomerForm(request.FILES,instance=customer)
    mydict={'userForm':userForm,'customerForm':customerForm}
    if request.method=='POST':
        userForm=forms.CustomerUserForm(request.POST,instance=user)
        customerForm=forms.CustomerForm(request.POST,instance=customer)
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            customerForm.save()
            return HttpResponseRedirect('my-profile')
    return render(request,'db/edit_profile.html',context=mydict)

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def cameradashveiw(request):
    cameradash=models.Location2CameraDashboard.objects.all()
    rowlabel=models.Location2RowLabel.objects.all()
    labels = []
    DefaultData = []
    DefaultData1=[]
    DefaultData2=[]

    for item in cameradash:
        labels.append(item.location)
        DefaultData.append(item.sum_total_days_rec)
        DefaultData1.append(item.sum_of_baseline_days_rec)
        DefaultData2.append(item.sum_of_storage_warning)

    labels_r =[]
    DefaultData_r=[]
    DefaultData_r_1=[]
    for item in rowlabel:
        labels_r.append(item.row_labels)
        DefaultData_r.append(item.sum_of_no_of_channels)
        DefaultData_r_1.append(item.sum_of_total_cameras)

    return render(request,'db/cameradash.html',{'cameradash':cameradash,
                                               'rowlabel':rowlabel,
                                               'labels':labels,
                                               'DefaultData':DefaultData,
                                               'DefaultData1':DefaultData1,
                                               'DefaultData2':DefaultData2,
                                               'labels_r':labels_r,
                                               'DefaultData_r':DefaultData_r,
                                               'DefaultData_r_1':DefaultData_r_1})


@login_required(login_url='customerlogin')
@user_passes_test(is_cust1)
def ban_cameradashveiw(request):
    cameradash=models.Location1CameraDashboard.objects.all()
    rowlabel=models.Location1RowLabel.objects.all()

    labels = []
    DefaultData = []
    DefaultData1=[]
    DefaultData2=[]

    for item in cameradash:
        labels.append(item.location)
        DefaultData.append(item.sum_total_days_rec)
        DefaultData1.append(item.sum_of_baseline_days_rec)
        DefaultData2.append(item.sum_of_storage_warning)

    labels_r =[]
    DefaultData_r=[]
    DefaultData_r_1=[]
    for item in rowlabel:
        labels_r.append(item.row_labels)
        DefaultData_r.append(item.sum_of_no_of_channels)
        DefaultData_r_1.append(item.sum_of_total_cameras)

    return render(request,'db/bangalorecameradash.html',{'cameradash':cameradash,
                                               'rowlabel':rowlabel,
                                               'labels':labels,
                                               'DefaultData':DefaultData,
                                               'DefaultData1':DefaultData1,
                                               'DefaultData2':DefaultData2,
                                               'labels_r':labels_r,
                                               'DefaultData_r':DefaultData_r,
                                               'DefaultData_r_1':DefaultData_r_1})
