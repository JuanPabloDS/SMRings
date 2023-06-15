
<h2 align="center">SMRING</h2>

## :scroll: Description

SMRING is a fictional e-commerce website for purchasing rings. On this website, you can register rings using the Django administrator. As a user, you can make purchases of as many rings as you wish. All purchases will be added to the shopping cart, where you can either proceed to checkout or remove items. To complete the purchase, you need to create a brief registration by providing your email address and password. Once logged in, you are ready to successfully finalize the purchase.

## :rocket: Technologies

The technologies usage in this project is:
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [JavaScript](https://www.javascript.com/)
- [Bootstrap](https://getbootstrap.com/)
- [JQuery](https://www.sqlite.org/)


##  :wrench: Setup
Clone this repository in your computer.
```
$ git clone https://github.com/JuanPabloDS/SMRings.git
```
After, install python development package:

Ubuntu.
```shell
$ sudo apt-get install python-dev
```

Fedora.
```shell
$ sudo dnf install python3-devel
```

Inside the project directory, you need to create your virtual enviroment and active it:
```shell
$ python -m venv pyenv
$ source pyenv/bin/activate
```

Upgrade pip:
```shell
$ pip install -U pip
```

Run the command to install the env requirements:
```shell
$ pip install -r requirements.txt
```

Run the migrations:
```shell
$ python manage.py migrate
```

Create your Django User:
```shell
$ python manage.py createsuperuser
```

Start the application:
```shell
$ python manage.py runserver
```

Look the swagger accessing *http://localhost:8000*
Look the django-admin accessing *http://localhost:8000/admin* and use your superuser email and password.