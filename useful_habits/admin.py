from django.contrib import admin

from useful_habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        'owner', 'place', 'time', 'action', 'usefulness', 'pleasantness',
        'frequency', 'duration', 'is_public', 'award'
    )
    list_filter = (
        'owner', 'place', 'time', 'action', 'usefulness', 'pleasantness',
        'connectivity', 'frequency', 'duration', 'is_public', 'award'
    )
    search_fields = (
        'owner', 'place', 'time', 'action', 'usefulness', 'pleasantness',
        'connectivity', 'frequency', 'duration', 'is_public', 'award'
    )

# Register your models here.
