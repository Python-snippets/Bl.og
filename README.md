# Bl.og - WIP

# Demo

<http://royalturd.pythonanywhere.com>

Made with ❤  by royalturd using [Django](https://docs.djangoproject.com/en/4.0/) hosted on [pythonanywhere.com](https://www.pythonanywhere.com/)

<a href="#license"><img src="https://img.shields.io/badge/License-GPL_v3-blue" alt="License"></a>

[![Django CI](https://github.com/Python-snippets/Bl.og/actions/workflows/django.yml/badge.svg)](https://github.com/Python-snippets/Bl.og/actions/workflows/django.yml)

[![CodeQL](https://github.com/Python-snippets/Bl.og/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/Python-snippets/Bl.og/actions/workflows/codeql-analysis.yml)

<img src="https://github.com/Python-snippets/Bl.og/blob/master/screenshots/Screenshot%202021-08-04%20044809.png">

<img src="https://github.com/Python-snippets/Bl.og/blob/master/screenshots/Screenshot%202021-08-04%20045057.png">

### Features

- Create a user account and login with Github
- Create a Bl.og
- Edit Delete and all the basic stuff with enhanced [ckeditor](https://pypi.org/project/django-ckeditor-updated/)
- Logout and login to your account on any device not just the one you created it on
- Change your user account password
- Upload Images and manage your profile
- Like and Dislike
- Bugs 💩

### To-Do

- Automatic backup and restore database

## Running Bl.og (locally)

### clone this repo

```
https://github.com/Python-snippets/Bl.og.git
```

### Install Django

```
pip3 install django
```

### Prepare your environment

```
python -m venv env
```

```
source env/Scripts/activate
```

### Run The development server

```
python manage.py runserver
```

> **_NOTE:_** Everytime you run the server, login/register a new user and create a new to do list, everything will be saved in the [db.sqlite3](./db.sqlite3) database file. Make sure not to add the `db.sqlite3` file to the your commits for public/production use. (Trust me i am guilty of it 😢)

## Contributing

I love contributions, so please feel free to fix bugs, improve things, provide documentation. Just send a pull request.
