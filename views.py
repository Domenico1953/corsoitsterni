from django.http import HttpResponse

def home(request):
    return HttpResponse(f"<h1>ITS Academy Terni - Homepage ( core mio esternauno )</h1>")


