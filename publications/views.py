from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from publications.models import Publication
from publications.forms import PublicationForm


def publications(request):
    form = PublicationForm()
    if request.method == "POST":
        form = PublicationForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            Publication.objects.create(title=data.get("title"),
                                       body=data.get("body"),
                                       image=data.get("image"),
                                       author=request.user)
    publications = Publication.objects.all()
    # pagination of pages
    paginator = Paginator(publications, 1)
    page = request.GET.get('page')
    try:
        publications = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        publications = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        publications = paginator.page(paginator.num_pages)
    return render(request, "publications.html", {"publications": publications,
                                                 "form": form})

