from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from app.views import home, post_tweet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    path('post_tweet/',post_tweet,name='post_tweet'),
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),

]

