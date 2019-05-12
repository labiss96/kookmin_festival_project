from django.contrib import admin
from django.urls import path
import festivalapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', festivalapp.views.home, name='home'),

    path('fest/<int:fest_id>', festivalapp.views.detail, name="detail"),
    path('fest_lost/<int:lost_id>', festivalapp.views.detail_lost, name="detail_lost"),

    path('fest/lost', festivalapp.views.lost, name="lost"),
    path('fest/talk', festivalapp.views.talk, name="talk"),

    path('fest/new', festivalapp.views.new, name="new"),
    path('fest/new_lost', festivalapp.views.new_lost, name="new_lost"),

    path('fest/create', festivalapp.views.create, name="create"),
    path('fest/create_lost', festivalapp.views.create_lost, name="create_lost"),

    path('delete/<int:delete_fest_id>', festivalapp.views.delete, name='delete'),
    path('edit/<int:edit_fest_id>', festivalapp.views.edit, name='edit'),
    path('update/<int:update_fest_id>', festivalapp.views.update, name='update'),
    
    path('delete_lost/<int:delete_lost_id>', festivalapp.views.delete_lost, name='delete_lost'),
    path('edit_lost/<int:edit_lost_id>', festivalapp.views.edit_lost, name='edit_lost'),
    path('update_lost/<int:update_lost_id>', festivalapp.views.update_lost, name='update_lost'),


    path('schedule/', festivalapp.views.schedule, name="schedule"),
    
]
