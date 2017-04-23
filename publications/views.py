from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from publications.models import Publication
from publications.forms import PublicationForm


def publications(request):
    Publication.objects.filter(Q(pk=1) | Q(title="123"))


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

# VARIANT 2 (look to publication.html variant 3 paginations)
# def gen_page_list(page_number, page_count):
#     # Pagination generator
#     my_page = []
#     if page_count > 10:
#         if page_number <=4:
#             for key in range(1, 7):
#                 my_page.append(key)
#             my_page.append("...")
#             my_page.append(page_count)
#         elif page_number >= (page_count-4):
#             my_page.append(1)
#             my_page.append("...")
#             for key in range((page_count-5), (page_count+1)):
#                 my_page.append(key)
#         else:
#             my_page.append(1)
#             my_page.append("...")
#     else:
#         for key in range(0, page_count):
#             my_page.append(key+1)
#     return my_page

