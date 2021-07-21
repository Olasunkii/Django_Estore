from .models import Category

#this function helps add category to the navar bar. A setting is done in settings
def categories(request):
    return {
        'categories': Category.objects.all()
    }