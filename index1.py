from django.http import Httpresponce

def index(request):
    return Httpresponce('hello world')
