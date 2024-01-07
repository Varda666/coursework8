from django.urls import path
# from rest_framework import routers
from django.contrib import admin

from useful_habits.views.habit import *
# from useful_habits.views.course import *
# from useful_habits.views.payment import PaymentListView, PaymentRetrieveView, PaymentUpdateView, PaymentCreateView, \
#     PaymentDestroyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HabitListView.as_view(), name='habit_list'),
    path('<int:pk>/', HabitRetrieveView.as_view(), name='habit_detail'),
    path('update/<int:pk>/', HabitUpdateView.as_view(), name='habit_update'),
    path('create/', HabitCreateView.as_view(), name='habit_create'),
    path('delete/<int:pk>/', HabitDestroyView.as_view(), name='habit_delete'),
   ]

# router = routers.SimpleRouter()
# router.register('course', CourseViewSet)
# urlpatterns += router.urls
