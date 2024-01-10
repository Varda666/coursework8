from django.db.models import QuerySet
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

from useful_habits.models import Habit
from useful_habits.permissions import IsModerator, IsOwnerOrPublic, IsOwner
from useful_habits.serializers.habit import HabitSerializer
from useful_habits.tasks import send_message_telegram


class HabitCreateView(CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]


class HabitUpdateView(UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class HabitRetrieveView(RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner | IsOwnerOrPublic]

class HabitDestroyView(DestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]


class HabitListView(ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class PublicHabitListView(ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrPublic]

    # def get_queryset(self):
    #     queryset = self.queryset
    #     if isinstance(queryset, QuerySet):
    #         # Ensure queryset is re-evaluated on each request.
    #         queryset = queryset.all()
    #         # for query in queryset:
    #         #     action = query['action']
    #         #     place = query['place']
    #         #     time = query['time']
    #         #     text = 'Не забудьте' + "\n" + str(action) + "\n" + str(place) + "\n" + time
    #         #     send_message_telegram(text=text)
    #     return queryset

