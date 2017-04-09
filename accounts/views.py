from django.shortcuts import render, HttpResponse
from accounts.models import User


def home_page(request):
    # print(request.GET)
    # users = User.objects.filter(username='Frog').order_by("-id")
    keyword = request.GET.get("keyword")
    users = User.objects.all()
    if keyword:
        users = users.filter(username__icontains=keyword)
        print(User.objects.filter(username__icontains=keyword).query)
    return render(request, "home_page.html", {"users": users})
    # return HttpResponse("Respons something")

# Create your views here.
