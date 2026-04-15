# Django Static Pages With No Templates

Create 4 web pages with no style, each page should have the following tags:

1. nav with anchor tags for every page, use | as separator
2. h1
3. h2
4. p

Submit repo with markdown file with blocks of code for:

* views.py
* urls.py
* settings.py (INSTALLED_APPS only)

Include screenshots for every page.

Use only django.http.HttpResponse, for every page add any of these data (include name and values for every element using f strings with ol or ul tags):

* 3 variables with different data types
* a list of mixed data types of length 6
* a dictionary with string keys and different data types values of length 5

# Example Code

config/settings.py

```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'static_pages_1',
]

```

config/urls.py

```python
from django.contrib import admin
from django.urls import path
from static_pages_1 import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('events/', views.events, name="events"),
    path('contact/', views.contact, name="contact"),
]
```
static_pages_1/views.py

```python
from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse
from django.middleware.csrf import get_token
from django.http import JsonResponse
from datetime import date

nav = """
    <nav>
        <a href='/'>Home</a> |
        <a href='/about/'>About Us</a> |
        <a href='/events/'>Events</a> |
        <a href='/contact/'>Contact</a>
    </nav>
"""
name = "Bobby"
age = 36
email = "bobbyboucher123@gmail.com"

home_body = f"""
    <ol>
        <li>Name: {name}</li>
        <li>Age: {age}</li>
        <li>Email: {email}</li>
    </ol>
    
"""
def home(request):
    content= f"""
    {nav}
    <h1>Welcome to Bismarck Testing Services!</h1>
    <h2>Please browse around.</h2>
    <p>Click on the About page to find a results example of a proctored exam at our Regina location.
    Click on the events page to find out about exams happening in your area.
    And feel free to utilize the Contact Us page if you have any questions or concerns.</p>
    """
    
    return HttpResponse(content + home_body)

def about(request):
    names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]
    scores = [92, 84, 73, 64, 89, 78]
    mixed_list = list(zip(names, scores))
    
    content = """
    {nav}
    <h1>This is the About Page. Below, you will find an example of a Final Exam our organization proctored.</h1>
    <h2>Here is a mixed list of names and their corresponding test scores.</h2>
    <p>As you can see, Alice got 92, Bob got 84, Charlie got 73, David got 64, Eve got 89, and Frank got 78 on the test.</p>
    <ol>
        {% for name, score in mixed_list %}
            <li>{{ name }} - {{ score }}</li>
        {% endfor %}
    </ol>
    """.replace("{nav}", nav)
    
    template = Template(content)
    html = template.render(Context({'mixed_list': mixed_list}))
    return HttpResponse(html)

def events(request):
    content_header = f"""
    {nav}
    <h1>Upcoming Events</h1>
    <h2>Here are some events that we have going on at our testing centre.</h2>
    <p>We have our Free CompTIA A+ Examinations coming up on June 26th. This is a $500 value. Spaces are limited!</p>
    """
    
    payload = {
        "title": "CompTIA A+ Blitz",
        "date": str(date(2026, 6, 26)),
        "location": "Regina, Saskatchewan",
        "description": "Free A+ Examinations ($500 Value!)",
        "vouchers": "Available for early birds",
        "price": "Free"
    }

    # This converts your dictionary into visible list items for the browser
    dict_items = "".join([f"<li>{key}: {val}</li>" for key, val in payload.items()])

    final_content = f"""
    {content_header}
    <ul>
        {dict_items}
    </ul>
    """
    
    return HttpResponse(final_content)

def contact(request):
    csrf_token = get_token(request)
    
    content = f"""
    {nav}
    <h1>Contact Us</h1>
    <h2>Get in Touch</h2>
    <p>Please fill out the form below or reach out via our social channels.</p>

    <form action="/contact/" method="POST">
        <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
        <label>Name:</label><br>
        <input type="text" name="name"><br><br>
        
        <label>Message:</label><br>
        <textarea name="message"></textarea><br><br>
        
        <button type="submit">Send Message</button>
    </form>
    """
    return HttpResponse(content)
```

# Screenshots

## Home Page
<img width="1919" height="1079" alt="Django Site Without Template (1)" src="https://github.com/user-attachments/assets/b3898dda-d530-43a2-b2c3-5e4255ad8c56" />

## About Us Page
<img width="1919" height="1079" alt="Django Site Without Template (2)" src="https://github.com/user-attachments/assets/5a18397c-d606-4450-be79-9468f46bbf33" />

## Events Page
<img width="1919" height="1079" alt="Django Site Without Template (3)" src="https://github.com/user-attachments/assets/5b6bd6d6-3cbd-49b7-99dd-76e3e9d4a63b" />

## Contact Us Page
<img width="1919" height="1079" alt="Django Site Without Template (4)" src="https://github.com/user-attachments/assets/3e0aa0bf-bdfe-43c2-ab1d-c8e6a035e37e" />
