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
    path('like/<int:upload_id>/', views.like_upload, name='like_upload'),
    path('comment/<int:upload_id>/', views.add_comment, name='add_comment'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),

]
