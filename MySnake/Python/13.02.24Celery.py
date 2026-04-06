from celery import Celery

app = Celery('Hello', broker = 'amqp://guest@localhost//')

@app.task
def hello():
    return 'Hello world'