# Django `3.2.2` learning docs

> Following _Freecodecamp_'s - **[Python Backend Web Development Course (with Django)](https://www.youtube.com/watch?v=jBzwzrDvZ18)** tutaorial by [_Code with Tomi_](https://www.youtube.com/c/CodeWithTomi)

### 1. Make a django project

```
django-admin startproject <project_name>
```

> We can create different apps in a django project
>
> Example:
>
> 1. **Twitter**
>
> -   **Twitter** is a project
> -   _Home_ page is an app
> -   _Explore_ is an app
> -   _Notifications_ is an app
>
> 2. **Instagram**
>
> -   **Instagram** is a project
> -   _Home_ is an app
> -   _Search_ is an app
> -   _Messages_ is an app

---

### 2. Make an app inside your project

```
python manage.py startapp <app_name>
```

#### `urls.py`

-   In our **app**, we need to create a `urls.py` file, which will handles all the url rounting of that certain app.
-   Inside `urls.py`, we need to import `path` from `django.urls` and `views` (_views.py_) from current **app**.
-   and we need to create a `urlpatterns` list, which will contain all the paths of our **app**.
-   Each _path_ is a `path()` function, which takes:
-   1. the _route_ (url pattern)
-   2. _views_'s function, from _views.py_
-   3. _name_ for naming our urls.

Example:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
]
```

-   here, `views.index` is a function, which returns the html in `index()` function.

#### `views.py`

-   Now, we need to create our `index()` function in `views.py`
-   we need to send our `html` as a **HTML response**, for which we need to import `HttpResponse` from `django.http`.
-   And we will return the `HttpResponse` which is having the html of our webpage.

Example:

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>Hello ji</h1>")
```

#### `urls.py` (project)

-   We need to include the urls which we have made inside our **app** in our main **project**.
-   To include those paths, we need to use `include()` function from `django.urls`.
-   It takes our app's urls path, from where we are accessing the webpage.
-   We use `include()` inside `path()` function as $2nd$ argument.
-   $1st$ argument is same, the _url pattern_.

Example:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]
```

---

### 3. Run your project

```
python manage.py runserver
```

-   We will see that our app will run on the _localhost_ server, mostly `8000` port.

```
http://127.0.0.1:8000
```

---

### 4. HTML Template files

-   Instead of string of _html_, we can actually pass our `html` template file.
-   We need to create a `templates` folder in our **project** directory.
-   In which we include our _html_ template file, which will be rendered in our **app**.

#### `settings.py`

-   We need to know django, that use our `templates` folder, for html templates.
-   We need to add `templates` file in `settings.py` in our **project** directory.
-   Inside the `TEMPLATES` list, in `DIRS` key, we add our `templates` folder path like this:

```python
'DIRS': [BASE_DIR, "templates"],
```

-   our `templates` folder is followed by the path of our base dire, which is stored in `BASE_DIR` variable.

#### `urls.py` (app)

-   Let's add another _path_, in which we'll use our _html_ template.

```python
path("about", views.about, name="about")
```

#### `urls.py` (project)

-   We need to add this _path_ into our project folder also, so that it can recognize this _path_ too.

```python
path("about", include("myapp.urls"))
```

#### `views.py`

-   We need to add our _html_ template.
-   And, we need to render our _html_ file, so we'll use `render()` function from `django.shortcuts`.
-   In `render()` function, we pass our request then our _html_ template file.

```python
def about(request):
    return render(request, "about.html")
```

---

### 5. rendering data from backend in html

We can add dynamic data in our `html` template

#### `views.py`

-   We create a dictionary which has the data required.
-   The dictionary is then passed into the `render()` function

```python
def about(request):
    context = {
        "name": "hasbulla"
        "age" : "18"
    }
    return render(request, "about.html", context)
```

#### `about.html`

-   Based on the keys created in the context dictionary.
-   Key belonging to the value is placed in `{{}}`.
-   We need to use [**jinja**](https://svn.python.org/projects/external/Jinja-2.1.1/docs/_build/html/templates.html) template in our _html_ file.

```html
<h1>I am {{name}}</h1>
```

---

### 6. Render user input from html

-   We can take user input in the html, using the form or input tag.
-   We need to send the data in backend, so we need a submit button too.

#### `form.html`

```html
<form action="" method="">
    <textarea name="usertext" id="textarea" cols="100" rows="10">
{{text}}</textarea
    >
    <br />
    <input type="submit" value="Submit" />
</form>
```

-   `action=` sends the data to the particular URL
-   `method=` can be a get request or post request

```html
{% if word_count %}
<h1>Total words are: {{word_count}}</h1>
{% endif %}
```

-   This jinja code checks if `word_count` exists.
-   Based on the above boolean argument `Total words are: {{word_count}}` is rendered.

#### `views.py`

-   We use `GET` attribute of `request` parameter to fetch the user data from the `html` file.
-   `GET` is a dictionary, and contains the _name_ of all html tags as keys and their values as values.

```python
try:
    words = request.GET["usertext"]
    return render(request, "form.html", {"text": words, "word_count": len(words.split())})
except Exception:
    return render(request, "form.html")
```

-   This code block checks if the get request works , if it does then we render the html with `word_count`
    else we dont render it with `word_count`.

---

### 7. `GET` and `POST` method

-   `POST` request is used when we want to send the data confidentially.
-   `GET` request is used when we don't work with confidential data.
-   `GET` method carries request in parameter appended in URL and it is less secure than `POST` method.

```html
<form method=""></form>
```

-   When method is empty it defaults to `GET`.

#### `views.py`

```python
words = request.POST["usertext"]
```

-   The `request.GET` is changed to `request.POST`

#### `form.html`

-   When making a `POST` request a `csrf_token` must be passed on to prevent hacker attacks.

```html
<form method="POST">{% csrf_token %}</form>
```

---

### 8. Adding Static files

-   To add _static_ files like _stylesheets_, javascript files etc.., we need to store them in `static` folder.

#### `settings.py`

-   We need to tell django where to locate _static_ files.
-   So, in `settings.py`, after `STATIC_URL = '/static/'` code, we need to add one line in the code.

```python
import os
STATICFILES_DIRS = (os.path.join(BASE_DIR , "static") , )
```

-   The variable name should be the exact same as above.

#### html files

-   Inside _HTML_ templates, where we use those _static_ files, we need to write `load static` jinja command on the top of html code.

```html
{% load static %}
```

-   We also have to specify `static` in the link of static files inside _HTML_ templates, where we are linking those files.

```html
<link rel="stylesheet" href="{% static 'style.css' %}" />
```

---

### 9. Django Models

-   We can access and manage data in django using **django models**.
-   A **django model** works as a _table_ in the database.
-   We don't need to excute _SQL_ queries externally, we can make **django models** which will handle all those things automatically.

#### `models.py` (myapp)

-   We create a **model** in `models.py`, using class (`OOP`).

Example:

```python
class Student:
    roll_no: int
    name: str
    cls: str
    total_marks: int | float
    is_pass: bool
```

#### `views.py`

-   We can use our _django_ **models** in our template files to render the data.
-   We need to create an instance of our class, i.e. a row in table, and we can pass it in `render()` function.
-   Currently, we are creating instances, not adding the data in original database.

Example:

```python
def student_page(request):
    std1 = Student()
    std1.name = "Karan"
    std1.cls = "12"
    std1.roll_no = 20
    std1.total_marks = 300
    std1.is_pass = True

    return render(request, "details.html", {"student1": std1})
```

#### `details.html`

-   In our _html_ template file, we can access it using `.` dot notation, same as we access in python, but using _jinja_ template.

Example:

```html
<div class="card" id="card-2">
    <div class="details">
        <i class="fa-solid fa-graduation-cap"></i>
        <h2>{{student1.name}}</h2>
    </div>
    <h3 class="class">
        {{student1.cls}}<sup>th</sup
        ><span>&emsp;-&ensp;{{student1.roll_no}}</span>
    </h3>
    <h3 class="marks">Total marks: {{student1.total_marks}}</h3>
    <br />
    <h2 class="is_pass">{{student1.is_pass}}</h2>
</div>
```

-   But if we need to show data in same template multiple times, using _jinja_ template, we can make for loop, which will reduce the code.

Example:

```html
{% for student in students %}
<div class="card" id="card-2">
    <div class="details">
        <i class="fa-solid fa-graduation-cap"></i>
        <h2>{{student.name}}</h2>
    </div>
    <h3 class="class">
        {{student.cls}}<sup>th</sup>
        <span>&emsp;-&ensp;{{student.roll_no}}</span>
    </h3>
    <h3 class="marks">Total marks: {{student.total_marks}}</h3>
    <br />
    {% if student.is_pass %}
    <h2
        class="is_pass"
        style="background:linear-gradient(135deg, #42e695 0%,#3bb2b8 100%);"
    >
        Pass
    </h2>
    {% else %}
    <h2
        class="is_pass"
        style="background:linear-gradient(135deg, #F5515F 0%,#A1051D 100%);"
    >
        Fail
    </h2>
    {% endif %}
</div>
{% endfor %}
```

-   Same as `if` statements, we need to end `for` loops too.
-   In Python, only the code indented inside `if`/`loops` execute, but in html, we need to make sure where it should be ended.

---

### 10. Django Admin pannel and Manipulation of Database

-   Earlier, we have created our _django_ **model** in `models.py`, but it was just a boilerplate.

#### `models.py` (myapp)

-   To create the database, we need to do some modifications to our **model**.
-   We need to:
-   -   Inherit our **model** from `models.Model`.
-   -   Specify the type of value each field should have.
-   We don't need to create `id` field in any **model**, django will create it automatically and set it as **Primary Key**.

Example:

```python
class Student(models.Model):
    roll_no = models.PositiveSmallIntegerField("Roll no.")
    name = models.CharField("Name", max_length=20)
    cls = models.CharField("Class", max_length=2)
    total_marks = models.PositiveSmallIntegerField("Total marks")
    is_pass = models.BooleanField("Pass?", default=True)
```

-   There are various types, a field can have.
-   All field types are avaible [here](https://docs.djangoproject.com/en/3.2/ref/models/fields/#model-field-types)

#### `settings.py` (django_app)

-   Now that we have created our database model, we need our _django_ project to identify it.
-   And, we have created it inside `myapp` app, so we need to include it in `INSTALLED_APPS` in `settings.py` of our main django project (`django_app`).

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "myapp",     # <-------
]
```

#### Terminal work

-   We need to tell django to make the database accordingly.
-   For that, we first need to stage our changes, just like we execute our query (not commit).
-   So, we need to run `makemigrations` command inside our django project in terminal.

```bash
python manage.py makemigrations
```

-   We'll see this kind of message, if we have wrote correct code, without any mistake.

```bash
$ python manage.py makemigrations
Migrations for 'myapp':
  myapp\migrations\0001_initial.py
    - Create model Student
```

-   To execute these changes, to make the table, we need to run `migrate` command inside our django project in terminal.

```bash
python manage.py migrate
```

-   It will create a `migrations` folder inside our app.

#### Admin pannel

-   Now, that we have made the changes, we can see and control everything in our django project using **Admin pannel**.
-   To access it, we need to create a _superuser_, with which we can login in our admin pannel
-   To create a _superuser_, we need to run following command inside our django project in terminal.

```bash
$ python manage.py createsuperuser
```

-   We need to create a _username_ and _password_ (compulsory).
-   After creating a _superuser_, we can access the **Admin pannel** using `http://127.0.0.1:8000/admin/` url.

#### `admin.py` (myapp)

-   We also need to register our model in django **Admin pannel** to view in admin pannel.
-   We'll use `admin.site.register()` function to register our model.

```python
from django.contrib import admin
from .models import Student

# Register your models here.
admin.site.register(Student)
```

-   Now, we can access our _model_ through **Admin pannel**.
-   We can add some rows manually, which basically called as `objects` in a _model_.

#### `views.py` (myapp)

-   To access the data from our _model_, we need to import it.
-   To fetch all the data, we'll use `objects.all()` method from our _model_.
-   It returns a list of objects (rows).

```python
def student_details(request):
    students = Student.objects.all()
    return render(request, "details.html", {"students": students})
```

---
