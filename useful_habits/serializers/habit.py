from rest_framework import serializers

from useful_habits.models import Habit
from useful_habits.validators import valid_duration


class HabitSerializer(serializers.ModelSerializer):
    duration = serializers.IntegerField(validators=[valid_duration])
    

    def validate_con(self, data):
        if data['connectivity'] is not None:
            raise serializers.ValidationError("Нельзя одновременно выбрать связанные привычки и указать вознаграждение")
        else:
            return data

    def validate_ple(self, data):
        if data['pleasantness'] is True:
            return data
        else:
            raise serializers.ValidationError("В связанные привычки могут попадать только привычки с признаком приятной привычки")

    def validate_awa(self, data):
        if data['pleasantness'] is True:
            raise serializers.ValidationError(
                "У приятной привычки не может быть вознаграждения или связанной привычки.")
        else:
            return data






    # # paid_lesson = serializers.PrimaryKeyRelatedField(required=False, read_only=True)
    # link = serializers.URLField(validators=[valid_url])

    class Meta:
        model = Habit
        fields = "__all__"


