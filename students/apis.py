# from rest_framework_tracking.mixins import LoggingMixin
from rest_framework import generics, permissions, response, status, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
import os
from students import serializers as student_serializer
from students import models as student_model
from students import tasks




class StudentApi(generics.ListCreateAPIView):
    queryset = student_model.Student.objects.all()
    serializer_class = student_serializer.StudentCreateSerializer


class UpdateStudentApi(generics.UpdateAPIView):
    queryset = student_model.Student.objects.all()
    serializer_class = student_serializer.StudentUpdateSerializer


class DeleteStudentApi(generics.DestroyAPIView):
    queryset = student_model.Student.objects.all()


def handle_uploaded_file(uploaded_file):
    """
     This method gets the uploaded file and writes it in the upload dir under the same name
    """
    fname = "create_student.csv"
    project_path = os.getcwd()
    loc = project_path + '/static/'
    filename = fname
    _fname = '%s%s' % (loc, filename)
    with open(_fname, 'wb+') as destination:
        for chunk in uploaded_file.chunks():
            destination.write(chunk)
    return _fname


@api_view(['GET', 'POST'])
def update_student_csv(request,):
    if request.method == 'POST':
        my_file = request.FILES['student_list']
        _fname = handle_uploaded_file(my_file)
        tasks.upload_file_sql.delay(_fname)
    return Response({"message": "File Received!"})

