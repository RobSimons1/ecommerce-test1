from django.shortcuts import render
from .models import Cases

# Create your views here.
def cases(request):
    """A view that displays the cases page"""
    cases = Cases.objects.all()
    return render(request, "cases.html", {"cases": cases})