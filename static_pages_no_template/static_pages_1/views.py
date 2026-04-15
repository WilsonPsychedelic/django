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
