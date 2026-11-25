# Django Calculator

A calculator web app built with Django, as a learning project. Type an expression, submit it, and the page shows the result.

## Features

- One-page calculator with a Bootstrap layout
- Sends the expression to the server and shows the result on the same page
- Shows an error message when the expression is not valid

## Built with

- Python 3, Django
- Django templates and Bootstrap

## Run it locally

```bash
git clone https://github.com/hamzakhalem/django-calcolator.git
cd django-calcolator
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install django
export DJANGO_SECRET_KEY="any-long-random-string"   # PowerShell: $env:DJANGO_SECRET_KEY="..."
python manage.py migrate
python manage.py runserver
```

Then open http://127.0.0.1:8000.

## Note

The server evaluates the expression with Python's `eval()`. That's fine for a local exercise, but don't deploy it publicly as it is: a real version should parse the expression and allow only numbers and operators.

## Project structure

```
calculator/   Project settings and root URLs
calcapp/      Views for the form and the result
templates/    The calculator page
```
