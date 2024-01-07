from django.db import models


# Create your models here.

class Habit(models.Model):
    FREQUENCY_CHOISES = [
        ('once every three hours', 'once every three hours'),
        ('twice a day', 'twice a day'),
        ('once a day', 'once a day'),
        ('once every two days', 'once every two days'),
        ('once every three days', 'once every three days'),
        ('once every four days', 'once every four days'),
        ('once every five days', 'once every five days'),
        ('once every six days', 'once every six days'),
    ]
    owner = models.ForeignKey(to='users.User', to_field='email', verbose_name='владелец', on_delete=models.DO_NOTHING )
    place = models.CharField(max_length=150, verbose_name='место выполнения')
    time = models.CharField(max_length=150, verbose_name='время выполнения')
    action = models.TextField(max_length=700, verbose_name='действие')
    usefulness = models.BooleanField(default=False, verbose_name='полезность')
    pleasantness = models.BooleanField(default=False, verbose_name='приятность')
    connectivity = models.ManyToManyField('self', symmetrical=False, default=False, verbose_name='связанные привычки')
    frequency = models.CharField(choices=FREQUENCY_CHOISES, max_length=150, verbose_name='переодичность')
    duration = models.IntegerField(verbose_name='время на выполнение в минутах')
    is_public = models.BooleanField(default=False, verbose_name='публичность')
    award = models.CharField(default='', blank=True, max_length=150, verbose_name='вознаграждение')


    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'


