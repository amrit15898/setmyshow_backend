from django.shortcuts import render

# Create your views here.
def post_events(request):
    pass 


def front_page(request):
    return render(request, "frontpage.html")

