from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is lost and found portal</h1>")