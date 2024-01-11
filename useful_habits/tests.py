from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from useful_habits.models import Habit
from users.models import User


class ModelCreateTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            user_role='moderator',
            email='test@mail.com',
            name='TestName',
            is_staff=True,
            is_active=True,
        )
        self.user.set_password('123qwe')
        self.user.save()
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
            owner=self.user,
            place='Коридор',
            time='Любое',
            action='Ходить туда сюда',
            usefulness=True,
            frequency='once every two days',
            duration=2,
            is_public=True,
            award='Печенька',

        )

    def test_get_list(self):
        response = self.client.get(
            reverse('useful_habits:habit_list')
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            [
                {"count": 1,
                 "next": None,
                 "previous": None,
                 "results": [
                     {
                         "id": 1,
                         "duration": 2,
                         "place": "Коридор",
                         "time": "Любое",
                         "action": "Ходить туда сюда",
                         "usefulness": True,
                         "pleasantness": False,
                         "frequency": "once every two days",
                         "is_public": True,
                         "award": "Печенька",
                         "owner": "test@mail.com",
                         "connectivity": []
                     },
                 ]
                 },
            ]
        )

    def test_habit_create(self):
        data = {
            'owner': User.objects.get(email='test@mail.com'),
            'place': 'Любое',
            'time': 'Любое',
            'action': 'Приседать 30 раз',
            'usefulness': True,
            'frequency': 'once a day',
            'duration': 1,
            'award': 'Деньга',
        }
        response = self.client.post(
            reverse('useful_habits:habit_create'),
            data=data,
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            Habit.objects.all().count(),
            2
        )

    def test_habit_update(self):
        data = {'action': 'Ходить туда сюда Ходить туда сюда',
                'duration': 2,
                }
        responce = self.client.put(
            reverse(
                'useful_habits:habit_update',
                kwargs={'pk': self.habit.pk}),
            data=data,
            format='json'
        )
        self.assertEquals(
            Habit.objects.get(pk=self.habit.pk).action,
            'Ходить туда сюда Ходить туда сюда'
        )

    def test_habit_delete(self):
        response = self.client.delete(
            reverse('useful_habits:habit_delete', kwargs={'pk': self.habit.pk})
        )
        self.assertEqual(response.status_code, 204)
        self.assertEquals(
            Habit.objects.all().count(),
            1
        )
