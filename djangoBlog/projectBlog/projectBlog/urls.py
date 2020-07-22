"""projectBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from appUsers import views as user_views
from appBlog import views as blog_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appBlog.urls')),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    # classview
    path('views/', blog_views.listview.as_view(template_name='blog/blogpage.html'),name='listview'), 
    path('create/', blog_views.createview.as_view(template_name='blog/createblog.html'),name='createview'), 
    path('views/detail/<int:pk>/', blog_views.detailview.as_view(template_name='blog/blogdetail.html'),name='detailview'), 
    path('update/<int:pk>/', blog_views.updateview.as_view(template_name='blog/update.html'),name='updateview'), 
    path('update/<int:pk>/delete', blog_views.deleteview.as_view(template_name='blog/post_confirm_delete.html'),name='deleteview'), 
    path('profile/', user_views.profile, name='profile'),
    path('allblog/<str:slug>', blog_views.allblogs, name='allblog')
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)