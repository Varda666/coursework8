# from rest_framework import serializers
#
# from useful_habits.models import Course, Lesson
# from useful_habits.serializers.habit import LessonSerializer
#
#
# class CourseSerializer(serializers.ModelSerializer):
#     # paid_course = serializers.PrimaryKeyRelatedField(required=False)
#     lessons_count = serializers.SerializerMethodField()
#     lessons = LessonSerializer(read_only=True)
#
#     def get_lessons_count(self, obj):
#         lessons_count = obj.lessons.count()
#         return lessons_count
#
#     def update(self, instance, validated_data):
#         course = Course.objects.get(pk=instance.id)
#         Course.objects.filter(pk=instance.id).update(**validated_data)
#
#
#         return instance
#
#     class Meta:
#         model = Course
#         fields = "__all__"
