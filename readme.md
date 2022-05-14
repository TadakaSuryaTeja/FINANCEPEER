# FINANCEPEER

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/TadakaSuryaTeja/FINANCEPEER.git
$ cd FINANCEPEER
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv venv
$ source venv/bin/activate
```

Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(venv)$ cd project
(venv)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

### Signup
Enter the user details and click on signup. The user will be created and the user will be navigated to homepage.

### Login

Login with the user credentials.

### Json Upload
After logging in, the user will be navigated to the upload page. The user will be able to upload the json file.

### To Create a Package

```sh
(venv)$ python setup.py bdist_wheel
```