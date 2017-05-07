from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import Http404

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse


from publications.models import Publication, PublicationLike, PublicationComment
from publications.forms import PublicationForm, PublicationCommentForm
from publications.serializers import PublicationSerializer, CreatePublicationSerializer

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from utils import gen_page_list


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

    # print("publications are ")

    # pagination of pages
    paginator = Paginator(publications, 5)
    page = request.GET.get('page', 1)
    try:
        publications = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        publications = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        publications = paginator.page(paginator.num_pages)
    page_nums = gen_page_list(int(page), paginator.num_pages)
    return render(request, "publications.html", {"publications": publications,
                                                 "form": form,
                                                 "page_nums": page_nums})


def single_publication(request, publication_id):
    publication = get_object_or_404(Publication, pk=publication_id)
    form = PublicationCommentForm()
    if request.method == "POST":
        form = PublicationCommentForm(request.POST)
        if form.is_valid():
            PublicationComment.objects.create(publication=publication,
                                              user=request.user,
                                              text=form.cleaned_data['text'])
            return HttpResponseRedirect(reverse("single_publication", kwargs={"publication_id": publication_id}))
    return render(request, "single_publication.html", {"publication": publication,
                                                       "form": form})
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


# @api_view(['GET', 'POST'])
# def publications_as_json(request, publication_id):
#     """
#     get:
#     return JSON data of requests publication
#
#     post:
#     return comment to POST Requests error
#     """
#     if request.method == "GET":
#         publication = get_object_or_404(Publication, pk=publication_id)
#         serializer = PublicationSerializer(publication)
#         return Response(serializer.data)
#     else:
#         return Response({"method": "POST"})



#!!! def publications_as_json(request, publication_id):
#     publication = get_object_or_404(Publication, pk=publication_id)
#     if publication_id <= publications():
#         return JsonResponse({"title": publication.title,
#                          "body": publication.body,
#                          "author": publication.author.first_name})
#     else:
#         return HttpResponse({"ERROR sorry, we can not fine this publications "})

class GetSinglePublicationView(APIView):
    serializer_class = PublicationSerializer

    def get_object(self, publication_id):
        try:
            return Publication.objects.get(pk=publication_id)
        except Publication.DoesNotExist:
            raise Http404

    def get(self, request, publication_id):
        publication = self.get_object(publication_id)
        return Response(self.serializer_class(publication).data)

    def delete(self, request, publication_id):
        publication = self.get_object(publication_id)
        publication.delete()
        return Response({"success": True})


class CreatePublicationView(APIView):
    serializer_class = CreatePublicationSerializer

    def post(self, request):
        serializer = self.serializer_class(request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            return Response({"asf": "rrr"})
        else:
            return Response(serializer.errors)
