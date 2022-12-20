# Django `3.2.2` learning docs

> Following *Freecodecamp*'s -  **[Python Backend Web Development Course (with Django)](https://www.youtube.com/watch?v=jBzwzrDvZ18)** tutaorial by [*Code with Tomi*](https://www.youtube.com/c/CodeWithTomi)


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
