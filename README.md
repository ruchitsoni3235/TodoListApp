# Django To-Do List Application

A simple to-do list web application built with Django. Users can add, edit, delete, and cross and uncross the tasks as completed.

## Features

- Add new tasks
- Edit tasks
- Delete tasks
- Cross the task as completed

## 🛠️ Tech Stack

- Python 3
- Django
- HTML/CSS (with Bootstrap or plain styling)
- SQLite3

Run Locally
  1. Clone the repo
 bash
   git clone https://github.com/ruchitsoni3235/todo-list-django.git
   cd todo-list-django

2. MAKE Migration
  python manage.py makemigrations

3. MAKE Migration
  python manage.py migrate
 
4. Start the server
  python manage.py runserver

5. Visit in browser:

http://127.0.0.1:8000/
  
6. Project Structure:
   
   todo_list/
├── manage.py
├── todo_list/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── app_name/
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   └── ...
└── README.md



