pipenv install django
pipenv shell
django-admin startproject myproject
# Run the development server to verify everything is set up correctly
python manage.py runserver
# Now, let's create a new app called "movies" to manage our movie-related data and views.
python manage.py startapp myapp

# after creating models, run the following commands to create the database and apply migrations
python manage.py makemigrations
python manage.py migrate
