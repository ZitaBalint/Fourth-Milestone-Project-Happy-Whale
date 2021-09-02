from django.shortcuts import render

# Create your views here.


def profile(request):
    """ Return profile.html page """
    return render(request, 'profile/profile.html')