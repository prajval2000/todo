from django.urls import path
from . import views

urlpatterns = [
    path("addTask/", views.addTask, name='addTask'),
    path("deleteTask/<int:pk>", views.deleteTask, name='deleteTask'),
    path('mark_as_done/<int:pk>', views.markAsDone, name='mark_as_done'),
    path('mark_as_undone/<int:pk>', views.markAsUndone, name='mark_as_undone'),
    path('edit_task/<int:pk>', views.editTask, name='edit_task'),


]
