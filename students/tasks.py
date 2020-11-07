import csv
from rest_framework.response import Response
from students import models as student_model
from celery import shared_task

@shared_task
def upload_file_sql(file_name):
    data = {}
    with open(file_name, 'r') as file:
        csv_file = csv.DictReader(file)
        for item in csv_file:
            roll_no = item.get('roll_no')
            name = item.get('name')
            father_name = item.get('father_name')
            email_id = item.get('email_id')
            phone_no = item.get('phone_no')
            data.update({'roll_no': roll_no, 'name': name, 'father_name': father_name, 'email_id': email_id,
                         'phone_no': phone_no})
            student_model.Student.objects.create(**data)
    return Response({"message": "Upload successful data!"})



@shared_task
def adding_task(x, y):
    return x + y