from django.shortcuts import render
import datetime

# Create your views here.
data = {
   'numbers': [1,2,3,4,5],
   'number': 15,
   'val': 120,
   'fullname': "I'am Abdul Khaleq",
   'name': "abdul khaleq",
   'date': datetime.datetime.now(),
   'empty': '',
   'dic':[
    {'name': 'zed', 'age': 19},
    {'name': 'amy', 'age': 22},
    {'name': 'joe', 'age': 31},
],
'size': 12345678,
'upname': 'ABDUL KHALEQ',
'num_messages': 5,
'time': datetime.datetime.now(),
'arr': [
    {'name': 'zed', 'age': 19},
    {'name': 'amy', 'age': 22},
    {'name': 'joe', 'age': 31},
],

}
def index(request):
    return render(request, 'index.html', data)

def products(request):
    return render(request, 'products.html', data)

def contact(request):
    return render(request, 'contact.html', data)

def about(request):
    return render(request, 'about.html', data)