# Django Polls Application
!['image'](https://github.com/CreativeDave/django_polls/blob/master/media/polls_gif.gif)
## Project Overview
> This is the completed version of the official [django tutorial](https://docs.djangoproject.com/en/2.1/intro/tutorial01/). It can be used to work through my [CRUD Workout and Command Line SQL exercise](https://github.com/CreativeDave/django_polls/blob/master/materials/CRUD_Workout.md).
### Getting Started
Completing the django tutorial was an exciting experience and I think every python programmer should do it. If you just want to quickly have a working app to run through my exercises, then follow the instructions below.

  1. Create a new virtual environment for this project in your directory of choice:  ``` $ python3 -m venv polls_venv```
  2. Navigate into this directory and activate the environment ```source bin/activate``` or on Windows ```source Scripts/activate```
  3. Clone this repository ```git clone https://github.com/CreativeDave/django_polls```
  4. Make sure django is installed ```python -m django --version``` and if not, install django ```pip install django```
  5. Open the django_polls folder and migrate the database: ```python manage.py makemigrations``` then ```python manage.py migrate```
  6. Finally, start the django development server ```python manage.py runserver``` and open http://127.0.0.1:8000/polls in your browser.
  7. Use the username: *admin123* and password: *admin123* to login to the admin portal to modify questions and choices. You can reach the admin portal at http://127.0.0.1:8000/admin.
