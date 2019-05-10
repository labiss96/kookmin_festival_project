"""festival_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
import festivalapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', festivalapp.views.home, name='home'),
    path('fest/<int:fest_id>', festivalapp.views.detail, name="detail"),
    path('fest/lost', festivalapp.views.lost, name="lost"),
    path('fest/talk', festivalapp.views.talk, name="talk"),
    path('fest/new', festivalapp.views.new, name="new"),

    path('fest/create', festivalapp.views.create, name="create"),
    path('delete/<int:delete_fest_id>', festivalapp.views.delete, name='delete'),
    path('edit/<int:edit_fest_id>', festivalapp.views.edit, name='edit'),
    path('update/<int:update_fest_id>', festivalapp.views.update, name='update'),
    
]
