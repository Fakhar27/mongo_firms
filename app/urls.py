from django.urls import path,include
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.contrib.auth import logout


urlpatterns = [
    path('',views.home, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/',views.register, name='register'),
    path('login/',views.login, name='login'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('dashboard_register/',views.dashboard_register,name='dashboard_register'),
    path('dashboard_view/',views.dashboard_view,name="dashboard_view"),
    path('view_firmdata/<str:record_id_str>/', views.view_firmdata, name='view_firmdata'),
    path('profile/',views.profile,name="profile"),
    path('delete_firmdata/<str:record_id_str>/', views.delete_firmdata, name='delete_firmdata'),
    path('dashboard_update/<str:record_id_str>/', views.update_firmdata, name='dashboard_update'),
    path('logout/', views.logout_view, name='logout'),
]
    
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
    