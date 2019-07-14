from bottle import route, run, static_file, view, redirect, request
 
 
import os
from datetime import datetime as dt
from random import randrange
 
 


@route("/static/<filename:path>")
def send_static(filename):
    return static_file(filename, root="static")


class TodoItem:
    def __init__(self, description):
        self.description = description
        self.is_completed = False


@route("/")
@view("index")
def index():
    tasks = [
        TodoItem("прочитать книгу"),
        TodoItem("учиться жонглировать 30 минут"),
        TodoItem("помыть посуду"),
        TodoItem("поесть"),
    ]
    return {"tasks": tasks}


@route("/api/roll/<some_id:int>")
def example_api_response(some_id):
    return {
        "requested_id": some_id,
        "random_number": randrange(some_id)
    }


@route("/api/delete/<uid:int>")
def api_delete(uid): 
    return redirect("/")


@route("/api/complete/<uid:int>")
def api_complete(uid): 
    return "Ok"


@route('/css/<filename>')
def send_css(filename):
    return static_file(filename, root='static/css')


@route('/js/<filename>')
def send_css(filename):
    return static_file(filename, root='static/js')


if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True)
