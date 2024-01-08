


set -o errexit  # exit on error

pip install pipenv
pipenv shell
pipenv install

python manage.py collectstatic --no-input
python manage.py migrate