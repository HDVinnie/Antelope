from django.http import HttpResponse

def index(request):
    return HttpResponse("Antelope.")

def login(request):
    return HttpResponse("Login.")

def register(request):
    return HttpResponse("Registration.")
