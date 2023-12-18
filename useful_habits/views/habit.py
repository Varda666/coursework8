
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

from useful_habits.models import Habit
from useful_habits.permissions import IsModerator, IsOwner, IsOwnerOrPublic
from useful_habits.serializers.habit import HabitSerializer
from useful_habits.tasks import _send_mail_email


class HabitCreateView(CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]




class HabitUpdateView(UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsModerator | IsOwner]



class HabitRetrieveView(RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsModerator | IsOwner | IsOwnerOrPublic]

class HabitDestroyView(DestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwner | IsModerator]


class HabitListView(ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsModerator | IsOwner | IsOwnerOrPublic]