source env/bin/activate
cd board
python manage.py makemigrations
python manage.py migrate
python manage.py runserver