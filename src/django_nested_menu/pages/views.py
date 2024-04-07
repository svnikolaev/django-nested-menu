from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Page


def page_view(request, slug=None, path=None):
    if slug:
        page = get_object_or_404(Page, slug=slug)
    elif path:
        page = get_object_or_404(Page, path=path)
    else:
        raise Http404("No Slug or Path provided")
    return render(request, 'pages/page.html', {'page': page})
