# agile-project
Sample project that exposes the 4 values and 12 principles of Agile Software Development.



Setup
=====

Cloning the repository
----------------------
```
$ git clone https://github.com/andrei-elizaga/agile-project.git
```

Create `.env` file with values:
------------------------------

```
DEBUG=True
SECRET_KEY='<secret_key>'
```

Install packages
----------------
```
$ pipenv install
```

Running the server
------------------
```
$ cd agile_project
$ pipenv run python manage.py runserver
```

Running `black` code formatter
------------------------------
```
$ pipenv run ./mkblack --check
$ pipenv run ./mkblack --diff
$ pipenv run ./mkblack
```

Running Tests
-------------
