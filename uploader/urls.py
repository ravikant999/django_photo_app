'''from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_view, name='upload'),
    path('display/', views.display_view, name='display'),
]
'''


from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('upload/', views.upload_view, name='upload'),
    path('display/', views.display_view, name='display'),
    path('edit/<int:pk>/', views.edit_upload, name='edit'),
    path('delete/<int:pk>/', views.delete_upload, name='delete'),
]
