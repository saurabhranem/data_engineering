from django.conf.urls import url
from . import apis


urlpatterns = [
    url(r'^student/', apis.StudentApi.as_view()),
    url(r'^update-student/(?P<pk>[0-9]+)', apis.UpdateStudentApi.as_view()),
    url(r'^delete-student/(?P<pk>[0-9]+)', apis.DeleteStudentApi.as_view()),
    url(r'^upload-csv/', apis.update_student_csv),
]