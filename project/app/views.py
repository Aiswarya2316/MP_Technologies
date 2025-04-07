from django.shortcuts import render,redirect



def home (req):
    return render(req,'home.html')

def python (req):
    return render(req,'python.html')

def java (req):
    return render(req,'java.html')

def c (req):
    return render(req,'c.html')

def cpp (req):
    return render(req,'cpp.html')

def react (req):
    return render(req,'react.html')

def maths (req):
    return render(req,'maths.html')

def contact (req):
    return render(req,'contact.html')
