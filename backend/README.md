
## Setup

The first thing to do is to clone the repository:

```sh
$ cd backend
```


Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:

    You can now run the development server:

        $ python manage.py runserver

And navigate to `http://127.0.0.1:8000/`.
Or navigate to `http://127.0.0.1:8000/users/`.
Or navigate to `http://127.0.0.1:8000/posts/`.

Others commands:
    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py createsuperuser

    $ python manage.py runserver

python3 manage.py livereload
python3 manage.py runserver