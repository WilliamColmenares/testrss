# RSS feed

This is a simple app that collects news from google's rss feed and retrieves the title and partial content of the news via rest api

## Usage

Run the migrations & install requirements

```python3
python3 manage.py makemigrations & python3 manage.py migrate
```

```python
python3 -m pip install -r requirements.txt
```

Then we are good to go, You can start the server and the celery beat worker by typing at the root folder

```pythoncelery -A rssfeedtest worker -l info -B
celery -A rssfeedtest worker -l info -B
```

This will query each 10 seconds the rss feed to collect new news articles. (this can be changed in the settings.py file)

Run the project by typing 

```python
python3 manage.py runserver
```

And go to 127.0.0.1:8000 to retrieve the collected news via rest api.