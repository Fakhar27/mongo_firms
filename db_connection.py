import pymongo
from django.contrib.auth.models import User

url = 'mongodb://51.20.118.87:27017'
client = pymongo.MongoClient(url)

db = client['NLC_TEST']

users_collection = db['user_registerations']  # Replace 'your_users_collection' with the actual name of your users collection



def authenticate_user(username, password):
    user_data = users_collection.find_one({'username': username, 'password': password})
    
    if user_data:
        # Check if the user with this username already exists in Django's User model
        user, created = User.objects.get_or_create(username=username)
        
        if created:
            # Set a password for the newly created user (this is required by Django)
            user.set_password(password)
            user.save()
        
        return user
    else:
        return None