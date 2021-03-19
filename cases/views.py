from django.shortcuts import render

# Create your views here.
def cases(request):
    """A view that displays the cases page"""
    return render(request, "cases.html")