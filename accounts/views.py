from django.shortcuts import render, HttpResponse
from accounts.models import Member

def home_page(request):
    members = Member.objects.all()
    # return HttpResponse("Respons something")
    return render(request, "home_page.html", {"name": "John",
                                              "fruits":["apple", "banana", "bash"]})
# Create your views here.
