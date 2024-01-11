from rest_framework import serializers

from useful_habits.models import Habit
from useful_habits.validators import valid_duration


class HabitSerializer(serializers.ModelSerializer):
    duration = serializers.IntegerField(validators=[valid_duration])

    def validate_connectivity(self, data):
        if data['pleasantness'] is True and data['connectivity'] is not None:
            raise serializers.ValidationError(
                "В связанные привычки могут попадать только "
                "привычки с признаком приятной привычки"
            )
        else:
            return data

    def validate_pleasantness(self, data):
        if (data['pleasantness'] is True and
                data['connectivity'] is not None and
                data['award']):
            raise serializers.ValidationError(
                "У приятной привычки не может "
                "быть вознаграждения или связанной привычки."
            )
        else:
            return data

    def validate_award(self, data):
        if data['connectivity'] is not None and data['award']:
            raise serializers.ValidationError(
                "Нельзя одновременно выбрать "
                "связанные привычки и указать вознаграждение."
            )
        else:
            return data

    class Meta:
        model = Habit
        fields = "__all__"


