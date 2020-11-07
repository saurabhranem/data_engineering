from rest_framework import serializers
from students import models as student_models

class StudentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = student_models.Student
        fields = ('roll_no', 'name', 'father_name', 'email_id', 'phone_no',)


class StudentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = student_models.Student
        fields = ('phone_no',)

