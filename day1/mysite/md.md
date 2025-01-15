

## Task: Creating a Django Project with Three Functional Applications

### Objective
You are required to create a Django project that contains three separate applications. Each application must be functional, meaning that each app will have its own views, URLs, and templates. You will need to ensure consistency across all applications by following a similar structure for each.

### Steps:

#### 1. **Create a New Django Project**
   - Start by creating a new Django project using the following command:
     ```bash
     django-admin startproject my_project
     ```

   - Change the directory to your newly created project folder:
     ```bash
     cd my_project
     ```

#### 2. **Create the First Application**
   - Create the first application using the following command:
     ```bash
     python manage.py startapp app1
     ```

   - Register this app in the `INSTALLED_APPS` section of your `settings.py` file:
     ```python
     INSTALLED_APPS = [
         # other apps
         'app1',
     ]
     ```

#### 3. **Create Views and URLs for App1**
   - In `app1/views.py`, create a simple view function:
     ```python
     from django.http import HttpResponse

     def home(request):
         return HttpResponse("Welcome to App1!")
     ```

   - In `app1/urls.py`, create a URL pattern for the view:
     ```python
     from django.urls import path
     from . import views

     urlpatterns = [
         path('', views.home, name='home'),
     ]
     ```

   - In the project's `urls.py` (located in the main project directory), include the URL configurations for `app1`:
     ```python
     from django.contrib import admin
     from django.urls import path, include

     urlpatterns = [
         path('admin/', admin.site.urls),
         path('app1/', include('app1.urls')),
     ]
     ```

#### 4. **Create the Second Application**
   - Create the second application using the following command:
     ```bash
     python manage.py startapp app2
     ```

   - Register this app in the `INSTALLED_APPS` section of `settings.py`:
     ```python
     INSTALLED_APPS = [
         # other apps
         'app2',
     ]
     ```

#### 5. **Create Views and URLs for App2**
   - In `app2/views.py`, create a simple view function:
     ```python
     from django.http import HttpResponse

     def home(request):
         return HttpResponse("Welcome to App2!")
     ```

   - In `app2/urls.py`, create a URL pattern for the view:
     ```python
     from django.urls import path
     from . import views

     urlpatterns = [
         path('', views.home, name='home'),
     ]
     ```

   - In the main `urls.py`, include the URL configurations for `app2`:
     ```python
     urlpatterns = [
         path('admin/', admin.site.urls),
         path('app1/', include('app1.urls')),
         path('app2/', include('app2.urls')),
     ]
     ```

#### 6. **Create the Third Application**
   - Create the third application using the following command:
     ```bash
     python manage.py startapp app3
     ```

   - Register this app in the `INSTALLED_APPS` section of `settings.py`:
     ```python
     INSTALLED_APPS = [
         # other apps
         'app3',
     ]
     ```

#### 7. **Create Views and URLs for App3**
   - In `app3/views.py`, create a simple view function:
     ```python
     from django.http import HttpResponse

     def home(request):
         return HttpResponse("Welcome to App3!")
     ```

   - In `app3/urls.py`, create a URL pattern for the view:
     ```python
     from django.urls import path
     from . import views

     urlpatterns = [
         path('', views.home, name='home'),
     ]
     ```

   - In the main `urls.py`, include the URL configurations for `app3`:
     ```python
     urlpatterns = [
         path('admin/', admin.site.urls),
         path('app1/', include('app1.urls')),
         path('app2/', include('app2.urls')),
         path('app3/', include('app3.urls')),
     ]
     ```

#### 8. **Test the Project**
   - Run the development server:
     ```bash
     python manage.py runserver
     ```
   - Open your browser and test each application:
     - Visit `http://127.0.0.1:8000/app1/` to see App1's view.
     - Visit `http://127.0.0.1:8000/app2/` to see App2's view.
     - Visit `http://127.0.0.1:8000/app3/` to see App3's view.

### Deliverables:
1. A Django project with three functional applications.
2. Each application must have:
   - A views.py file with at least one simple view.
   - A urls.py file with URL configurations for the views.
   - The application's URLs must be registered in the project's main urls.py file.
3. A final working version of the project that can be run locally.

### Evaluation Criteria:
- The project is organized into three applications.
- The views and URLs for each application are set up correctly and follow a consistent structure.
- The project is functional, and each application serves its view properly when accessed in the browser.

### Notes:
- Ensure the naming conventions are consistent (e.g., `views.py`, `urls.py`).
- Maintain proper indentation and formatting in your Python files.

