from django.urls import path
from .import views 

urlpatterns = [

    path('', views.home, name='home'),
    path('register/', views.registration_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('joblist/<int:pk>', views.joblistview, name='joblist'),
    # path('jobdetail/<int:pk>', views.jobdetailview, name='jobdetail'),

]