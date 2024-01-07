from django.urls import reverse_lazy
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.views import TokenObtainPairView


from users.models import User
from useful_habits.permissions import IsOwner
from users.serializers import UserSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def form_valid(self, form):
    #     if form.is_valid():
    #         self.object = form.save()
    #         # Сохранение объекта перед тем, как установить ему пароль
    #         self.object.set_password(form.cleaned_data['password'])
    #         form = self.object.save()
    #
    #         return super().form_valid(form)


# class UserHabitsCreateView(CreateAPIView):
#     queryset = UserHabits.objects.all()
#     serializer_class = UserHabitsSerializer


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    # def perform_update(self, serializer):
    #     if check_last_visit(pk=self.request.user):
    #         pass
    #     self.request.user.is_active = False

class UserRetrieveView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated, IsOwner]

class UserDestroyView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser | IsOwner]


# class UserHabitsDestroyView(DestroyAPIView):
#     queryset = UserHabits.objects.all()
#     serializer_class = UserHabitsSerializer
#     permission_classes = [IsAuthenticated, IsAdminUser | IsOwner]
#
#
# class UserHabitsListView(ListAPIView):
#     queryset = UserHabits.objects.all()
#     serializer_class = UserHabitsSerializer
#     permission_classes = [IsAuthenticated, IsOwner]


# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer
