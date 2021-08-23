from .models import Category

def categories(request):
    """ all categories """
    return{
        'categories': Category.objects.all()
    }
