<h1 align="center">Hi, I'm <span style="color:#15B1ED;">Tima</span>
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>
<h3 align="center">A passionate backend developer from Kyrgyzstan 🇰🇬</h3>

# Celery Test
**Celery** communication integration with **[Django](https://www.djangoproject.com/)** via **[Redis](https://redis.io/)** server. This repository explains how to set up **[Celery](https://docs.celeryq.dev/)** and integrate it with **[Django-Rest-Framework](https://www.django-rest-framework.org/)**.

## Installation
To get this project up and running you should start by installing Python on your computer. I would suggest that you create a virtual environment to store your project's dependencies separately. You can install virtualenv with

```bash
pip install virtualenv
```
Clone this repository then go to the project directory.
```bash
git clone https://github.com/orozbekov/django-celery-test.git
cd django-celery-test
```
In a terminal (mac/Linux) run the following command in the base directory of this project to create a virtual environment.
```bash
python3 -m venv .venv
```
That will create a new folder `.venv` in your project directory. Next activate it with this command on mac/Linux:
```bash
source .venv/bin/activate
```
Then install the project dependencies with this command:
```bash
pip install -r requirements.txt
```
Now you can run the project with this command:
```bash
python manage.py runserver
```

### Celery

Start celery worker with this command:
```bash
celery -A config worker -l info
```
Please note: For Celery's import magic to work, it is important where the celery commands are run. If you are in the same folder as manage.py, you should be right.

### Redis
Start the Redis server with this command:
```bash
redis-server
```

## Running Tests
To run tests, run the following command
```bash
python manage.py test apps/
```
<h3 align="center">Languages and Tools:</h3>
<p align="center">
<a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> 
    <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> 
</a> 
<a href="https://git-scm.com/" target="_blank" rel="noreferrer"> 
    <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> 
</a> 
<a href="https://www.linux.org/" target="_blank" rel="noreferrer"> 
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" alt="linux" width="40" height="40"/> 
</a>
<a href="https://postman.com" target="_blank" rel="noreferrer"> 
    <img src="https://www.vectorlogo.zone/logos/getpostman/getpostman-icon.svg" alt="postman" width="40" height="40"/> 
</a> 
<a href="https://www.python.org" target="_blank" rel="noreferrer"> 
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> 
</a>  
<a href="https://redis.io" target="_blank" rel="noreferrer"> 
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/redis/redis-original-wordmark.svg" alt="redis" width="40" height="40"/> 
</a>
</p>