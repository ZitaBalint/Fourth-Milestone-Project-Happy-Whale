from django.shortcuts import render

# Create your views here.


def profile(request):
    """ Return index.html page """
    return render(request, 'profiles/profile.html')


