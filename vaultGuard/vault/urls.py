from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('', views.home, name='home'),
    path('logout/', views.user_logout, name='logout'),
    path('add_entry/', views.add_entry, name='add_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    path('generate_password/', views.generate_password, name='generate_password'),
    
    #sidebar
    path('generator/', views.generator, name='generator'),
    path('ai-assistance/', views.ai_assistance, name='ai_assistance'),
]

