from django.shortcuts import render


def testing(request):
    return render(request, 'tester.html', {})
# Create your views here.
