...............djnago install step by step.........................
step-1>> python -m venv env
step-2>>. env/Scripts/activate
step-3>>pip install django
step-4>>django-admin startproject myproject
step-5>>cd myproject/
step-6>>python manage.py startapp store
step-7>>myproject vitre settings.py installed_app nice likho 'store'
step-8>>myproject > urls.py jabo path, diya include likhte hoibe 
urlpatterns = [

]
step-9>>python manage.py runserver
step-10>>store folder cerate korte hoibe tar name 'templates' tar modhe rakhte hoibe
step-11>>store folder cerate korte hoibe tar name 'static' tar modhe rakhte hoibe 'assets' and 'forms' folder
step-12>>head section nice likhte hoibe {% load static %}
step-13>> views.py file 
step-14>>design na pele command 'python manage.py collectstatic
step-15>> python manage.py makemigraions
step-16>> python manage.py migrate
step-17>> python manage.py createsuperuser
