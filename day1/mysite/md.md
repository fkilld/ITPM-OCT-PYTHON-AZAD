

### **Steps to Create and Register a Django Application**

#### 1. **Add the App to `INSTALLED_APPS` in `settings.py`**

Open your `settings.py` file and register your app by adding it to the `INSTALLED_APPS` list:

```python
INSTALLED_APPS = [
    # Default Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Custom apps
    'myapp',  # Register your app here
]
```

---
---

#### 2. **Create a View in `views.py`**

In the `views.py` file of your app (`myapp`), define the view function:

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World')
```

#### 3. **Create `urls.py` in Your Application Folder**

In the root directory of your app (`myapp`), create a new file called `urls.py` and define the URL patterns for your views:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # URL pattern for the index view
]
```

---

#### 4. **Include App URLs in the Main `urls.py`**

In the project's main `urls.py` file, include the app's URLs:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Include the app's URLs
]
```


---

#### 5. **Run the Server**

Start the development server using the following command:

```bash
python manage.py runserver
```

---

#### 6. **Check the Output in the Browser**

Open your browser and go to:

```
http://localhost:8000
```

You should see the "Hello World" message displayed.

---

### **Summary**
- Register your app in `INSTALLED_APPS`.
- Create `urls.py` in the app folder and define the URL patterns.
- Include the app's URL patterns in the project's `urls.py`.
- Write a view function in `views.py`.
- Run the server and verify the result in the browser.
