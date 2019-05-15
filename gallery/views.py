from django.shortcuts import render
from .models import Image


def gallery_home(request):
    '''
    function to render all index page with all images
    '''
    images = Image.all_images()
    return render(request, 'gallery/gallery-home.html', {"images": images})


def search_results(request):
    '''
    function to handle searching for images by category and rendering the
    results
    '''
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'gallery/search.html',
                      {"message": message, "categories": searched_images})
    else:
        message = ""
        return render(request, 'gallery/search.html', {"message": message})
