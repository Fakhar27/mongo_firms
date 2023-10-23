from bson import ObjectId
from django.shortcuts import render, redirect,get_object_or_404
from db_connection import db  
from django.contrib import messages
from datetime import datetime
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.templatetags.static import static
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from pymongo import MongoClient
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse
from db_connection import authenticate_user
from db_connection import users_collection
from django.contrib.auth import login as auth_login


def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password != password2:
            messages.error(request,'PASSWORDS DO NOT MATCH! MAKE SURE THEY ARE SAME!')
        else:
            user_data = {
                'username': username,
                'password': password,
            }
            db['user_registerations'].insert_one(user_data)
            return redirect('login')
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate_user(username, password)
        if user:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            messages.error(request, 'PLEASE ENTER CORRECT USERNAME OR PASSWORD')
            return render(request, 'login.html')
    return render(request, 'login.html')

@login_required
def dashboard(request):
    firm_data = list(db['firm_registrations'].find()) 
    active_firms_count = db['firm_registrations'].count_documents({'status': 'ACTIVE'})
    inactive_firms_count = db['firm_registrations'].count_documents({'status': 'INACTIVE'})
    return render(request, 'dashboard.html',{'firm_data':firm_data,'active_firms_count': active_firms_count,
    'inactive_firms_count': inactive_firms_count})
    
@login_required
def dashboard_register(request):
    if request.method == 'POST':
        record_id = ObjectId() 
        firmname = request.POST['firmname']
        firmest = request.POST['firm_est']
        NTN = request.POST['NTN']
        STRN = request.POST['STRN']
        Sponser = request.POST['Sponser']
        category = request.POST['category']
        reason = request.POST['reason']
        fromdate_str = request.POST['fromdate']
        todate_str = request.POST['todate']
        ownername = request.POST['ownername']
        ownercnic = request.POST['ownercnic']
        landlinenumber = request.POST['landlinenumber']
        phonenumber = request.POST['phonenumber']
        owneremail = request.POST['owneremail']
        websiteurl = request.POST['websiteurl']
        address = request.POST['address']
        BAN = request.POST['BAN']
        uploadfile = request.FILES.get('uploadfile')
        status = request.POST.get('status')
    
        if uploadfile:
            fs = FileSystemStorage()
            filename = fs.save(uploadfile.name, uploadfile)
            file_url = fs.url(filename)
        else:
            file_url = None
        
        fromdate = datetime.strptime(fromdate_str, '%Y-%m-%d')
        todate = datetime.strptime(todate_str, '%Y-%m-%d')
        
        if uploadfile:
            fs = FileSystemStorage()
            filename = fs.save(uploadfile.name, uploadfile)

        firmdata = {
            'record_id': record_id,
            'record_id_str': str(record_id), 
            'firmname': firmname,
            'firmest': firmest,
            'NTN': NTN,
            'STRN': STRN,
            'Sponser': Sponser,
            'category': category,
            'reason': reason,
            'fromdate': fromdate,
            'todate': todate,
            'ownername': ownername,
            'ownercnic': ownercnic,
            'landlinenumber': landlinenumber,
            'phonenumber': phonenumber,
            'owneremail': owneremail,
            'websiteurl': websiteurl,
            'address': address,
            'BAN': BAN,
            'uploadfile': filename if uploadfile else None,  
            'status': status,
        }
        db['firm_registrations'].insert_one(firmdata)
        return redirect('dashboard_register')
    return render(request, 'dashboard_register.html')

@login_required
def dashboard_view(request):
    firm_data = list(db['firm_registrations'].find())  
    firm_data_with_str_id = [{'record_id_str': str(record['_id']), **record} for record in firm_data]
    return render(request, 'dashboard_view.html', {'firm_data': firm_data_with_str_id})

@login_required
def view_firmdata(request, record_id_str):
    record = db['firm_registrations'].find_one({'record_id_str': record_id_str})
    image_filename = record.get('uploadfile', None)
    image_path_or_url = None
    if image_filename:
        media_url = settings.MEDIA_URL
        image_url = f"{media_url}{image_filename}"
        image_path_or_url = request.build_absolute_uri(image_url)
    return render(request, 'view_firmdata.html', {'record': record, 'image_path_or_url': image_path_or_url})

@login_required
def profile(request):
    # Get the currently authenticated user
    user = request.user
    
    # Retrieve user data based on the username
    user_data = users_collection.find_one({'username': user.username})
    
    if user_data:
        return render(request, 'profile.html', {'user_data': user_data})
    else:
        return redirect('login')
  
@login_required  
def delete_firmdata(request, record_id_str):
    db['firm_registrations'].delete_one({'record_id_str': record_id_str})
    return redirect('dashboard_view')

@login_required
def update_firmdata(request, record_id_str):
    
    record = db['firm_registrations'].find_one({'record_id_str': record_id_str})
    image_filename = record.get('uploadfile', None)
    image_path_or_url = None
    if image_filename:
        media_url = settings.MEDIA_URL
        image_url = f"{media_url}{image_filename}"
        image_path_or_url = request.build_absolute_uri(image_url)
            
    if request.method == 'POST':
        record_id = ObjectId() 
        firmname = request.POST['firmname']
        firmest = request.POST['firm_est']
        NTN = request.POST['NTN']
        STRN = request.POST['STRN']
        Sponser = request.POST['Sponser']
        category = request.POST['category']
        reason = request.POST['reason']
        fromdate_str = request.POST['fromdate']
        todate_str = request.POST['todate']
        ownername = request.POST['ownername']
        ownercnic = request.POST['ownercnic']
        landlinenumber = request.POST['landlinenumber']
        phonenumber = request.POST['phonenumber']
        owneremail = request.POST['owneremail']
        websiteurl = request.POST['websiteurl']
        address = request.POST['address']
        BAN = request.POST['BAN']
        uploadfile = request.FILES.get('uploadfile')
        status = request.POST.get('status')
    
        if uploadfile:
            fs = FileSystemStorage()
            filename = fs.save(uploadfile.name, uploadfile)
            file_url = fs.url(filename)
        else:
            file_url = None
        
        fromdate = datetime.strptime(fromdate_str, '%Y-%m-%d')
        todate = datetime.strptime(todate_str, '%Y-%m-%d')
        
        if uploadfile:
            fs = FileSystemStorage()
            filename = fs.save(uploadfile.name, uploadfile)

        db['firm_registrations'].update_one(
            {'record_id_str': record_id_str},
            {
                '$set': {
                    'record_id': record_id,
                    'record_id_str': str(record_id), 
                    'firmname': firmname,
                    'firmest': firmest,
                    'NTN': NTN,
                    'STRN': STRN,
                    'Sponser': Sponser,
                    'category': category,
                    'reason': reason,
                    'fromdate': fromdate,
                    'todate': todate,
                    'ownername': ownername,
                    'ownercnic': ownercnic,
                    'landlinenumber': landlinenumber,
                    'phonenumber': phonenumber,
                    'owneremail': owneremail,
                    'websiteurl': websiteurl,
                    'address': address,
                    'BAN': BAN,
                    'uploadfile': filename if uploadfile else None,  
                    'status': status,
                }
            }
        )
        return redirect('dashboard_view')
    return render(request, 'dashboard_update.html', {'record': record,'image_path_or_url': image_path_or_url})

def logout_view(request):
    logout(request)
    return redirect('login')



# def dashboard_view(request):
#     firm_data = list(db['firm_registrations'].find())  
#     firm_data_with_ids = [{'_id': str(record['_id']), **record} for record in firm_data]
#     return render(request, 'dashboard_view.html', {'firm_data': firm_data_with_ids})

# from django.shortcuts import render
# from .models import User
# from django.http import HttpResponse
# from .models import User
# from django.shortcuts import render,redirect
# from db_connection import db

# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user_data = {
#             'username':username,
#             'password':password
#         }
#         db['user'].insert_one(user_data)
#         # user = User(username=username,password=password)
#         # user.save()
#         return redirect('login.html')
#     return render(request, 'register.html')


# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         try:
#             user = db['user'].find_one({
#                 'username':username,
#                 'password':password
#                 })
#             return redirect('dashboard')
#         except:
#             pass
#         # try:
#         #     user = User.objects.get(username=username,password=password)
#         #     return redirect('dashboard')
#         # except User.DoesNotExist:
#         #     pass
#     return render(request,'login.html')
            
# def dashboard(request):
#     user = db['user'].find()
#     return HttpResponse(user)
    
# def index(request):
#     return HttpResponse("<h1>APP IS RUNNING</h1>")

# def add_person(request):
#     records = {
#         "first_name":"Hamza",
#         "last_name":"Shahid"
#     }
#     person_collection.insert_one(records)
#     return HttpResponse("NEW PERSON IS ADDED")

# def get_persons(request):
#     persons = person_collection.find()
#     return HttpResponse(persons)