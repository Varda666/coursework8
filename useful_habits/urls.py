from django.urls import path
from django.contrib import admin

from useful_habits.views.habit import (HabitListView, PublicHabitListView,
                                       HabitRetrieveView,
                                       HabitUpdateView,
                                       HabitCreateView, HabitDestroyView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HabitListView.as_view(), name='habit_list'),
    path('public/', PublicHabitListView.as_view(), name='public_habit_list'),
    path('<int:pk>/', HabitRetrieveView.as_view(), name='habit_detail'),
    path('update/<int:pk>/', HabitUpdateView.as_view(), name='habit_update'),
    path('create/', HabitCreateView.as_view(), name='habit_create'),
    path('delete/<int:pk>/', HabitDestroyView.as_view(), name='habit_delete'),
]

