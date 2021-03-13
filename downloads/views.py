from django.shortcuts import render

# Create your views here.
def downloads(request):
    """A view that displays the downloads page"""
    return render(request, "downloads.html")