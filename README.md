# data_engineering
Django Upload CRUD and upload CSV Apps
This is a small Django project to demonstrate Django CRUD functionality and CSV upload functionality.

students: Implement CRUD using CBV (Class Based Views).
students: csv upload and upload data into DB using Rabbitmq, Celery, Docker.
Install Required Packages
The Django CRUD project only need a single Python package "Django", it was built and tested with Django 3.x version. To install it use the following command:

pip install -r requirements.txt

Running the Application
Before running the application we need to create the needed DB tables:

./manage.py migrate
Now you can run the development web server:

./manage.py runserver
To access the applications go to the URL http://localhost:8000/

I need a user and password to access "/api/v1/csv_sql/student/"
Yes, the "/api/v1/csv_sql/student/" demonstrate how CRUD can work with Django users, and you do need to create a user to test it, you can create a user using the following command:

./manage.py createsuperuser
To create a normal user (non super user), you must login to the admin page and create it: http://localhost:8000/admin/

API to upload CSV - 
/api/v1/csv_sql/upload-csv/

API to List DATA - 
/api/v1/csv_sql/student/
