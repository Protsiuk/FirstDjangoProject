from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse

from publications.models import Publication, PublicationLike
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
    paginator = Paginator(publications, 5)
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


def single_publication(request, publication_id):
    publication = get_object_or_404(Publication, pk=publication_id)

    return render(request, "single_publication.html", {"publication": publication})
    # publication = Publication.objects.get(pk=publication_id)


def like_single_publication(request, publication_id):
    if request.user.is_authenticated():
        publication = get_object_or_404(Publication, pk=publication_id)
        if PublicationLike.objects.filter(publication=publication, user=request.user).exists():
            PublicationLike.objects.filter(publication=publication, user=request.user).delete()
        else:
            PublicationLike.objects.create(publication=publication, user=request.user)
        return HttpResponseRedirect(reverse("single_publication", kwargs={"publication_id": publication_id}))
    else:
        return HttpResponseRedirect(reverse("login"))

    # @login_required(login_url="/login/")
    # def sign_out(request):
    #     logout(request)
    #     return HttpResponseRedirect(reverse("home"))