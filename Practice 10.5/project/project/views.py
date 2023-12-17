from django.shortcuts import render 
from datetime import datetime



def home(request) :
     
    dummy_posts = [
        {
            'title': 'Introduction to Django',
            'content': 'django is a high-level Python web framework...',
            'author': 'John Doe',
            'date_posted': datetime.now(),
            'age' : 123456
        },
        {
            'title': 'Getting Started with Django Models',
            'content': 'Django models allow you to define your data models...',
            'author': 'Jane Smith',
            'date_posted': '2023-02-02',
        },
        {
            'title': 'Building Views in Django',
            'content': 'Views handle the processing of user requests in Django...',
            'author': 'Bob Johnson',
            'date_posted': '2023-03-10',
        },

        ['a','v','c']
        
    ]
    return render(request,'home.html',{'posts': dummy_posts }) 

   
